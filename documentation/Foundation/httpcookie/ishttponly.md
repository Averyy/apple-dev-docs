# isHTTPOnly

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the cookie should only be sent using HTTP headers, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

Cookies can be marked as HTTP-only by a server (or by JavaScript code). Cookies marked as such must only be sent via HTTP Headers in HTTP requests for URLs that match both the path and domain of the respective cookies.

> **Note**:  [`RFC 6265`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6265) formally defines the `HttpOnly` attribute.

> ❗ **Important**:  To prevent cross-site scripting vulnerabilities, don’t deliver cookies marked as HTTP-only to JavaScript code.

## See Also

- [var isSecure: Bool](httpcookie/issecure.md)
  A Boolean value that indicates whether the cookie may only be sent over secure channels.
- [var sameSitePolicy: HTTPCookieStringPolicy?](httpcookie/samesitepolicy.md)
  A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.
- [struct HTTPCookieStringPolicy](httpcookiestringpolicy.md)
  Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/ishttponly)*