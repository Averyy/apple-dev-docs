# allowsCellularAccess

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the cellular radio can be used; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## See Also

- [var allowsCellularAccess: Bool](nsmutableurlrequest/allowscellularaccess.md)
  A Boolean value that indicates whether a connection can use the device’s cellular network (if present).
- [var timeoutInterval: TimeInterval](nsurlrequest/timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](nsurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the default cookie handling will be used for this request.
- [var httpShouldUsePipelining: Bool](nsurlrequest/httpshouldusepipelining.md)
  A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/allowscellularaccess)*