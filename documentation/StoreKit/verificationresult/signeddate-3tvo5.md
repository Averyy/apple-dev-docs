# signedDate

**Framework**: StoreKit  
**Kind**: property

The date that the App Store signed the JWS subscription renewal information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var signedDate: Date { get }
```

#### Discussion

Use the [`signedDate`](verificationresult/signeddate-8x9bg.md) to verify whether the certificate used to sign the transaction was valid when the App Store signed the transaction.

## See Also

- [var jwsRepresentation: String](verificationresult/jwsrepresentation-178oj.md)
  The subscription renewal information signed by the App Store, in JWS Compact Serialization format.
- [var deviceVerification: Data](verificationresult/deviceverification-5hvi9.md)
  The device verification value to use to verify whether the subscription renewal information belongs to the device.
- [var deviceVerificationNonce: UUID](verificationresult/deviceverificationnonce-6mzfc.md)
  The UUID for computing the device verification value.
- [var headerData: Data](verificationresult/headerdata-3be0o.md)
  The header component of the JWS subscription renewal information.
- [var payloadData: Data](verificationresult/payloaddata-abfv.md)
  The payload component of the JWS subscription renewal information.
- [var signedData: Data](verificationresult/signeddata-1t80n.md)
  The subscription renewal information data that the signature applies to.
- [var signatureData: Data](verificationresult/signaturedata-9uw8c.md)
  The signature component of the JWS subscription renewal information.
- [var signature: P256.Signing.ECDSASignature](verificationresult/signature-95r7x.md)
  The signature component of the JSON web signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/signeddate-3tvo5)*