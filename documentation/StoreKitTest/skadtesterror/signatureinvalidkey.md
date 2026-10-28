# signatureInvalidKey

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Type Property

The public key isn’t a valid cryptographic key, in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
static var signatureInvalidKey: SKAdTestError.Code { get }
```

## Discussion

The public key that you provide in the [`validate(_:publicKey:)`](../skadtestsession/validate%28_,publickey%29.md) or [`validateImpression(parameters:publicKey:)`](../skadtestsession/validateimpression%28parameters,publickey%29.md) methods must be a key that uses Elliptic Curve Digital Signature Algorithm (ECDSA) with a prime256v1 curve. For more information about the key, see [Registering an ad network](../../StoreKit/registering-an-ad-network.md).

## See Also

### Getting Signature Errors
- [static var missingSignature: SKAdTestError.Code](./missingsignature.md)
  The signature for the ad is missing, in the testing environment.
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
- [static var signatureVerificationFailed: SKAdTestError.Code](./signatureverificationfailed.md)
  The signature verification failed in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/signatureinvalidkey)*