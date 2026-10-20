# httpShouldUsePipelining

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.

**Availability**:
- iOS 4.0+ - Deprecated in 18.4
- iPadOS 4.0+ - Deprecated in 18.4
- Mac Catalyst 13.1+ - Deprecated in 18.4
- macOS 10.7+ - Deprecated in 15.4
- tvOS 9.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 2.4
- watchOS 2.0+ - Deprecated in 11.4

> **Deprecated**: Pipelining is an HTTP/1.1 concept. Adopt HTTP/2 or later instead.

## Declaration

```swift
var httpShouldUsePipelining: Bool { get set }
```

```objc
@property BOOL HTTPShouldUsePipelining;
```

#### Discussion

[`true`](../../Swift/true.md) if the request should continue transmitting data, [`false`](../../Swift/false.md) if the request should wait for a response. The default value is [`false`](../../Swift/false.md).

Setting this property to [`true`](../../Swift/true.md) value does not guarantee HTTP pipelining behavior. This may have no effect if an HTTP proxy is configured, or if the HTTP request uses an unsafe request method—for example, POST requests will not pipeline. Pipelining behavior may not begin until the second request on a given TCP connection. There may be other situations where pipelining does not occur even though this property is set to [`true`](../../Swift/true.md). HTTP/1.1 allows the client to send multiple requests to the server without waiting for a response. Though HTTP/1.1 requires support for pipelining, some servers report themselves as being HTTP/1.1 but do not support pipelining (disconnecting, sending resources in the wrong order, omitting part of a resource, etc.).

HTTP/2 and later ignore this property. HTTP/1.1 only considers this property in the classic loading mode (`usesClassicLoadingMode`).

## See Also

### Controlling request behavior
- [var timeoutInterval: TimeInterval](./timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](./httpshouldhandlecookies.md)
  A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value that indicates whether a connection can use the device’s cellular network (if present).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpshouldusepipelining)*