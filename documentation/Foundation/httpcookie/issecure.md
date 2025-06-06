# isSecure

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the cookie may only be sent over secure channels.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isSecure: Bool { get }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/swift/true) if this cookie should only be sent over secure channels, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isHTTPOnly: Bool](httpcookie/ishttponly.md)
  A Boolean value that indicates whether the cookie should only be sent to HTTP servers.
- [var sameSitePolicy: HTTPCookieStringPolicy?](httpcookie/samesitepolicy.md)
  A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.
- [struct HTTPCookieStringPolicy](httpcookiestringpolicy.md)
  Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/issecure)*