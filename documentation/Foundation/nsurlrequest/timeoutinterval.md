# timeoutInterval

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The request’s timeout interval, in seconds.

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
var timeoutInterval: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval timeoutInterval;
```

## Discussion

If during a connection attempt the request remains idle for longer than the timeout interval, the request is considered to have timed out.

## See Also

### Related Documentation
- [var timeoutInterval: TimeInterval](../nsmutableurlrequest/timeoutinterval.md)
  The request’s timeout interval, in seconds.
### Controlling request behavior
- [var httpShouldHandleCookies: Bool](./httpshouldhandlecookies.md)
  A Boolean value that indicates whether the default cookie handling will be used for this request.
- [var httpShouldUsePipelining: Bool](./httpshouldusepipelining.md)
  A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission.
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/timeoutinterval)*