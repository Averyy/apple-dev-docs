# unsafePayloadValue

**Framework**: StoreKit  
**Kind**: property

The associated value of the verification result that StoreKit doesn’t confirm as verified.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var unsafePayloadValue: SignedType { get }
```

#### Discussion

This property represents the value of a payload in a JSON Web Signature (JWS) value that’s not confirmed to have passed StoreKit verification.

Use the [`unsafePayloadValue`](verificationresult/unsafepayloadvalue.md) for debugging purposes or other situations where the integrity of the data is unimportant. This property ignores any verification errors. To get a payload that passed verification, or to check for verification errors, use the [`payloadValue`](verificationresult/payloadvalue.md) property instead.

> ❗ **Important**:  Don’t trust the integrity of the values you receive from the [`unsafePayloadValue`](verificationresult/unsafepayloadvalue.md) property. This property contains data regardless of the verification result, and contains data even if StoreKit’s verification fails.

To determine if the JWS value fails verification, perform a verification on the [`jwsRepresentation`](verificationresult/jwsrepresentation-178oj.md) property for subscription renewal information, the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) property for transactions, or the [`jwsRepresentation`](verificationresult/jwsrepresentation-6ma59.md) property for app transactions.

## See Also

- [VerificationResult.verified(_:)](verificationresult/verified(_:).md)
  The associated value passed StoreKit automatic verification checks.
- [case unverified(SignedType, VerificationResult<SignedType>.VerificationError)](verificationresult/unverified(_:_:).md)
  The associated value failed StoreKit automatic verification checks.
- [var payloadValue: SignedType](verificationresult/payloadvalue.md)
  The verified value of the signed type that StoreKit confirms as verified.
- [VerificationResult.VerificationError](verificationresult/verificationerror.md)
  Error cases for StoreKit JWS verification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/unsafepayloadvalue)*