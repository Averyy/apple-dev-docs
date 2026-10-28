# SKAdTestSession

**Framework**: StoreKit Test  
**Kind**: class  
**Role**: Class

The class you use to test ad impressions and postbacks in Xcode.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
class SKAdTestSession
```

```objc
@interface SKAdTestSession : NSObject
```

## Overview

Use the `SKAdTestSession` class to test your implementations of SKAdNetwork. Create one instance of this class to use in multiple test cases. The instance represents a test session, and holds a set of test postbacks. Use [`SKAdTestPostback`](./skadtestpostback.md) to create test postbacks. Call [`setPostbacks(_:)`](./skadtestsession/setpostbacks%28_%29.md) to add test postbacks to the test session. The test session deletes the postbacks from the instance after you call [`flushPostbacks(responses:)`](./skadtestsession/flushpostbacks%28responses%29.md).

> **Note**:  Check [`SKAdTestPostbackVersion`](./skadtestpostbackversion.md) for the list of SKAdNetwork versions that the testing environment supports.

### Validate ad impressions

In the production environment, ad networks sign the ad impressions that apps display. In the testing environment, you have the opportunity to validate the ad impression signature. Ad networks provide two types of ads: StoreKit-rendered ads and view-through ads. To validate the ad impressions, use the following methods:

- [`validate(_:publicKey:)`](./skadtestsession/validate%28_,publickey%29.md) to test your signature for view-through ads
- [`validateImpression(parameters:publicKey:)`](./skadtestsession/validateimpression%28parameters,publickey%29.md) to test your signature for StoreKit-rendered ads
- [`validateWebAdImpressionPayload(_:publicKey:)`](./skadtestsession/validatewebadimpressionpayload%28_,publickey%29.md) to test your signature for web ads

You need a cryptographic private key to generate signatures. Use a public/private key pair that you create using an Elliptic Curve Digital Signature Algorithm (ECDSA) with a prime256V1 curve. Provide the public key in the validation methods. Secure your private keys as you would other credentials, such as passwords. Never share your private keys, store keys in a code repository, or include keys in client-facing code.

### Test conversion values and postbacks

In the production environment, ad networks receive postbacks on their server after users install an advertised app and a timer expires. In the testing environment, you can control all aspects of the postback, including when it’s sent.

In the production environment, an advertised app may update a conversion value as the user interacts with the app. The final conversion value appears in the winning postback. In the testing environment, you have the opportunity to check the test postback before it’s sent to determine whether your app is updating conversion values as expected.

To perform tests on conversion values and postbacks, follow these steps:

1. Create up to six test postbacks using [`SKAdTestPostback`](./skadtestpostback.md).
2. Add the test postbacks to the test session by calling [`setPostbacks(_:)`](./skadtestsession/setpostbacks%28_%29.md).
3. In the code representing the advertised app, register the test postbacks by calling [`updatePostbackConversionValue(_:completionHandler:)`](../StoreKit/skadnetwork/updatepostbackconversionvalue%28_,completionhandler%29.md)or [`registerAppForAdNetworkAttribution()`](../StoreKit/skadnetwork/registerappforadnetworkattribution%28%29.md).
4. To test conversion values, call [`updatePostbackConversionValue(_:completionHandler:)`](../StoreKit/skadnetwork/updatepostbackconversionvalue%28_,completionhandler%29.md) to update the conversion value of the winning test postback.
5. Call [`flushPostbacks(responses:)`](./skadtestsession/flushpostbacks%28responses%29.md) when you’re done updating the conversion value and are ready to test receiving postbacks on your server. This method sends the test postbacks to your server, and removes them from the test session.

## Topics

### Validating impressions
- [func validate(SKAdImpression, publicKey: String) throws](./skadtestsession/validate%28_,publickey%29.md)
  Validates an impression for a view-through ad.
- [func validateImpression(parameters: [String : Any], publicKey: String) throws](./skadtestsession/validateimpression%28parameters,publickey%29.md)
  Validates an impression for a StoreKit-rendered ad.
- [func validateWebAdImpressionPayload(Data, publicKey: String) throws](./skadtestsession/validatewebadimpressionpayload%28_,publickey%29.md)
  Validates an impression for a web ad.
### Adding and sending postbacks
- [func setPostbacks([SKAdTestPostback]) throws](./skadtestsession/setpostbacks%28_%29.md)
  Add test postbacks to the test session.
- [var postbacks: [SKAdTestPostback]](./skadtestsession/postbacks.md)
  An array of test postbacks you set in the testing environment.
- [func flushPostbacks(responses: ([String : SKAdTestPostbackResponse]?, (any Error)?) -> Void)](./skadtestsession/flushpostbacks%28responses%29.md)
  Sends the test postbacks and handles the responses.
- [typealias SKANTestPostbackResponseHandler](./skantestpostbackresponsehandler.md)
  A type that represents the test postback response handler.
### Viewing the developer postback URL
- [var developerPostbackURL: URL?](./skadtestsession/developerpostbackurl.md)
  The URL that SKAdNetwork computes to send copies of winning postbacks to the advertised app’s developer.
### Initializing test sessions
- [init()](./skadtestsession/init%28%29.md)
  Initializes an SKAdNetwork test session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Ad impression and postback testing
- [Testing and validating ad impression signatures and postbacks for SKAdNetwork](./testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
  Validate your ad impressions and test your postbacks by creating unit tests using the StoreKit Test framework.
- [class SKAdTestPostback](./skadtestpostback.md)
  A test postback that contains ad conversion information in the testing environment.
- [class SKAdTestPostbackResponse](./skadtestpostbackresponse.md)
  The status and error information for a postback that the system sends in the testing environment.
- [struct SKAdTestPostbackVersion](./skadtestpostbackversion.md)
  A constant that indicates the postback version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession)*