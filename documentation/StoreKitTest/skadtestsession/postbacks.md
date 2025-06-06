# postbacks

**Framework**: StoreKit Test  
**Kind**: property

An array of test postbacks you set in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var postbacks: [SKAdTestPostback] { get }
```

#### Discussion

Use this property to check that your updates to the test postbacks, such as conversion value updates, are working as expected. See [`setPostbacks(_:)`](skadtestsession/setpostbacks(_:).md) for information on adding postbacks to the test session.

## See Also

- [func setPostbacks([SKAdTestPostback]) throws](skadtestsession/setpostbacks(_:).md)
  Add test postbacks to the test session.
- [func flushPostbacks(responses: SKANTestPostbackResponseHandler)](skadtestsession/flushpostbacks(responses:).md)
  Sends the test postbacks and handles the responses.
- [typealias SKANTestPostbackResponseHandler](skantestpostbackresponsehandler.md)
  A type that represents the test postback response handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession/postbacks)*