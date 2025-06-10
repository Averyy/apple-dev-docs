# HTTPCookieStringPolicy

**Framework**: Foundation  
**Kind**: struct

Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct HTTPCookieStringPolicy
```

#### Discussion

[`RFC 6265`](https://developer.apple.comhttps://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site-00) defines “same site” as the registerable domain of a URI.

## Topics

### Creating a policy
- [init(rawValue: String)](httpcookiestringpolicy/init(rawvalue:).md)
  Creates an HTTP cookie string policy from the given raw string.
### Policies
- [static let sameSiteStrict: HTTPCookieStringPolicy](httpcookiestringpolicy/samesitestrict.md)
  A policy that prohibits a cross-site request from including the cookie.
- [static let sameSiteLax: HTTPCookieStringPolicy](httpcookiestringpolicy/samesitelax.md)
  A policy that allows certain cross-site requests to include the cookie.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isHTTPOnly: Bool](httpcookie/ishttponly.md)
  A Boolean value that indicates whether the cookie should only be sent to HTTP servers.
- [var isSecure: Bool](httpcookie/issecure.md)
  A Boolean value that indicates whether the cookie may only be sent over secure channels.
- [var sameSitePolicy: HTTPCookieStringPolicy?](httpcookie/samesitepolicy.md)
  A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestringpolicy)*