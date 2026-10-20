# flushPostbacks(responses:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

Sends the test postbacks and handles the responses.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
func flushPostbacks(responses: @escaping @Sendable ([String : SKAdTestPostbackResponse]?, (any Error)?) -> Void)
```

```swift
func flushPostbacksWithResponses() async throws -> [String : SKAdTestPostbackResponse]
```

```objc
- (void) flushPostbacksWithResponses:(SKANTestPostbackResponseHandler) responses;
```

#### Discussion

This method sends the test postbacks that you set up using [`setPostbacks(_:)`](./setpostbacks%28_%29.md) to the server URL provided in each postback, and then deletes them from this test session. Note that you set up the postback server URL when you create the postback instance using [`SKAdTestPostback`](../skadtestpostback.md).

This method calls the response handler with either a dictionary that contains postback [`transactionIdentifier`](../skadtestpostback/transactionidentifier.md) keys with their responses ([`SKAdTestPostbackResponse`](../skadtestpostbackresponse.md)), or a single [`SKAdTestError`](../skadtesterror.md) error. If you receive an error, it indicates a failure that isn’t specific to any single postback, but is a general issue; for example, a test session has no postbacks, there’s a connectivity issue, or the postbacks aren’t registered.

To perform tests with postbacks, do the following:

1. Create a test postback using [`SKAdTestPostback`](../skadtestpostback.md).
2. Add the test postbacks to the test session by calling [`setPostbacks(_:)`](./setpostbacks%28_%29.md).
3. In the code representing the advertised app, register the test postback by calling [`updatePostbackConversionValue(_:completionHandler:)`](../../StoreKit/skadnetwork/updatepostbackconversionvalue%28_,completionhandler%29.md)or [`registerAppForAdNetworkAttribution()`](../../StoreKit/skadnetwork/registerappforadnetworkattribution%28%29.md).
4. Optionally, update the conversion value by calling [`updatePostbackConversionValue(_:completionHandler:)`](../../StoreKit/skadnetwork/updatepostbackconversionvalue%28_,completionhandler%29.md).
5. Call [`flushPostbacks(responses:)`](./flushpostbacks%28responses%29.md) when you’re done updating the conversion value and are ready to test receiving postbacks on your server.

## Parameters

- `responses`: A handler that matches the signature of [`SKANTestPostbackResponseHandler`](../skantestpostbackresponsehandler.md).

## See Also

### Adding and sending postbacks
- [func setPostbacks([SKAdTestPostback]) throws](./setpostbacks%28_%29.md)
  Add test postbacks to the test session.
- [var postbacks: [SKAdTestPostback]](./postbacks.md)
  An array of test postbacks you set in the testing environment.
- [typealias SKANTestPostbackResponseHandler](../skantestpostbackresponsehandler.md)
  A type that represents the test postback response handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession/flushpostbacks(responses:))*