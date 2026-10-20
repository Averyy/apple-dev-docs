# isSecure

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isSecure) BOOL secure;
```

#### Discussion

This value is [`true`](../../Swift/true.md) if this cookie should only be sent over secure channels, otherwise [`false`](../../Swift/false.md).

## See Also

### Securing cookies
- [var isHTTPOnly: Bool](./ishttponly.md)
  A Boolean value that indicates whether the cookie should only be sent to HTTP servers.
- [var sameSitePolicy: HTTPCookieStringPolicy?](./samesitepolicy.md)
  A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.
- [struct HTTPCookieStringPolicy](../httpcookiestringpolicy.md)
  Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/issecure)*