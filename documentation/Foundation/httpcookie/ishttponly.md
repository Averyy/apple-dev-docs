# isHTTPOnly

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the cookie should only be sent to HTTP servers.

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
var isHTTPOnly: Bool { get }
```

```objc
@property (readonly, getter=isHTTPOnly) BOOL HTTPOnly;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the cookie should only be sent using HTTP headers, [`false`](../../Swift/false.md) otherwise.

Cookies can be marked as HTTP-only by a server (or by JavaScript code). Cookies marked as such must only be sent via HTTP Headers in HTTP requests for URLs that match both the path and domain of the respective cookies.

> **Note**:  [RFC 6265](https://tools.ietf.org/html/rfc6265) formally defines the `HttpOnly` attribute.

> ❗ **Important**:  To prevent cross-site scripting vulnerabilities, don’t deliver cookies marked as HTTP-only to JavaScript code.

## See Also

### Securing cookies
- [var isSecure: Bool](./issecure.md)
  A Boolean value that indicates whether the cookie may only be sent over secure channels.
- [var sameSitePolicy: HTTPCookieStringPolicy?](./samesitepolicy.md)
  A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.
- [struct HTTPCookieStringPolicy](../httpcookiestringpolicy.md)
  Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/ishttponly)*