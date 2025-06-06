# didSucceed

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that indicates whether the system successfully delivered the test postback.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var didSucceed: Bool { get set }
```

#### Discussion

The value is `true` if the system successfully delivered the test postback and received an HTTP 200 response.

## See Also

- [var httpResponse: HTTPURLResponse?](skadtestpostbackresponse/httpresponse.md)
  The HTTP response from the server receiving the test postback.
- [var error: (any Error)?](skadtestpostbackresponse/error.md)
  An error the test session reports if sending a test postbacks fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostbackresponse/didsucceed)*