# sameSitePolicy

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var sameSitePolicy: HTTPCookieStringPolicy? { get }
```

#### Discussion

Along with the policy values defined by [`HTTPCookieStringPolicy`](httpcookiestringpolicy.md), this property may also be `nil`. In this case, cross-site requests include the cookie.

## See Also

- [var isHTTPOnly: Bool](httpcookie/ishttponly.md)
  A Boolean value that indicates whether the cookie should only be sent to HTTP servers.
- [var isSecure: Bool](httpcookie/issecure.md)
  A Boolean value that indicates whether the cookie may only be sent over secure channels.
- [struct HTTPCookieStringPolicy](httpcookiestringpolicy.md)
  Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/samesitepolicy)*