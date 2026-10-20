# postbacks

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

An array of test postbacks you set in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var postbacks: [SKAdTestPostback] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<SKAdTestPostback *> * postbacks;
```

#### Discussion

Use this property to check that your updates to the test postbacks, such as conversion value updates, are working as expected. See [`setPostbacks(_:)`](./setpostbacks%28_%29.md) for information on adding postbacks to the test session.

## See Also

### Adding and sending postbacks
- [func setPostbacks([SKAdTestPostback]) throws](./setpostbacks%28_%29.md)
  Add test postbacks to the test session.
- [func flushPostbacks(responses: ([String : SKAdTestPostbackResponse]?, (any Error)?) -> Void)](./flushpostbacks%28responses%29.md)
  Sends the test postbacks and handles the responses.
- [typealias SKANTestPostbackResponseHandler](../skantestpostbackresponsehandler.md)
  A type that represents the test postback response handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession/postbacks)*