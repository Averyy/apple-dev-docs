# allowsCellularAccess

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL allowsCellularAccess;
```

#### Discussion

Setting this property to [`true`](../../Swift/true.md) (the default) makes the request eligible to run over cellular, subject to other considerations (including, but not limited to, the [`allowsCellularAccess`](../urlsessionconfiguration/allowscellularaccess.md) property of the [`URLSessionConfiguration`](../urlsessionconfiguration.md)). Setting this value to [`false`](../../Swift/false.md) ensures that the request will never run over cellular.

## See Also

### Related Documentation
- [var waitsForConnectivity: Bool](../urlsessionconfiguration/waitsforconnectivity.md)
  A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.
### Controlling request behavior
- [var timeoutInterval: TimeInterval](./timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](./httpshouldhandlecookies.md)
  A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [var httpShouldUsePipelining: Bool](./httpshouldusepipelining.md)
  A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/allowscellularaccess)*