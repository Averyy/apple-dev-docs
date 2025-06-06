# NSAllowsArbitraryLoads

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether App Transport Security restrictions are disabled for all network connections.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- visionOS 1.0+

#### Discussion

Set this key’s value to `YES` to disable App Transport Security (ATS) restrictions for all domains not specified in the [`NSExceptionDomains`](information-property-list/nsapptransportsecurity/nsexceptiondomains.md) dictionary. Domains you specify in that dictionary aren’t affected by this key’s value.

> ❗ **Important**:  You must supply a justification during App Store review if you set the key’s value to `YES`, as described in `Provide Justification for Exceptions`. Use this key with caution because it significantly reduces the security of your app. In most cases, it’s better to upgrade your servers to meet the requirements imposed by ATS, or at least to use a narrower exception.

 You must supply a justification during App Store review if you set the key’s value to `YES`, as described in `Provide Justification for Exceptions`. Use this key with caution because it significantly reduces the security of your app. In most cases, it’s better to upgrade your servers to meet the requirements imposed by ATS, or at least to use a narrower exception.

Disabling ATS means that unsecured HTTP connections are allowed. HTTPS connections are also allowed, and are still subject to default server trust evaluation, as described in `Ensure the Network Server Meets Minimum Requirements`. However, extended security checks—like requiring a minimum Transport Layer Security (TLS) protocol version—are disabled. Without ATS, you’re also free to loosen the default server trust requirements, as described in [`Performing manual server trust authentication`](https://developer.apple.com/documentation/Foundation/performing-manual-server-trust-authentication).

In iOS 10 and later and macOS 10.12 and later, the value of the [`NSAllowsArbitraryLoads`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md) key is ignored—and the default value of `NO` used instead—if any of the following keys are present in your app’s [`Information Property List`](information-property-list.md) file:

- [`NSAllowsArbitraryLoadsForMedia`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsformedia.md)
- [`NSAllowsArbitraryLoadsInWebContent`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsinwebcontent.md)
- [`NSAllowsLocalNetworking`](information-property-list/nsapptransportsecurity/nsallowslocalnetworking.md)

For more information about how the OS version affects ATS behavior, see the [`NSAppTransportSecurity`](information-property-list/nsapptransportsecurity.md) key’s Versioning section.

## See Also

- [NSAllowsArbitraryLoadsForMedia](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsformedia.md)
  A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made using the AV Foundation framework.
- [NSAllowsArbitraryLoadsInWebContent](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsinwebcontent.md)
  A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made from web views.
- [NSAllowsLocalNetworking](information-property-list/nsapptransportsecurity/nsallowslocalnetworking.md)
  A Boolean value that indicates whether to allow local resources to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowsarbitraryloads)*