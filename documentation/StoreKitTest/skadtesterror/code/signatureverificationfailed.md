# SKAdTestError.Code.signatureVerificationFailed

**Framework**: StoreKit Test  
**Kind**: case

The signature verification failed in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
case signatureVerificationFailed
```

#### Discussion

The ad impression signature isn’t valid. Check the following:

- You use the same cryptographic key-pair when you sign the ad impression and validate it in the testing environment. If you use different key pairs in these two steps, signature verification will fail. For more information about signing the ad, see [`Signing and providing ads`](https://developer.apple.com/documentation/StoreKit/signing-and-providing-ads). For more information about validating the ad impression in the testing environment, see [`validate(_:publicKey:)`](skadtestsession/validate(_:publickey:).md) and [`validateImpression(parameters:publicKey:)`](skadtestsession/validateimpression(parameters:publickey:).md).
- You use the correct signature instructions for the SKAdNetwork version that your app uses.For more information about SKAdNetwork versions, see [`SKAdNetwork release notes`](https://developer.apple.com/documentation/StoreKit/skadnetwork-release-notes).
- Your signature contains all the parameters in the correct order for the version you’re using.
- Your signature uses the correct separator character.

For more information about signatures, see [`Signing and providing ads`](https://developer.apple.com/documentation/StoreKit/signing-and-providing-ads).

## See Also

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
- [SKAdTestError.Code.missingSignature](skadtesterror/code/missingsignature.md)
  The signature for the ad is missing, in the testing environment.
- [SKAdTestError.Code.signatureInvalidKey](skadtesterror/code/signatureinvalidkey.md)
  The public key isn’t a valid cryptographic key, in the testing environment.
- [SKAdTestError.Code.signatureInvalidOrder](skadtesterror/code/signatureinvalidorder.md)
  The order of the parameters in the signature is invalid, in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/signatureverificationfailed)*