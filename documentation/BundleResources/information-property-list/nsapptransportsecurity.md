# NSAppTransportSecurity

**Framework**: Bundle Resources  
**Kind**: dictionary

A description of changes made to the default security for HTTP connections.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- visionOS 1.0+

#### Discussion

On Apple platforms, a networking feature called App Transport Security (ATS) improves privacy and data integrity for all apps and app extensions. ATS requires that all HTTP connections made with the [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system)—typically using the [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) class—use HTTPS. It further imposes extended security checks that supplement the default server trust evaluation prescribed by the Transport Layer Security (TLS) protocol. ATS blocks connections that fail to meet minimum security specifications. For additional details, see [`Preventing Insecure Network Connections`](https://developer.apple.com/documentation/Security/preventing-insecure-network-connections).

You can circumvent or augment these protections by adding the [`NSAppTransportSecurity`](information-property-list/nsapptransportsecurity.md) key to your app’s [`Information Property List`](information-property-list.md) file and providing an ATS configuration dictionary as the value. For example, you can:

- Allow insecure loads for web views while maintaining ATS protections elsewhere in your app using the [`NSAllowsArbitraryLoadsInWebContent`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsinwebcontent.md) key.
- Enable additional security features like Certificate Transparency using the [`NSRequiresCertificateTransparency`](information-property-list/nsrequirescertificatetransparency.md) key, or Certificate Pinning using the [`NSPinnedDomains`](information-property-list/nsapptransportsecurity/nspinneddomains.md) key.
- Reduce or remove security requirements for communication with particular servers using the [`NSExceptionDomains`](information-property-list/nsapptransportsecurity/nsexceptiondomains.md) key.

> ❗ **Important**:  Always look for ways to improve server security before adding ATS exceptions. Loosening ATS restrictions reduces the security of your app.

 Always look for ways to improve server security before adding ATS exceptions. Loosening ATS restrictions reduces the security of your app.

All keys in the ATS configuration dictionary are optional, with default values that are suitable for most apps. Keys that define global exceptions apply to all network connections made by your app, except connections to domains specified in the [`NSExceptionDomains`](information-property-list/nsapptransportsecurity/nsexceptiondomains.md) sub-dictionary. That sub-dictionary allows you to separately manage settings for individual domains.

##### Versioning

ATS operates by default for apps linked against the iOS 9.0 or macOS 10.11 SDKs or later. When you link your app against an older SDK, ATS is disabled no matter which version of operating system your app runs on.

If you specify a value for any of the global exceptions besides [`NSAllowsArbitraryLoads`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md), then the ATS behavior depends on the version of the OS on which your app runs:

This behavior enables you to manage differences between OS versions. You provide a coarse exception ([`NSAllowsArbitraryLoads`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md)) for older versions, and a more targeted exception, like [`NSAllowsArbitraryLoadsInWebContent`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsinwebcontent.md), for when it’s available.

## Topics

### Global Exceptions
- [NSAllowsArbitraryLoads](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md)
  A Boolean value indicating whether App Transport Security restrictions are disabled for all network connections.
- [NSAllowsArbitraryLoadsForMedia](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsformedia.md)
  A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made using the AV Foundation framework.
- [NSAllowsArbitraryLoadsInWebContent](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsinwebcontent.md)
  A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made from web views.
- [NSAllowsLocalNetworking](information-property-list/nsapptransportsecurity/nsallowslocalnetworking.md)
  A Boolean value that indicates whether to allow local resources to load.
### Domain-Specific Exceptions
- [NSExceptionDomains](information-property-list/nsapptransportsecurity/nsexceptiondomains.md)
  Custom App Transport Security (ATS) configurations for named domains.
### Certificate Pinning
- [NSPinnedDomains](information-property-list/nsapptransportsecurity/nspinneddomains.md)
  A collection of certificates that App Transport Security expects when connecting to named domains.

## See Also

- [Preventing Insecure Network Connections](../Security/preventing-insecure-network-connections.md)
  Enforce secure network links in your app by relying on App Transport Security.
- [NSAdvertisingAttributionReportEndpoint](information-property-list/nsadvertisingattributionreportendpoint.md)
  The URL where Private Click Measurement and SKAdNetwork send attribution information.
- [NSBonjourServices](information-property-list/nsbonjourservices.md)
  Bonjour service types browsed by the app.
- [CKSharingSupported](information-property-list/cksharingsupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity)*