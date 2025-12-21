# httpShouldHandleCookies

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the default cookie handling will be used for this request.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var httpShouldHandleCookies: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the default cookie handling will be used for this request, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise. The default is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var httpShouldHandleCookies: Bool](nsmutableurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [var timeoutInterval: TimeInterval](nsurlrequest/timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldUsePipelining: Bool](nsurlrequest/httpshouldusepipelining.md)
  A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission.
- [var allowsCellularAccess: Bool](nsurlrequest/allowscellularaccess.md)
  A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/httpshouldhandlecookies)*