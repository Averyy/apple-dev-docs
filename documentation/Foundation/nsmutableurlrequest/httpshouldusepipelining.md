# httpShouldUsePipelining

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var httpShouldUsePipelining: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the request should continue transmitting data, [`false`](https://developer.apple.com/documentation/Swift/false) if the request should wait for a response. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

Setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) value does not guarantee HTTP pipelining behavior. This may have no effect if an HTTP proxy is configured, or if the HTTP request uses an unsafe request method—for example, POST requests will not pipeline. Pipelining behavior may not begin until the second request on a given TCP connection. There may be other situations where pipelining does not occur even though this property is set to [`true`](https://developer.apple.com/documentation/Swift/true). HTTP 1.1 allows the client to send multiple requests to the server without waiting for a response. Though HTTP 1.1 requires support for pipelining, some servers report themselves as being HTTP 1.1 but do not support pipelining (disconnecting, sending resources in the wrong order, omitting part of a resource, etc.).

## See Also

- [var timeoutInterval: TimeInterval](nsmutableurlrequest/timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](nsmutableurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [var allowsCellularAccess: Bool](nsmutableurlrequest/allowscellularaccess.md)
  A Boolean value that indicates whether a connection can use the device’s cellular network (if present).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpshouldusepipelining)*