# allowsCellularAccess

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).

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
var allowsCellularAccess: Bool { get }
```

```objc
@property (readonly) BOOL allowsCellularAccess;
```

#### Discussion

[`true`](../../Swift/true.md) if the cellular radio can be used; [`false`](../../Swift/false.md) otherwise.

## See Also

### Related Documentation
- [var allowsCellularAccess: Bool](../nsmutableurlrequest/allowscellularaccess.md)
  A Boolean value that indicates whether a connection can use the device’s cellular network (if present).
### Controlling request behavior
- [var timeoutInterval: TimeInterval](./timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](./httpshouldhandlecookies.md)
  A Boolean value that indicates whether the default cookie handling will be used for this request.
- [var httpShouldUsePipelining: Bool](./httpshouldusepipelining.md)
  A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/allowscellularaccess)*