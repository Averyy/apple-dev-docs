# payloadValue

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The verified value of the signed type that StoreKit confirms as verified.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var payloadValue: SignedType { get throws }
```

#### Discussion

This property represents the value of a payload in a JSON Web Signature (JWS) value that passed StoreKit verification.

This property throws an error if the JWS value containing the payload doesn’t pass StoreKit’s verification and is therefore *unverified*. To access the payload of an unverified JWS value, get the associated value of the verification result, or use the [`unsafePayloadValue`](./unsafepayloadvalue.md) property.

## See Also

### Getting the verification results
- [VerificationResult.verified(_:)](./verified%28_%29.md)
  The associated value passed StoreKit automatic verification checks.
- [case unverified(SignedType, VerificationResult<SignedType>.VerificationError)](./unverified%28_,_%29.md)
  The associated value failed StoreKit automatic verification checks.
- [var unsafePayloadValue: SignedType](./unsafepayloadvalue.md)
  The associated value of the verification result that StoreKit doesn’t confirm as verified.
- [VerificationResult.VerificationError](./verificationerror.md)
  Error cases for StoreKit JWS verification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/payloadvalue)*