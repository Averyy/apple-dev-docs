# SKAdTestError

**Framework**: StoreKit Test  
**Kind**: struct

An error the testing environment returns for SKAdNetwork testing errors.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
struct SKAdTestError
```

#### Overview

Unit tests that call [`setPostbacks(_:)`](skadtestsession/setpostbacks(_:).md), [`flushPostbacks(responses:)`](skadtestsession/flushpostbacks(responses:).md), [`validateImpression(parameters:publicKey:)`](skadtestsession/validateimpression(parameters:publickey:).md), and [`validate(_:publicKey:)`](skadtestsession/validate(_:publickey:).md), can throw [`SKAdTestError`](skadtesterror.md) errors.

When you call the unit test methods [`validateImpression(parameters:publicKey:)`](skadtestsession/validateimpression(parameters:publickey:).md), [`validate(_:publicKey:)`](skadtestsession/validate(_:publickey:).md), or [`validateWebAdImpressionPayload(_:publicKey:)`](skadtestsession/validatewebadimpressionpayload(_:publickey:).md) to validate your ad impression, the system may return signature-related errors.

When you call [`setPostbacks(_:)`](skadtestsession/setpostbacks(_:).md) and [`flushPostbacks(responses:)`](skadtestsession/flushpostbacks(responses:).md), you may get postback-related errors.

## Topics

### Getting Signature Errors
- [static var missingSignature: SKAdTestError.Code](skadtesterror/missingsignature.md)
  The signature for the ad is missing, in the testing environment.
- [static var signatureInvalidKey: SKAdTestError.Code](skadtesterror/signatureinvalidkey.md)
  The public key isn’t a valid cryptographic key, in the testing environment.
- [static var signatureInvalidOrder: SKAdTestError.Code](skadtesterror/signatureinvalidorder.md)
  The order of the parameters in the signature is invalid, in the testing environment.
- [static var signatureMissingAdNetworkId: SKAdTestError.Code](skadtesterror/signaturemissingadnetworkid.md)
  The signature is missing an ad network identifier, in the testing environment.
- [static var signatureMissingAppAdamId: SKAdTestError.Code](skadtesterror/signaturemissingappadamid.md)
  The signature is missing the app item identifier for the advertised app, in the testing environment.
- [static var signatureMissingFidelityType: SKAdTestError.Code](skadtesterror/signaturemissingfidelitytype.md)
  The signature is missing the fidelity type, in the testing environment.
- [static var signatureMissingNonce: SKAdTestError.Code](skadtesterror/signaturemissingnonce.md)
  The signature is missing the nonce, in the testing environment.
- [static var signatureMissingSourceAppAdamId: SKAdTestError.Code](skadtesterror/signaturemissingsourceappadamid.md)
  The signature is missing the source app item identifier, in the testing environment.
- [static var signatureMissingSourceDomain: SKAdTestError.Code](skadtesterror/signaturemissingsourcedomain.md)
  The signature is missing the source domain, in the testing environment.
- [static var signatureMissingSourceIdentifier: SKAdTestError.Code](skadtesterror/signaturemissingsourceidentifier.md)
  The signature is missing the source identifier, in the testing environment.
- [static var signatureMissingTimestamp: SKAdTestError.Code](skadtesterror/signaturemissingtimestamp.md)
  The signature is missing a timestamp, in the testing environment.
- [static var signatureUnknownError: SKAdTestError.Code](skadtesterror/signatureunknownerror.md)
  An unknown error occurred with the signature in the testing environment.
- [static var signatureVerificationFailed: SKAdTestError.Code](skadtesterror/signatureverificationfailed.md)
  The signature verification failed in the testing environment.
### Getting Postback Errors
- [static var excessivePostbacks: SKAdTestError.Code](skadtesterror/excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [static var invalidConversionValue: SKAdTestError.Code](skadtesterror/invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [static var invalidPostbackURL: SKAdTestError.Code](skadtesterror/invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [static var invalidRunnerUpPostback: SKAdTestError.Code](skadtesterror/invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [static var invalidWinningPostbackCount: SKAdTestError.Code](skadtesterror/invalidwinningpostbackcount.md)
  The number of winning postbacks isn’t valid, in the testing environment.
- [static var malformedPostbacks: SKAdTestError.Code](skadtesterror/malformedpostbacks.md)
  The postback in the testing environment is malformed.
- [static var missingPostbacks: SKAdTestError.Code](skadtesterror/missingpostbacks.md)
  The testing environment doesn’t have any postbacks.
- [static var misplacedWinnerPostback: SKAdTestError.Code](skadtesterror/misplacedwinnerpostback.md)
  A winning postback wasn’t found in the first position, in the testing environment.
- [static var missingWinningPostback: SKAdTestError.Code](skadtesterror/missingwinningpostback.md)
  The testing environment is missing a winning postback.
- [static var noPendingPostbacks: SKAdTestError.Code](skadtesterror/nopendingpostbacks.md)
  The test session doesn’t have any pending postbacks to send.
- [static var unlinkedWinningPostbacks: SKAdTestError.Code](skadtesterror/unlinkedwinningpostbacks.md)
  The postbacks aren’t correctly related to one another.
### Getting Other Errors
- [static var invalidVersion: SKAdTestError.Code](skadtesterror/invalidversion.md)
  A postback contains an incorrect version number.
- [static var invalidImpressionId: SKAdTestError.Code](skadtesterror/invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [static var invalidSourceAppAdamId: SKAdTestError.Code](skadtesterror/invalidsourceappadamid.md)
  The app ID is less than zero.
- [static var invalidSourceDomain: SKAdTestError.Code](skadtesterror/invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [static var invalidSourceIdentifier: SKAdTestError.Code](skadtesterror/invalidsourceidentifier.md)
  The postback’s identifier isn’t two, three, or four digits.
- [static var unknownError: SKAdTestError.Code](skadtesterror/unknownerror.md)
  An unknown error occurred in the testing environment.
### Getting Older Errors
- [static var invalidCampaignId: SKAdTestError.Code](skadtesterror/invalidcampaignid.md)
  The campaign ID isn’t an integer between one and one hundred.
- [static var signatureMissingCampaignId: SKAdTestError.Code](skadtesterror/signaturemissingcampaignid.md)
  The signature is missing the campaign identifier, in the testing environment.
- [static var conflictingSource: SKAdTestError.Code](skadtesterror/conflictingsource.md)
  This error code is unused.
### Initializing the Error Objects
- [SKAdTestError.Code](skadtesterror/code.md)
  Enumerated error codes related to ad network testing in the testing environment.
### Type Properties
- [static var errorDomain: String](skadtesterror/errordomain.md)
  The domain of the error.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let SKAdTestErrorDomain: String](skadtesterrordomain.md)
  A string that identifies the error domain for SKAdNetwork testing in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror)*