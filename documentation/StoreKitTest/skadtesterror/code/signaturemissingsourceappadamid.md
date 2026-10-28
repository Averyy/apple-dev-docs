# SKAdTestError.Code.signatureMissingSourceAppAdamId

**Framework**: StoreKit Test  
**Kind**: case  
**Role**: Case

The signature is missing the source app item identifier, in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
case signatureMissingSourceAppAdamId
```

```c
SKAdTestErrorCodeSignatureMissingSourceAppAdamId
```

## Discussion

Be sure to include the app item identifier for the source app when you create and validate an ad impression in the testing environment.

## See Also

### Signature Errors
- [SKAdTestError.Code.missingSignature](./missingsignature.md)
  The signature for the ad is missing, in the testing environment.
- [SKAdTestError.Code.signatureInvalidKey](./signatureinvalidkey.md)
  The public key isn’t a valid cryptographic key, in the testing environment.
- [SKAdTestError.Code.signatureInvalidOrder](./signatureinvalidorder.md)
  The order of the parameters in the signature is invalid, in the testing environment.
- [SKAdTestError.Code.signatureMissingAdNetworkId](./signaturemissingadnetworkid.md)
  The signature is missing an ad network identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingAppAdamId](./signaturemissingappadamid.md)
  The signature is missing the app item identifier for the advertised app, in the testing environment.
- [SKAdTestError.Code.signatureMissingFidelityType](./signaturemissingfidelitytype.md)
  The signature is missing the fidelity type, in the testing environment.
- [SKAdTestError.Code.signatureMissingNonce](./signaturemissingnonce.md)
  The signature is missing the nonce, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceDomain](./signaturemissingsourcedomain.md)
  The signature is missing the source domain, in the testing environment.
- [SKAdTestError.Code.signatureMissingSourceIdentifier](./signaturemissingsourceidentifier.md)
  The signature is missing the source identifier, in the testing environment.
- [SKAdTestError.Code.signatureMissingTimestamp](./signaturemissingtimestamp.md)
  The signature is missing a timestamp, in the testing environment.
- [SKAdTestError.Code.signatureUnknownError](./signatureunknownerror.md)
  An unknown error occurred with the signature in the testing environment.
- [SKAdTestError.Code.signatureVerificationFailed](./signatureverificationfailed.md)
  The signature verification failed in the testing environment.
- [SKAdTestError.Code.missingSignature](./missingsignature.md)
  The signature for the ad is missing, in the testing environment.
- [SKAdTestError.Code.signatureInvalidKey](./signatureinvalidkey.md)
  The public key isn’t a valid cryptographic key, in the testing environment.
- [SKAdTestError.Code.signatureInvalidOrder](./signatureinvalidorder.md)
  The order of the parameters in the signature is invalid, in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/signaturemissingsourceappadamid)*