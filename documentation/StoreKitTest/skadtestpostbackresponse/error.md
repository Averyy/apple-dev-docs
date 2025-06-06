# error

**Framework**: StoreKit Test  
**Kind**: property

An error the test session reports if sending a test postbacks fails.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var error: (any Error)? { get set }
```

#### Discussion

If the test session encounters an error when attempting to send the test postback with [`flushPostbacks(responses:)`](skadtestsession/flushpostbacks(responses:).md), this property contains an [`SKAdTestError`](skadtesterror.md) error.

## See Also

- [var didSucceed: Bool](skadtestpostbackresponse/didsucceed.md)
  A Boolean value that indicates whether the system successfully delivered the test postback.
- [var httpResponse: HTTPURLResponse?](skadtestpostbackresponse/httpresponse.md)
  The HTTP response from the server receiving the test postback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostbackresponse/error)*