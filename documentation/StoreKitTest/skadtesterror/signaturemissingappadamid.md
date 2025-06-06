# signatureMissingAppAdamId

**Framework**: StoreKit Test  
**Kind**: property

The signature is missing the app item identifier for the advertised app, in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
static var signatureMissingAppAdamId: SKAdTestError.Code { get }
```

#### Discussion

Be sure to include the app item identifier for the advertised app when you create and validate an ad impression in the testing environment.

## See Also

- [static var missingSignature: SKAdTestError.Code](skadtesterror/missingsignature.md)
  The signature for the ad is missing, in the testing environment.
- [static var signatureInvalidKey: SKAdTestError.Code](skadtesterror/signatureinvalidkey.md)
  The public key isn’t a valid cryptographic key, in the testing environment.
- [static var signatureInvalidOrder: SKAdTestError.Code](skadtesterror/signatureinvalidorder.md)
  The order of the parameters in the signature is invalid, in the testing environment.
- [static var signatureMissingAdNetworkId: SKAdTestError.Code](skadtesterror/signaturemissingadnetworkid.md)
  The signature is missing an ad network identifier, in the testing environment.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/signaturemissingappadamid)*