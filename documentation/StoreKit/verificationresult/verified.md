# VerificationResult.verified(_:)

**Framework**: StoreKit  
**Kind**: case

The associated value passed StoreKit automatic verification checks.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case verified(SignedType)
```

## Mentions

- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md)
- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)

#### Discussion

The associated value in this case is the App Store-signed value.

## See Also

- [case unverified(SignedType, VerificationResult<SignedType>.VerificationError)](verificationresult/unverified(_:_:).md)
  The associated value failed StoreKit automatic verification checks.
- [var payloadValue: SignedType](verificationresult/payloadvalue.md)
  The verified value of the signed type that StoreKit confirms as verified.
- [var unsafePayloadValue: SignedType](verificationresult/unsafepayloadvalue.md)
  The associated value of the verification result that StoreKit doesn’t confirm as verified.
- [VerificationResult.VerificationError](verificationresult/verificationerror.md)
  Error cases for StoreKit JWS verification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/verified(_:))*