# SKAdTestPostbackResponse

**Framework**: StoreKit Test  
**Kind**: class

The status and error information for a postback that the system sends in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
class SKAdTestPostbackResponse
```

## Topics

### Getting Postback Responses
- [var didSucceed: Bool](skadtestpostbackresponse/didsucceed.md)
  A Boolean value that indicates whether the system successfully delivered the test postback.
- [var httpResponse: HTTPURLResponse?](skadtestpostbackresponse/httpresponse.md)
  The HTTP response from the server receiving the test postback.
- [var error: (any Error)?](skadtestpostbackresponse/error.md)
  An error the test session reports if sending a test postbacks fails.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Testing and validating ad impression signatures and postbacks for SKAdNetwork](testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
  Validate your ad impressions and test your postbacks by creating unit tests using the StoreKit Test framework.
- [class SKAdTestSession](skadtestsession.md)
  The class you use to test ad impressions and postbacks in Xcode.
- [class SKAdTestPostback](skadtestpostback.md)
  A test postback that contains ad conversion information in the testing environment.
- [struct SKAdTestPostbackVersion](skadtestpostbackversion.md)
  A constant that indicates the postback version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostbackresponse)*