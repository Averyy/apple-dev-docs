# payloadData

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The payload component of the JWS app transaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var payloadData: Data { get }
```

Available when `SignedType` is `AppTransaction`.

#### Discussion

This value is the same as the [`jsonRepresentation`](../apptransaction/jsonrepresentation.md) in [`AppTransaction`](../apptransaction.md).

## See Also

### Getting properties for app transactions
- [var jwsRepresentation: String](./jwsrepresentation-6ma59.md)
  The app transaction signed by the App Store, in JWS Compact Serialization format.
- [var deviceVerification: Data](./deviceverification-6c8xu.md)
  The device verification value to use to verify whether the app transaction belongs to the device.
- [var deviceVerificationNonce: UUID](./deviceverificationnonce-6082b.md)
  The UUID for computing the device verification value.
- [var signedDate: Date](./signeddate-24zch.md)
  The date that the App Store signed the JWS app transaction.
- [var headerData: Data](./headerdata-3drrl.md)
  The header component of the JWS app transaction.
- [var signedData: Data](./signeddata-99fyo.md)
  The app transaction data that the signature applies to.
- [var signatureData: Data](./signaturedata-4pvv0.md)
  The signature component of the JWS app transaction.
- [var signature: P256.Signing.ECDSASignature](./signature-6d5ue.md)
  The signature component of the JSON web signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/payloaddata-97acz)*