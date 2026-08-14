# Preventing Insecure Network Connections

**Framework**: Security

Enforce secure network links in your app by relying on App Transport Security.

#### Overview

On Apple platforms, a networking security feature called App Transport Security (ATS) improves privacy and data integrity for all apps and app extensions. It does this by requiring that network connections made by your app are secured by the Transport Layer Security (TLS) protocol using reliable certificates and ciphers. ATS blocks connections that don’t meet minimum security requirements.

![Diagram showing how ATS blocks insecure connections, but lets secure traffic flow between your app and the network.](/images/com.apple.security/media-3162039@2x.png)

ATS operates by default for apps linked against the iOS 9.0 or macOS 10.11 SDKs or later. In cases where you need to connect to a server that isn’t fully secure—and that you can’t reconfigure to make more secure—you can add exceptions to loosen some of the ATS requirements.

> **Note**:  If you link your app against an SDK older than iOS 9.0 or macOS 10.11, ATS is disabled no matter which version of the operating system your app runs on.

##### Prefer High Level Frameworks in Your App

The system enforces ATS when you use the standard [`URL Loading System`](https://developer.apple.com/documentation/foundation/url-loading-system). Instances of [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession) automatically negotiate the most secure connection available from the server. The only action your app must take is to use secure URLs, like those beginning with `https`. Otherwise, ATS denies the connection and prints a console message:

```console
App Transport Security has blocked a cleartext HTTP (http://) resource
load since it is insecure. Temporary exceptions can be configured via
your app's Info.plist file.
```

ATS doesn’t apply to calls your app makes to lower-level networking interfaces like the [`Network`](https://developer.apple.com/documentation/network) framework or [`CFNetwork`](https://developer.apple.com/documentation/cfnetwork). In these cases, you take responsibility for ensuring the security of the connection. You can construct a secure connection this way, but mistakes are both easy to make and costly. It’s typically safest to rely on the [`URL Loading System`](https://developer.apple.com/documentation/foundation/url-loading-system) instead.

##### Ensure the Network Server Meets Minimum Requirements

A secure server establishes its identity using an X.509 digital certificate. A connecting client examines this certificate to perform default server trust evaluation, which includes checking that the certificate:

- Has an intact digital signature, showing that the certificate hasn’t been tampered with.
- Isn’t expired.
- Has a name that matches the server’s DNS name.
- Is signed by another valid certificate, which is in turned signed by another, and so on back to a trusted anchor certificate, which must be issued by a Certificate Authority (CA). The anchor certificate must be part of the client operating system, as indicated in [`Lists of available trusted root certificates in iOS`](https://developer.apple.comhttps://support.apple.com/en-us/HT204132), or be installed on the client by the user or a system administrator.

ATS requires all of these things, and then provides extended security checks:

- The server certificate must be signed with either a Rivest-Shamir-Adleman (RSA) key of at least 2048 bits, or an Elliptic-Curve Cryptography (ECC) key of at least 256 bits.
- The certificate must use the Secure Hash Algorithm 2 (SHA-2) with a digest length, sometimes called a *fingerprint*, of at least 256 bits (that is, SHA-256 or greater).
- The connection must use Transport Layer Security (TLS) protocol version 1.2 or later.
- Data must be exchanged using either the AES-128 or the AES-256 symmetric cipher.
- The link must support perfect forward secrecy (PFS) through Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) key exchange.

> **Note**:  [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession) automatically handles server trust evaluation for you, but enables you to customize the process, for example to extend trust to a self-signed certificate embedded in your app, or to bypass certificate expiry. When ATS is enabled, you can no longer loosen trust evaluation requirements that way, but you can still tighten them — for example, to implement certificate pinning. For more information, see [`Performing manual server trust authentication`](https://developer.apple.com/documentation/foundation/performing-manual-server-trust-authentication).

##### Optional Niap Functional Package for Tls Requirements

ATS provides support to further restrict default TLS client behavior to help meet requirements outlined by the National Information Assurance Partnership (NIAP) in the Functional Package for Transport Layer Security. This compliance mode is opt-in only and provides additional options for regulated environments. To opt-in to this mode, use the [`NSRequiresNIAPTLSPackageVersion`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsrequiresniaptlspackageversion) key, which can be set to enforce this mode globally, and the [`NSExceptionRequiresNIAPTLSPackageVersion`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsexceptionrequiresniaptlspackageversion) key to configure exceptions to the global policy on a per-domain basis.

##### Configure Exceptions Only When Needed and Prefer Server Fixes

ATS disallows a connection if the server fails to meet one of the security checks discussed in the previous section. Your best response is to update the server. If you can’t do that for some reason, you can specify exceptions in your app to disable one or more aspects of ATS.

> ❗ **Important**:  It’s always better to fix the server when faced with an ATS failure. Exceptions reduce the security of your app. Some also require justification when submitting an app to the App Store, as described in the next section.

You configure ATS exceptions by providing a dictionary as the value for the optional [`NSAppTransportSecurity`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity) key in your app’s [`Information Property List`](https://developer.apple.com/documentation/bundleresources/information-property-list) file. The dictionary has the following structure, where all keys are optional:

```console
NSAppTransportSecurity : Dictionary {
    NSAllowsArbitraryLoads : Boolean
    NSAllowsArbitraryLoadsForMedia : Boolean
    NSAllowsArbitraryLoadsInWebContent : Boolean
    NSAllowsLocalNetworking : Boolean
    NSRequiresNIAPTLSPackageVersion : String
    NSExceptionDomains : Dictionary {
        <domain-name-string> : Dictionary {
            NSIncludesSubdomains : Boolean
            NSExceptionAllowsInsecureHTTPLoads : Boolean
            NSExceptionMinimumTLSVersion : String
            NSExceptionRequiresForwardSecrecy : Boolean
            NSRequiresCertificateTransparency : Boolean
            NSExceptionRequiresNIAPTLSPackageVersion : String
        }
    }
}
```

Keys at the first level of the [`NSAppTransportSecurity`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity) dictionary apply to connections made to any domain not specifically called out in the [`NSExceptionDomains`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsexceptiondomains) subdictionary. For example, by setting [`NSAllowsArbitraryLoads`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowsarbitraryloads) to `YES`, you completely disable ATS for all network connections when you add this to your app’s Info.plist:

![None](/images/com.apple.security/media-3138689@2x.png)

Depending on your use case, you can provide narrower exceptions. For example, by setting [`NSAllowsArbitraryLoadsInWebContent`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsinwebcontent) to `YES`, you can disable ATS restrictions on calls made from within web views, like instances of [`WKWebView`](https://developer.apple.com/documentation/webkit/wkwebview):

![None](/images/com.apple.security/media-3138691@2x.png)

You might only need to limit your ATS exception to a single domain. For example, if you need to access the insecure server `http://example.com`, you can still maintain all the benefits of ATS for other domains by setting the [`NSExceptionAllowsInsecureHTTPLoads`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsexceptionallowsinsecurehttploads) to `YES` in the domain-specific sub-dictionary:

![None](/images/com.apple.security/media-3138690@2x.png)

> **Note**:  Global exceptions don’t apply to any domains that you add to the [`NSExceptionDomains`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsexceptiondomains) dictionary. So you can invert the previous example—allowing insecure traffic on all domains *except* `example.com`—by placing [`NSAllowsArbitraryLoads`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowsarbitraryloads) at the top level, and including an empty `example.com` dictionary as an exception domain.

You can use the `nscurl` command line tool to connect to a server using different combinations of ATS exceptions. This helps you quickly narrow down the source of any ATS failures you have and figure out what exceptions you need. See [`Identifying the Source of Blocked Connections`](identifying-the-source-of-blocked-connections.md) for details.

##### Provide Justification for Exceptions

Adding certain ATS exceptions to your app’s [`Information Property List`](https://developer.apple.com/documentation/bundleresources/information-property-list) file requires you to provide justification, and might trigger additional App Store review for your app. Exceptions that require justification are:

- Arbitrary connection exceptions ([`NSAllowsArbitraryLoads`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowsarbitraryloads))
- Media streaming exceptions ([`NSAllowsArbitraryLoadsForMedia`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsformedia))
- Web content loads ([`NSAllowsArbitraryLoadsInWebContent`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsinwebcontent))
- Per-domain nonsecure connections ([`NSExceptionAllowsInsecureHTTPLoads`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsexceptionallowsinsecurehttploads))
- Per-domain minimum TLS version ([`NSExceptionMinimumTLSVersion`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsexceptionminimumtlsversion))

[`NSRequiresNIAPTLSPackageVersion`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsrequiresniaptlspackageversion) and [`NSExceptionRequiresNIAPTLSPackageVersion`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsexceptionrequiresniaptlspackageversion) don’t require justification because they strengthen rather than weaken security requirements.

Some examples of justifications eligible for consideration are:

- The app must connect to a server managed by another entity that doesn’t support secure connections.
- The app must support connecting to devices that cannot be upgraded to use secure connections, and that must be accessed using public host names.
- The app must display embedded web content from a variety of sources, but can’t use a class supported by the web content exception.
- The app loads media content that is encrypted and that contains no personalized information.

When submitting your app to the App Store, provide sufficient information for the App Store to determine why your app cannot make secure connections by default.

> ❗ **Important**:  Always look for a way to avoid using exceptions as a first recourse. If you must use an exception, make it as limited in scope as possible.

## Topics

### Evaluation
- [Identifying the Source of Blocked Connections](identifying-the-source-of-blocked-connections.md)
  Figure out why App Transport Security denies a network connection.
### Exceptions
- [NSAppTransportSecurity](../bundleresources/information-property-list/nsapptransportsecurity.md)
  A description of changes made to the default security for HTTP connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/preventing-insecure-network-connections)*