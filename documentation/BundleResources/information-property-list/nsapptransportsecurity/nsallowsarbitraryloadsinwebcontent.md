# NSAllowsArbitraryLoadsInWebContent

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made from web views.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS 10.12+
- visionOS 1.0+

## Details

- **Name**: `NSAllowsArbitraryLoadsInWebContent` (Allow Arbitrary Loads in Web Content)
- **Type**: boolean



**Default**: `NO`

#### Discussion

Set this key’s value to `YES` to exempt your app’s [`WKWebView`](../../../WebKit/wkwebview.md) instances from App Transport Security restrictions without affecting your [`URLSession`](../../../Foundation/urlsession.md) connections. Domains you specify in the [`NSExceptionDomains`](./nsexceptiondomains.md) dictionary aren’t affected by this key’s value.

In iOS 10 and later and in macOS 10.12 and later, if you include this key with any value, then App Transport Security ignores the value of the [`NSAllowsArbitraryLoads`](./nsallowsarbitraryloads.md) key, instead using that key’s default value of `NO`. For more information about how the OS version affects ATS behavior, see the [`NSAppTransportSecurity`](../nsapptransportsecurity.md) key’s Versioning section.

> ❗ **Important**:  You must supply a justification during App Store review if you set the key’s value to `YES`, as described in `Provide Justification for Exceptions`.

## See Also

### Global Exceptions
- [NSAllowsArbitraryLoads](./nsallowsarbitraryloads.md)
  A Boolean value indicating whether App Transport Security restrictions are disabled for all network connections.
- [NSAllowsArbitraryLoadsForMedia](./nsallowsarbitraryloadsformedia.md)
  A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made using the AV Foundation framework.
- [NSAllowsLocalNetworking](./nsallowslocalnetworking.md)
  A Boolean value that indicates whether to allow local resources to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowsarbitraryloadsinwebcontent)*