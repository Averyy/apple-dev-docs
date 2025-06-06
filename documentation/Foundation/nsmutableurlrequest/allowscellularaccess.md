# allowsCellularAccess

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether a connection can use the device’s cellular network (if present).

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var allowsCellularAccess: Bool { get set }
```

#### Discussion

Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) (the default) makes the request eligible to run over cellular, subject to other considerations (including, but not limited to, the [`allowsCellularAccess`](urlsessionconfiguration/allowscellularaccess.md) property of the [`URLSessionConfiguration`](urlsessionconfiguration.md)). Setting this value to [`false`](https://developer.apple.com/documentation/swift/false) ensures that the request will never run over cellular.

## See Also

- [var waitsForConnectivity: Bool](urlsessionconfiguration/waitsforconnectivity.md)
  A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.
- [var timeoutInterval: TimeInterval](nsmutableurlrequest/timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](nsmutableurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [var httpShouldUsePipelining: Bool](nsmutableurlrequest/httpshouldusepipelining.md)
  A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/allowscellularaccess)*