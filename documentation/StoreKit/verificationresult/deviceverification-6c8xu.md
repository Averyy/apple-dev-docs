# deviceVerification

**Framework**: StoreKit  
**Kind**: property

The device verification value to use to verify whether the app transaction belongs to the device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var deviceVerification: Data { get }
```

#### Discussion

For more information about using the device verification value, see [`deviceVerification`](transaction/deviceverification.md).

This value is identical to the [`deviceVerification`](apptransaction/deviceverification.md) value in [`AppTransaction`](apptransaction.md).

## See Also

- [var jwsRepresentation: String](verificationresult/jwsrepresentation-6ma59.md)
  The app transaction signed by the App Store, in JWS Compact Serialization format.
- [var deviceVerificationNonce: UUID](verificationresult/deviceverificationnonce-6082b.md)
  The UUID for computing the device verification value.
- [var signedDate: Date](verificationresult/signeddate-24zch.md)
  The date that the App Store signed the JWS app transaction.
- [var headerData: Data](verificationresult/headerdata-3drrl.md)
  The header component of the JWS app transaction.
- [var payloadData: Data](verificationresult/payloaddata-97acz.md)
  The payload component of the JWS app transaction.
- [var signedData: Data](verificationresult/signeddata-99fyo.md)
  The app transaction data that the signature applies to.
- [var signatureData: Data](verificationresult/signaturedata-4pvv0.md)
  The signature component of the JWS app transaction.
- [var signature: P256.Signing.ECDSASignature](verificationresult/signature-6d5ue.md)
  The signature component of the JSON web signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/deviceverification-6c8xu)*