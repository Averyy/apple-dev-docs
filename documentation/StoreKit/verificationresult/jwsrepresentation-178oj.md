# jwsRepresentation

**Framework**: StoreKit  
**Kind**: property

The subscription renewal information signed by the App Store, in JWS Compact Serialization format.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var jwsRepresentation: String { get }
```

#### Discussion

Use this JSON Web Signature (JWS) value to perform your own JWS verification on your server or on the device.

The [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) is the same as the [`JWSRenewalInfo`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSRenewalInfo) that the App Store Server API returns, and the [`JWSRenewalInfo`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSRenewalInfo) that you receive from App Store Server Notifications. The [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md)’s decoded payload contains two additional fields: `deviceVerification` and `deviceVerificationNonce`. Use these fields on the device to verify that the JWS information belongs to the device. For more information, see [`deviceVerificationID`](appstore/deviceverificationid.md).

To verify the [`jwsRepresentation`](verificationresult/jwsrepresentation-178oj.md) on your server, consider using the App Store Server Library function `verifyAndDecodeRenewalInfo`, available in each language the library supports. For more information, see [`Simplifying your implementation by using the App Store Server Library`](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

> ❗ **Important**:  The decoded payloads of the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) and [`JWSRenewalInfo`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSRenewalInfo) strings contain [`renewalPrice`](https://developer.apple.com/documentation/AppStoreServerAPI/renewalPrice) fields that are specified in  of the currency; StoreKit represents the [`renewalPrice`](product/subscriptioninfo/renewalinfo/renewalprice.md) in  of currency. Take care not to confuse these two representations when working with both APIs.

## See Also

- [var deviceVerification: Data](verificationresult/deviceverification-5hvi9.md)
  The device verification value to use to verify whether the subscription renewal information belongs to the device.
- [var deviceVerificationNonce: UUID](verificationresult/deviceverificationnonce-6mzfc.md)
  The UUID for computing the device verification value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/jwsrepresentation-178oj)*