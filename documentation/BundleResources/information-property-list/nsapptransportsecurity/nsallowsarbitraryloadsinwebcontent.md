# NSAllowsArbitraryLoadsInWebContent

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made from web views.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS 10.12+
- visionOS 1.0+

#### Discussion

Set this key’s value to `YES` to exempt your app’s [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) instances from App Transport Security restrictions without affecting your [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) connections. Domains you specify in the [`NSExceptionDomains`](information-property-list/nsapptransportsecurity/nsexceptiondomains.md) dictionary aren’t affected by this key’s value.

In iOS 10 and later and in macOS 10.12 and later, if you include this key with any value, then App Transport Security ignores the value of the [`NSAllowsArbitraryLoads`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md) key, instead using that key’s default value of `NO`. For more information about how the OS version affects ATS behavior, see the [`NSAppTransportSecurity`](information-property-list/nsapptransportsecurity.md) key’s Versioning section.

> ❗ **Important**:  You must supply a justification during App Store review if you set the key’s value to `YES`, as described in `Provide Justification for Exceptions`.

## See Also

- [NSAllowsArbitraryLoads](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md)
  A Boolean value indicating whether App Transport Security restrictions are disabled for all network connections.
- [NSAllowsArbitraryLoadsForMedia](information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsformedia.md)
  A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made using the AV Foundation framework.
- [NSAllowsLocalNetworking](information-property-list/nsapptransportsecurity/nsallowslocalnetworking.md)
  A Boolean value that indicates whether to allow local resources to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsinwebcontent)*