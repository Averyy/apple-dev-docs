# deviceVerificationNonce

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The UUID for computing the device verification value.

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
var deviceVerificationNonce: UUID { get }
```

Available when `SignedType` is `Transaction`.

#### Discussion

Use the lowercased nonce when computing the [`deviceVerification`](./deviceverification-69lvx.md) value.

This value is identical to the [`deviceVerificationNonce`](../transaction/deviceverificationnonce.md) value in [`Transaction`](../transaction.md).

## See Also

### Getting properties for transactions
- [var jwsRepresentation: String](./jwsrepresentation-21vgo.md)
  The transaction signed by the App Store, in JWS Compact Serialization format.
- [var deviceVerification: Data](./deviceverification-69lvx.md)
  The device verification value to use to verify whether the transaction belongs to the device.
- [var signedDate: Date](./signeddate-8x9bg.md)
  The date that the App Store signed the JWS transaction.
- [var headerData: Data](./headerdata-9egfp.md)
  The header component of the JWS transaction.
- [var payloadData: Data](./payloaddata-uyle.md)
  The payload component of the JWS transaction.
- [var signedData: Data](./signeddata-56usp.md)
  The transaction data that the signature applies to.
- [var signatureData: Data](./signaturedata-4pyv8.md)
  The signature component of the JWS transaction.
- [var signature: P256.Signing.ECDSASignature](./signature-7t1ne.md)
  The signature component of the JSON web signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/deviceverificationnonce-9dfrn)*