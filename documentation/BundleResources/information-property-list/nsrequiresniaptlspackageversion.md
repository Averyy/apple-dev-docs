# NSRequiresNIAPTLSPackageVersion

**Framework**: Bundle Resources  
**Kind**: typealias

A string that indicates the version to use for the NIAP Functional Package for TLS.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+



**Type**: string

#### Discussion

App Transport Security (ATS) allows you to further restrict default TLS client behavior to help meet requirements outlined by the United States government’s National Information Assurance Partnership (NIAP) Functional Package for Transport Layer Security. This compliance mode is opt-in only and provides additional options to help developers create NIAP-compliant modes of operations for their apps.

The value of this key is a string, which can have the following values:

- **`none`**: Apply no additional requirements. This value results in the default ATS behavior.
- **`FCP_v2.1`**: Make your default client connections enforce additional requirements (described below) as specified in the [`Functional Package for Transport Layer Security (TLS) Version 2.1`](https://developer.apple.comhttps://www.niap-ccevs.org/static_html/protection-profile/519/PKG_TLS_V2.1.html).
- **`recommended`**: Use the recommended version of the NIAP functional package for the operating system version your app is running on. Currently, this is equivalent to `FCP_v2.1`.

The `FCP_v2.1` value adds the following requirements on top of standard ATS:

- The client offers the same TLS 1.3 ciphersuites as the default ATS policy. For TLS 1.2, the client offers only perfect forward secret (using ECDHE), AES-GCM ciphersuites with a SHA-256 or greater pseudorandom function (PRF).
- The client no longer offers the signature algorithm `rsa_pkcs15_sha1`, as specified in [`FCS_TLSC_EXT.1.4`](https://developer.apple.comhttps://www.niap-ccevs.org/static_html/protection-profile/519/PKG_TLS_V2.1.html#FCS_TLSC_EXT.1.4).
- The server’s certificate signature  must use a signature algorithm offered in the client hello, as defined in [`RFC 8446 Section 4.2.3`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc8446#section-4.2.3) and [`RFC 5246 Section 7.4.2`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc5246#section-7.4.2).
- TLS 1.2 connections must negotiate the Extended Master Secret extension, as specified in [`RFC 7627`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7627).

Use this key to opt in to the compliance behavior globally, as shown in the following example.

```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSRequiresNIAPTLSPackageVersion</key>
    <string>FCP_v2.1</string>
</dict>
```

You can use the [`NSExceptionRequiresNIAPTLSPackageVersion`](information-property-list/nsexceptionrequiresniaptlspackageversion.md) key within the [`NSExceptionDomains`](information-property-list/nsapptransportsecurity/nsexceptiondomains.md) dictionary to carve out behavior exceptions for specific domains.

## See Also

- [NSExceptionRequiresNIAPTLSPackageVersion](information-property-list/nsexceptionrequiresniaptlspackageversion.md)
  A string that indicates the version to use for the NIAP Functional Package for TLS, applied to an exception domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsrequiresniaptlspackageversion)*