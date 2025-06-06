# SKANTestPostbackResponseHandler

**Framework**: StoreKit Test  
**Kind**: typealias

A type that represents the test postback response handler.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
typealias SKANTestPostbackResponseHandler = ([String : SKAdTestPostbackResponse]?, (any Error)?) -> Void
```

#### Discussion

The system calls the response handler and provides one of two values:

- A dictionary with a key that identifies a test postback using its [`transactionIdentifier`](skadtestpostback/transactionidentifier.md) value, and the associated value of the response, [`SKAdTestPostbackResponse`](skadtestpostbackresponse.md) that you receive when calling [`flushPostbacks(responses:)`](skadtestsession/flushpostbacks(responses:).md)
- An [`SKAdTestError`](skadtesterror.md) error

## See Also

- [func setPostbacks([SKAdTestPostback]) throws](skadtestsession/setpostbacks(_:).md)
  Add test postbacks to the test session.
- [var postbacks: [SKAdTestPostback]](skadtestsession/postbacks.md)
  An array of test postbacks you set in the testing environment.
- [func flushPostbacks(responses: SKANTestPostbackResponseHandler)](skadtestsession/flushpostbacks(responses:).md)
  Sends the test postbacks and handles the responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skantestpostbackresponsehandler)*