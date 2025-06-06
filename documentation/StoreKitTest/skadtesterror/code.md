# SKAdTestError.Code

**Framework**: StoreKit Test  
**Kind**: enum

Enumerated error codes related to ad network testing in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
enum Code
```

## Topics

### Signature Errors
- [SKAdTestError.Code.missingSignature](skadtesterror/code/missingsignature.md)
  The signature for the ad is missing, in the testing environment.
- [SKAdTestError.Code.signatureInvalidKey](skadtesterror/code/signatureinvalidkey.md)
  The public key isn’t a valid cryptographic key, in the testing environment.
- [SKAdTestError.Code.signatureInvalidOrder](skadtesterror/code/signatureinvalidorder.md)
  The order of the parameters in the signature is invalid, in the testing environment.
- [SKAdTestError.Code.signatureMissingAdNetworkId](skadtesterror/code/signaturemissingadnetworkid.md)
  The signature is missing an ad network identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingAppAdamId](skadtesterror/code/signaturemissingappadamid.md)
  The signature is missing the app item identifier for the advertised app, in the testing environment.
- [SKAdTestError.Code.signatureMissingFidelityType](skadtesterror/code/signaturemissingfidelitytype.md)
  The signature is missing the fidelity type, in the testing environment.
- [SKAdTestError.Code.signatureMissingNonce](skadtesterror/code/signaturemissingnonce.md)
  The signature is missing the nonce, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceAppAdamId](skadtesterror/code/signaturemissingsourceappadamid.md)
  The signature is missing the source app item identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceDomain](skadtesterror/code/signaturemissingsourcedomain.md)
  The signature is missing the source domain, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceIdentifier](skadtesterror/code/signaturemissingsourceidentifier.md)
  The signature is missing the source identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingTimestamp](skadtesterror/code/signaturemissingtimestamp.md)
  The signature is missing a timestamp, in the testing environment.
- [SKAdTestError.Code.signatureUnknownError](skadtesterror/code/signatureunknownerror.md)
  An unknown error occurred with the signature in the testing environment.
- [SKAdTestError.Code.signatureVerificationFailed](skadtesterror/code/signatureverificationfailed.md)
  The signature verification failed in the testing environment.
- [SKAdTestError.Code.missingSignature](skadtesterror/code/missingsignature.md)
  The signature for the ad is missing, in the testing environment.
- [SKAdTestError.Code.signatureInvalidKey](skadtesterror/code/signatureinvalidkey.md)
  The public key isn’t a valid cryptographic key, in the testing environment.
- [SKAdTestError.Code.signatureInvalidOrder](skadtesterror/code/signatureinvalidorder.md)
  The order of the parameters in the signature is invalid, in the testing environment.
- [SKAdTestError.Code.signatureMissingAdNetworkId](skadtesterror/code/signaturemissingadnetworkid.md)
  The signature is missing an ad network identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingAppAdamId](skadtesterror/code/signaturemissingappadamid.md)
  The signature is missing the app item identifier for the advertised app, in the testing environment.
- [SKAdTestError.Code.signatureMissingFidelityType](skadtesterror/code/signaturemissingfidelitytype.md)
  The signature is missing the fidelity type, in the testing environment.
- [SKAdTestError.Code.signatureMissingNonce](skadtesterror/code/signaturemissingnonce.md)
  The signature is missing the nonce, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceAppAdamId](skadtesterror/code/signaturemissingsourceappadamid.md)
  The signature is missing the source app item identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceDomain](skadtesterror/code/signaturemissingsourcedomain.md)
  The signature is missing the source domain, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceIdentifier](skadtesterror/code/signaturemissingsourceidentifier.md)
  The signature is missing the source identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingTimestamp](skadtesterror/code/signaturemissingtimestamp.md)
  The signature is missing a timestamp, in the testing environment.
- [SKAdTestError.Code.signatureUnknownError](skadtesterror/code/signatureunknownerror.md)
  An unknown error occurred with the signature in the testing environment.
- [SKAdTestError.Code.signatureVerificationFailed](skadtesterror/code/signatureverificationfailed.md)
  The signature verification failed in the testing environment.
### Postback Errors
- [SKAdTestError.Code.excessivePostbacks](skadtesterror/code/excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [SKAdTestError.Code.invalidConversionValue](skadtesterror/code/invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidPostbackURL](skadtesterror/code/invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidRunnerUpPostback](skadtesterror/code/invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [SKAdTestError.Code.invalidWinningPostbackCount](skadtesterror/code/invalidwinningpostbackcount.md)
  The number of winning postbacks isn’t valid, in the testing environment.
- [SKAdTestError.Code.malformedPostbacks](skadtesterror/code/malformedpostbacks.md)
  The postback in the testing environment is malformed.
- [SKAdTestError.Code.missingPostbacks](skadtesterror/code/missingpostbacks.md)
  The testing environment doesn’t have any postbacks.
- [SKAdTestError.Code.misplacedWinnerPostback](skadtesterror/code/misplacedwinnerpostback.md)
  A winning postback wasn’t found in the first position, in the testing environment.
- [SKAdTestError.Code.missingWinningPostback](skadtesterror/code/missingwinningpostback.md)
  The testing environment is missing a winning postback.
- [SKAdTestError.Code.noPendingPostbacks](skadtesterror/code/nopendingpostbacks.md)
  The test session doesn’t have any pending postbacks to send.
- [SKAdTestError.Code.unlinkedWinningPostbacks](skadtesterror/code/unlinkedwinningpostbacks.md)
  The postbacks aren’t correctly related to one another.
- [SKAdTestError.Code.excessivePostbacks](skadtesterror/code/excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [SKAdTestError.Code.invalidConversionValue](skadtesterror/code/invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidPostbackURL](skadtesterror/code/invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidRunnerUpPostback](skadtesterror/code/invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [SKAdTestError.Code.invalidWinningPostbackCount](skadtesterror/code/invalidwinningpostbackcount.md)
  The number of winning postbacks isn’t valid, in the testing environment.
- [SKAdTestError.Code.malformedPostbacks](skadtesterror/code/malformedpostbacks.md)
  The postback in the testing environment is malformed.
- [SKAdTestError.Code.missingPostbacks](skadtesterror/code/missingpostbacks.md)
  The testing environment doesn’t have any postbacks.
- [SKAdTestError.Code.misplacedWinnerPostback](skadtesterror/code/misplacedwinnerpostback.md)
  A winning postback wasn’t found in the first position, in the testing environment.
- [SKAdTestError.Code.missingWinningPostback](skadtesterror/code/missingwinningpostback.md)
  The testing environment is missing a winning postback.
- [SKAdTestError.Code.noPendingPostbacks](skadtesterror/code/nopendingpostbacks.md)
  The test session doesn’t have any pending postbacks to send.
- [SKAdTestError.Code.unlinkedWinningPostbacks](skadtesterror/code/unlinkedwinningpostbacks.md)
  The postbacks aren’t correctly related to one another.
### Other Errors
- [SKAdTestError.Code.invalidVersion](skadtesterror/code/invalidversion.md)
  A postback contains an incorrect version number.
- [SKAdTestError.Code.invalidImpressionId](skadtesterror/code/invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [SKAdTestError.Code.invalidSourceAppAdamId](skadtesterror/code/invalidsourceappadamid.md)
  The app ID is less than zero.
- [SKAdTestError.Code.invalidSourceDomain](skadtesterror/code/invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [SKAdTestError.Code.invalidSourceIdentifier](skadtesterror/code/invalidsourceidentifier.md)
  The postback’s identifier isn’t two, three, or four digits.
- [SKAdTestError.Code.unknownError](skadtesterror/code/unknownerror.md)
  An unknown error occurred in the testing environment.
- [SKAdTestError.Code.invalidVersion](skadtesterror/code/invalidversion.md)
  A postback contains an incorrect version number.
- [SKAdTestError.Code.invalidImpressionId](skadtesterror/code/invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [SKAdTestError.Code.invalidSourceAppAdamId](skadtesterror/code/invalidsourceappadamid.md)
  The app ID is less than zero.
- [SKAdTestError.Code.invalidSourceDomain](skadtesterror/code/invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [SKAdTestError.Code.invalidSourceIdentifier](skadtesterror/code/invalidsourceidentifier.md)
  The postback’s identifier isn’t two, three, or four digits.
- [SKAdTestError.Code.unknownError](skadtesterror/code/unknownerror.md)
  An unknown error occurred in the testing environment.
### Older Errors
- [SKAdTestError.Code.invalidCampaignId](skadtesterror/code/invalidcampaignid.md)
  The campaign ID isn’t an integer between one and one hundred.
- [SKAdTestError.Code.signatureMissingCampaignId](skadtesterror/code/signaturemissingcampaignid.md)
  The signature is missing the campaign identifier, in the testing environment.
- [SKAdTestError.Code.conflictingSource](skadtesterror/code/conflictingsource.md)
  This error code is unused.
- [SKAdTestError.Code.invalidCampaignId](skadtesterror/code/invalidcampaignid.md)
  The campaign ID isn’t an integer between one and one hundred.
- [SKAdTestError.Code.signatureMissingCampaignId](skadtesterror/code/signaturemissingcampaignid.md)
  The signature is missing the campaign identifier, in the testing environment.
- [SKAdTestError.Code.conflictingSource](skadtesterror/code/conflictingsource.md)
  This error code is unused.
### Initializers
- [init?(rawValue: Int)](skadtesterror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code)*