# payloadData

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The payload component of the JWS subscription renewal information.

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
var payloadData: Data { get }
```

Available when `SignedType` is `Product.SubscriptionInfo.RenewalInfo`.

## Discussion

This value is the same as the [`jsonRepresentation`](../transaction/jsonrepresentation.md) in [`Product.SubscriptionInfo.RenewalInfo`](../product/subscriptioninfo/renewalinfo.md).

## See Also

### Getting properties for subscription renewal information
- [var jwsRepresentation: String](./jwsrepresentation-178oj.md)
  The subscription renewal information signed by the App Store, in JWS Compact Serialization format.
- [var deviceVerification: Data](./deviceverification-5hvi9.md)
  The device verification value to use to verify whether the subscription renewal information belongs to the device.
- [var deviceVerificationNonce: UUID](./deviceverificationnonce-6mzfc.md)
  The UUID for computing the device verification value.
- [var signedDate: Date](./signeddate-3tvo5.md)
  The date that the App Store signed the JWS subscription renewal information.
- [var headerData: Data](./headerdata-3be0o.md)
  The header component of the JWS subscription renewal information.
- [var signedData: Data](./signeddata-1t80n.md)
  The subscription renewal information data that the signature applies to.
- [var signatureData: Data](./signaturedata-9uw8c.md)
  The signature component of the JWS subscription renewal information.
- [var signature: P256.Signing.ECDSASignature](./signature-95r7x.md)
  The signature component of the JSON web signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/payloaddata-abfv)*