# signatureVerificationFailed

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Type Property

The signature verification failed in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
static var signatureVerificationFailed: SKAdTestError.Code { get }
```

## Discussion

The ad impression signature isn’t valid. Check the following:

- You use the same cryptographic key-pair when you sign the ad impression and validate it in the testing environment. If you use different key pairs in these two steps, signature verification will fail. For more information about signing the ad, see [Signing and providing ads](../../StoreKit/signing-and-providing-ads.md). For more information about validating the ad impression in the testing environment, see [`validate(_:publicKey:)`](../skadtestsession/validate%28_,publickey%29.md) and [`validateImpression(parameters:publicKey:)`](../skadtestsession/validateimpression%28parameters,publickey%29.md).
- You use the correct signature instructions for the SKAdNetwork version that your app uses. For more information about SKAdNetwork versions, see [SKAdNetwork release notes](../../StoreKit/skadnetwork-release-notes.md).
- Your signature contains all the parameters in the correct order for the version you’re using.
- Your signature uses the correct separator character.

For more information about signatures, see [Signing and providing ads](../../StoreKit/signing-and-providing-ads.md).

## See Also

### Getting Signature Errors
- [static var missingSignature: SKAdTestError.Code](./missingsignature.md)
  The signature for the ad is missing, in the testing environment.
- [static var signatureInvalidKey: SKAdTestError.Code](./signatureinvalidkey.md)
  The public key isn’t a valid cryptographic key, in the testing environment.
- [static var signatureInvalidOrder: SKAdTestError.Code](./signatureinvalidorder.md)
  The order of the parameters in the signature is invalid, in the testing environment.
- [static var signatureMissingAdNetworkId: SKAdTestError.Code](./signaturemissingadnetworkid.md)
  The signature is missing an ad network identifier, in the testing environment.
- [static var signatureMissingAppAdamId: SKAdTestError.Code](./signaturemissingappadamid.md)
  The signature is missing the app item identifier for the advertised app, in the testing environment.
- [static var signatureMissingFidelityType: SKAdTestError.Code](./signaturemissingfidelitytype.md)
  The signature is missing the fidelity type, in the testing environment.
- [static var signatureMissingNonce: SKAdTestError.Code](./signaturemissingnonce.md)
  The signature is missing the nonce, in the testing environment.
- [static var signatureMissingSourceAppAdamId: SKAdTestError.Code](./signaturemissingsourceappadamid.md)
  The signature is missing the source app item identifier, in the testing environment.
- [static var signatureMissingSourceDomain: SKAdTestError.Code](./signaturemissingsourcedomain.md)
  The signature is missing the source domain, in the testing environment.
- [static var signatureMissingSourceIdentifier: SKAdTestError.Code](./signaturemissingsourceidentifier.md)
  The signature is missing the source identifier, in the testing environment.
- [static var signatureMissingTimestamp: SKAdTestError.Code](./signaturemissingtimestamp.md)
  The signature is missing a timestamp, in the testing environment.
- [static var signatureUnknownError: SKAdTestError.Code](./signatureunknownerror.md)
  An unknown error occurred with the signature in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/signatureverificationfailed)*