# didSucceed

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system successfully delivered the test postback.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var didSucceed: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL didSucceed;
```

#### Discussion

The value is `true` if the system successfully delivered the test postback and received an HTTP 200 response.

## See Also

### Getting Postback Responses
- [var httpResponse: HTTPURLResponse?](./httpresponse.md)
  The HTTP response from the server receiving the test postback.
- [var error: (any Error)?](./error.md)
  An error the test session reports if sending a test postbacks fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostbackresponse/didsucceed)*