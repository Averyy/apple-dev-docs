# httpShouldUsePipelining

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission.

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
var httpShouldUsePipelining: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the request should continue transmitting data; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var httpShouldUsePipelining: Bool](nsmutableurlrequest/httpshouldusepipelining.md)
  A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.
- [var timeoutInterval: TimeInterval](nsurlrequest/timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](nsurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the default cookie handling will be used for this request.
- [var allowsCellularAccess: Bool](nsurlrequest/allowscellularaccess.md)
  A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/httpshouldusepipelining)*