# SKAdTestError.Code

**Framework**: StoreKit Test  
**Kind**: enum  
**Role**: Enumeration

Enumerated error codes related to ad network testing in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
enum Code
```

```c
enum SKAdTestErrorCode : NSInteger;
```

## Topics

### Signature Errors
- [SKAdTestError.Code.missingSignature](./code/missingsignature.md)
  The signature for the ad is missing, in the testing environment.
- [SKAdTestError.Code.signatureInvalidKey](./code/signatureinvalidkey.md)
  The public key isn’t a valid cryptographic key, in the testing environment.
- [SKAdTestError.Code.signatureInvalidOrder](./code/signatureinvalidorder.md)
  The order of the parameters in the signature is invalid, in the testing environment.
- [SKAdTestError.Code.signatureMissingAdNetworkId](./code/signaturemissingadnetworkid.md)
  The signature is missing an ad network identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingAppAdamId](./code/signaturemissingappadamid.md)
  The signature is missing the app item identifier for the advertised app, in the testing environment.
- [SKAdTestError.Code.signatureMissingFidelityType](./code/signaturemissingfidelitytype.md)
  The signature is missing the fidelity type, in the testing environment.
- [SKAdTestError.Code.signatureMissingNonce](./code/signaturemissingnonce.md)
  The signature is missing the nonce, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceAppAdamId](./code/signaturemissingsourceappadamid.md)
  The signature is missing the source app item identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceDomain](./code/signaturemissingsourcedomain.md)
  The signature is missing the source domain, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceIdentifier](./code/signaturemissingsourceidentifier.md)
  The signature is missing the source identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingTimestamp](./code/signaturemissingtimestamp.md)
  The signature is missing a timestamp, in the testing environment.
- [SKAdTestError.Code.signatureUnknownError](./code/signatureunknownerror.md)
  An unknown error occurred with the signature in the testing environment.
- [SKAdTestError.Code.signatureVerificationFailed](./code/signatureverificationfailed.md)
  The signature verification failed in the testing environment.
- [SKAdTestError.Code.missingSignature](./code/missingsignature.md)
  The signature for the ad is missing, in the testing environment.
- [SKAdTestError.Code.signatureInvalidKey](./code/signatureinvalidkey.md)
  The public key isn’t a valid cryptographic key, in the testing environment.
- [SKAdTestError.Code.signatureInvalidOrder](./code/signatureinvalidorder.md)
  The order of the parameters in the signature is invalid, in the testing environment.
- [SKAdTestError.Code.signatureMissingAdNetworkId](./code/signaturemissingadnetworkid.md)
  The signature is missing an ad network identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingAppAdamId](./code/signaturemissingappadamid.md)
  The signature is missing the app item identifier for the advertised app, in the testing environment.
- [SKAdTestError.Code.signatureMissingFidelityType](./code/signaturemissingfidelitytype.md)
  The signature is missing the fidelity type, in the testing environment.
- [SKAdTestError.Code.signatureMissingNonce](./code/signaturemissingnonce.md)
  The signature is missing the nonce, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceAppAdamId](./code/signaturemissingsourceappadamid.md)
  The signature is missing the source app item identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceDomain](./code/signaturemissingsourcedomain.md)
  The signature is missing the source domain, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceIdentifier](./code/signaturemissingsourceidentifier.md)
  The signature is missing the source identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingTimestamp](./code/signaturemissingtimestamp.md)
  The signature is missing a timestamp, in the testing environment.
- [SKAdTestError.Code.signatureUnknownError](./code/signatureunknownerror.md)
  An unknown error occurred with the signature in the testing environment.
- [SKAdTestError.Code.signatureVerificationFailed](./code/signatureverificationfailed.md)
  The signature verification failed in the testing environment.
### Postback Errors
- [SKAdTestError.Code.excessivePostbacks](./code/excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [SKAdTestError.Code.invalidConversionValue](./code/invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidPostbackURL](./code/invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidRunnerUpPostback](./code/invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [SKAdTestError.Code.invalidWinningPostbackCount](./code/invalidwinningpostbackcount.md)
  The number of winning postbacks isn’t valid, in the testing environment.
- [SKAdTestError.Code.malformedPostbacks](./code/malformedpostbacks.md)
  The postback in the testing environment is malformed.
- [SKAdTestError.Code.missingPostbacks](./code/missingpostbacks.md)
  The testing environment doesn’t have any postbacks.
- [SKAdTestError.Code.misplacedWinnerPostback](./code/misplacedwinnerpostback.md)
  A winning postback wasn’t found in the first position, in the testing environment.
- [SKAdTestError.Code.missingWinningPostback](./code/missingwinningpostback.md)
  The testing environment is missing a winning postback.
- [SKAdTestError.Code.noPendingPostbacks](./code/nopendingpostbacks.md)
  The test session doesn’t have any pending postbacks to send.
- [SKAdTestError.Code.unlinkedWinningPostbacks](./code/unlinkedwinningpostbacks.md)
  The postbacks aren’t correctly related to one another.
- [SKAdTestError.Code.excessivePostbacks](./code/excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [SKAdTestError.Code.invalidConversionValue](./code/invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidPostbackURL](./code/invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidRunnerUpPostback](./code/invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [SKAdTestError.Code.invalidWinningPostbackCount](./code/invalidwinningpostbackcount.md)
  The number of winning postbacks isn’t valid, in the testing environment.
- [SKAdTestError.Code.malformedPostbacks](./code/malformedpostbacks.md)
  The postback in the testing environment is malformed.
- [SKAdTestError.Code.missingPostbacks](./code/missingpostbacks.md)
  The testing environment doesn’t have any postbacks.
- [SKAdTestError.Code.misplacedWinnerPostback](./code/misplacedwinnerpostback.md)
  A winning postback wasn’t found in the first position, in the testing environment.
- [SKAdTestError.Code.missingWinningPostback](./code/missingwinningpostback.md)
  The testing environment is missing a winning postback.
- [SKAdTestError.Code.noPendingPostbacks](./code/nopendingpostbacks.md)
  The test session doesn’t have any pending postbacks to send.
- [SKAdTestError.Code.unlinkedWinningPostbacks](./code/unlinkedwinningpostbacks.md)
  The postbacks aren’t correctly related to one another.
### Other Errors
- [SKAdTestError.Code.invalidVersion](./code/invalidversion.md)
  A postback contains an incorrect version number.
- [SKAdTestError.Code.invalidImpressionId](./code/invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [SKAdTestError.Code.invalidSourceAppAdamId](./code/invalidsourceappadamid.md)
  The app ID is less than zero.
- [SKAdTestError.Code.invalidSourceDomain](./code/invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [SKAdTestError.Code.invalidSourceIdentifier](./code/invalidsourceidentifier.md)
  The postback’s identifier isn’t two, three, or four digits.
- [SKAdTestError.Code.unknownError](./code/unknownerror.md)
  An unknown error occurred in the testing environment.
- [SKAdTestError.Code.invalidVersion](./code/invalidversion.md)
  A postback contains an incorrect version number.
- [SKAdTestError.Code.invalidImpressionId](./code/invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [SKAdTestError.Code.invalidSourceAppAdamId](./code/invalidsourceappadamid.md)
  The app ID is less than zero.
- [SKAdTestError.Code.invalidSourceDomain](./code/invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [SKAdTestError.Code.invalidSourceIdentifier](./code/invalidsourceidentifier.md)
  The postback’s identifier isn’t two, three, or four digits.
- [SKAdTestError.Code.unknownError](./code/unknownerror.md)
  An unknown error occurred in the testing environment.
### Older Errors
- [SKAdTestError.Code.invalidCampaignId](./code/invalidcampaignid.md)
  The campaign ID isn’t an integer between one and one hundred.
- [SKAdTestError.Code.signatureMissingCampaignId](./code/signaturemissingcampaignid.md)
  The signature is missing the campaign identifier, in the testing environment.
- [SKAdTestError.Code.conflictingSource](./code/conflictingsource.md)
  This error code is unused.
- [SKAdTestError.Code.invalidCampaignId](./code/invalidcampaignid.md)
  The campaign ID isn’t an integer between one and one hundred.
- [SKAdTestError.Code.signatureMissingCampaignId](./code/signaturemissingcampaignid.md)
  The signature is missing the campaign identifier, in the testing environment.
- [SKAdTestError.Code.conflictingSource](./code/conflictingsource.md)
  This error code is unused.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code)*