# signature

**Framework**: StoreKit  
**Kind**: property

The signature component of the JSON web signature.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var signature: P256.Signing.ECDSASignature { get }
```

#### Discussion

Use this [`signature`](verificationresult/signature-95r7x.md) with [`Apple CryptoKit`](https://developer.apple.com/documentation/CryptoKit) if you verify the signature on the device.

## See Also

- [var jwsRepresentation: String](verificationresult/jwsrepresentation-6ma59.md)
  The app transaction signed by the App Store, in JWS Compact Serialization format.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/signature-6d5ue)*