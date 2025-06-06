# timeoutInterval

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

If during a connection attempt the request remains idle for longer than the timeout interval, the request is considered to have timed out.

## See Also

- [var timeoutInterval: TimeInterval](nsmutableurlrequest/timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](nsurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the default cookie handling will be used for this request.
- [var httpShouldUsePipelining: Bool](nsurlrequest/httpshouldusepipelining.md)
  A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission.
- [var allowsCellularAccess: Bool](nsurlrequest/allowscellularaccess.md)
  A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/timeoutinterval)*