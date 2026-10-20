# VerificationResult.unverified(_:_:)

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

The associated value failed StoreKit automatic verification checks.

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
case unverified(SignedType, VerificationResult<SignedType>.VerificationError)
```

#### Discussion

The first associated value in this case is the App Store-signed value. The second associated value provides the reason why the verification failed.

## See Also

### Getting the verification results
- [VerificationResult.verified(_:)](./verified%28_%29.md)
  The associated value passed StoreKit automatic verification checks.
- [var payloadValue: SignedType](./payloadvalue.md)
  The verified value of the signed type that StoreKit confirms as verified.
- [var unsafePayloadValue: SignedType](./unsafepayloadvalue.md)
  The associated value of the verification result that StoreKit doesn’t confirm as verified.
- [VerificationResult.VerificationError](./verificationerror.md)
  Error cases for StoreKit JWS verification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/unverified(_:_:))*