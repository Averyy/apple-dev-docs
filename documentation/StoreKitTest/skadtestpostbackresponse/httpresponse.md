# httpResponse

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The HTTP response from the server receiving the test postback.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var httpResponse: HTTPURLResponse? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSHTTPURLResponse * httpResponse;
```

#### Discussion

This property contains your server’s full HTTP response.

## See Also

### Getting Postback Responses
- [var didSucceed: Bool](./didsucceed.md)
  A Boolean value that indicates whether the system successfully delivered the test postback.
- [var error: (any Error)?](./error.md)
  An error the test session reports if sending a test postbacks fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostbackresponse/httpresponse)*