# deviceVerificationNonce

**Framework**: StoreKit  
**Kind**: property

The UUID for computing the device verification value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var deviceVerificationNonce: UUID { get }
```

#### Discussion

Use the lowercased nonce when computing the [`deviceVerification`](verificationresult/deviceverification-5hvi9.md) value.

This value is identical to the [`deviceVerificationNonce`](product/subscriptioninfo/renewalinfo/deviceverificationnonce.md) value in [`Product.SubscriptionInfo.RenewalInfo`](product/subscriptioninfo/renewalinfo.md).

## See Also

- [var jwsRepresentation: String](verificationresult/jwsrepresentation-178oj.md)
  The subscription renewal information signed by the App Store, in JWS Compact Serialization format.
- [var deviceVerification: Data](verificationresult/deviceverification-5hvi9.md)
  The device verification value to use to verify whether the subscription renewal information belongs to the device.
- [var signedDate: Date](verificationresult/signeddate-3tvo5.md)
  The date that the App Store signed the JWS subscription renewal information.
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

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/deviceverificationnonce-6mzfc)*