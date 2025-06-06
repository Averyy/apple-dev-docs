# NSAllowsLocalNetworking

**Framework**: Bundleresources  
**Kind**: typealias

A Boolean value that indicates whether to allow local resources to load.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS 10.12+
- visionOS 1.0+

#### Discussion

The `NSAllowsLocalNetworking` key controls whether App Transport Security (ATS) allows your app to connect to unqualified domains, `.local` domains, and IP addresses using IPv4 or IPv6.

In iOS 9 and macOS 10.11, ATS disallows connections to all three domain types. You can add exceptions for unqualified domains and `.local` domains in the [`NSExceptionDomains`](information-property-list/nsapptransportsecurity/nsexceptiondomains.md) dictionary, but you can’t add IP addresses. Instead you use [`NSAllowsArbitraryLoads`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md) when you want to load directly from an IP address.

In iOS 10 through iOS 16, iPadOS 13.1 through iPadOS 16, and macOS 10.12 through macOS 13, ATS allows all three of these connections by default, so you no longer need an exception for any of them. However, if you need to maintain compatibility with older versions of the OS, set both of the [`NSAllowsArbitraryLoads`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md) and [`NSAllowsLocalNetworking`](information-property-list/nsapptransportsecurity/nsallowslocalnetworking.md) keys to `YES`.

In iOS 17, iPadOS 17, and macOS 14, ATS no longer allows connections to IP addresses by default. Add individual IP addresses and classless inter-domain routing (CIDR) ranges in the [`NSExceptionDomains`](information-property-list/nsapptransportsecurity/nsexceptiondomains.md) dictionary.

The local networking exception tells newer versions of the OS to ignore the arbitrary loads key, and enable access to unqualified domains, `.local` domains, and IP addresses that they would otherwise restrict. Meanwhile, the arbitrary loads key tells older versions of the OS, which don’t process the local networking exception key, to bypass ATS completely. This allows your app to work on different OS versions while minimizing the use of the wider exception. For more information about how global ATS exceptions interact across OS versions, see the [`NSAppTransportSecurity`](information-property-list/nsapptransportsecurity.md) key’s Versioning section.

> **Note**:  While ATS doesn’t block local loads by default in newer versions of the OS, consider setting [`NSAllowsLocalNetworking`](information-property-list/nsapptransportsecurity/nsallowslocalnetworking.md) to `YES` as a declaration of intent, if appropriate, even if you don’t support older OS versions.

## See Also

- [NSAllowsArbitraryLoads](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md)
  A Boolean value indicating whether App Transport Security restrictions are disabled for all network connections.
- [NSAllowsArbitraryLoadsForMedia](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsformedia.md)
  A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made using the AV Foundation framework.
- [NSAllowsArbitraryLoadsInWebContent](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsinwebcontent.md)
  A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made from web views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowslocalnetworking)*