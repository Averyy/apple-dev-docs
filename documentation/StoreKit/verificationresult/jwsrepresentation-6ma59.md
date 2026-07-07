# jwsRepresentation

**Framework**: StoreKit  
**Kind**: property

The app transaction signed by the App Store, in JWS Compact Serialization format.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var jwsRepresentation: String { get }
```

#### Discussion

Use this JSON Web Signature (JWS) value to perform your own JWS verification on your server or on the device.

To verify the [`jwsRepresentation`](verificationresult/jwsrepresentation-6ma59.md) on your server, consider using the App Store Server Library function `verifyAndDecodeAppTransaction`, available in each language the library supports. For more information, see [`Simplifying your implementation by using the App Store Server Library`](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

The [`jwsRepresentation`](verificationresult/jwsrepresentation-6ma59.md)’s decoded payload contains the fields `deviceVerification` and `deviceVerificationNonce`. Use these fields on the device to verify that the JWS information belongs to the device. For more information, see [`deviceVerificationID`](appstore/deviceverificationid.md).

## See Also

- [var deviceVerification: Data](verificationresult/deviceverification-6c8xu.md)
  The device verification value to use to verify whether the app transaction belongs to the device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/jwsrepresentation-6ma59)*