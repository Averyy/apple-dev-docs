# httpShouldUsePipelining

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission.

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
var httpShouldUsePipelining: Bool { get }
```

```objc
@property (readonly) BOOL HTTPShouldUsePipelining;
```

## Discussion

[`true`](../../Swift/true.md) if the request should continue transmitting data; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var httpShouldUsePipelining: Bool](../nsmutableurlrequest/httpshouldusepipelining.md)
  A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.
### Controlling request behavior
- [var timeoutInterval: TimeInterval](./timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](./httpshouldhandlecookies.md)
  A Boolean value that indicates whether the default cookie handling will be used for this request.
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/httpshouldusepipelining)*