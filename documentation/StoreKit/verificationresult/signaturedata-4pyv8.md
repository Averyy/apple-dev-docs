# signatureData

**Framework**: StoreKit  
**Kind**: property

The signature component of the JWS transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var signatureData: Data { get }
```

## See Also

- [var jwsRepresentation: String](verificationresult/jwsrepresentation-21vgo.md)
  The transaction signed by the App Store, in JWS Compact Serialization format.
- [var deviceVerification: Data](verificationresult/deviceverification-69lvx.md)
  The device verification value to use to verify whether the transaction belongs to the device.
- [var deviceVerificationNonce: UUID](verificationresult/deviceverificationnonce-9dfrn.md)
  The UUID for computing the device verification value.
- [var signedDate: Date](verificationresult/signeddate-8x9bg.md)
  The date that the App Store signed the JWS transaction.
- [var headerData: Data](verificationresult/headerdata-9egfp.md)
  The header component of the JWS transaction.
- [var payloadData: Data](verificationresult/payloaddata-uyle.md)
  The payload component of the JWS transaction.
- [var signedData: Data](verificationresult/signeddata-56usp.md)
  The transaction data that the signature applies to.
- [var signature: P256.Signing.ECDSASignature](verificationresult/signature-7t1ne.md)
  The signature component of the JSON web signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/signaturedata-4pyv8)*