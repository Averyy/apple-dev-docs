# jwsRepresentation

**Framework**: StoreKit  
**Kind**: property

The transaction signed by the App Store, in JWS Compact Serialization format.

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

## Mentions

- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)

#### Discussion

Use this JSON Web Signature (JWS) value to perform your own JWS verification on your server or on the device.

The [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) is the same as the [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransaction) that the App Store Server API returns and the [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSTransaction) that you receive from App Store Server Notifications. The [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md)’s decoded payload contains two additional fields: `deviceVerification` and `deviceVerificationNonce`. Use these fields on the device to verify that the JWS information belongs to the device. For more information, see [`deviceVerificationID`](appstore/deviceverificationid.md).

To verify the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) on your server, consider using the App Store Server Library function `verifyAndDecodeTransaction`, available in each language the library supports. For more information, see [`Simplifying your implementation by using the App Store Server Library`](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

> ❗ **Important**:  The decoded payloads of the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) and [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransaction) strings contain [`price`](https://developer.apple.com/documentation/AppStoreServerAPI/price) fields that are specified in  of the currency;  StoreKit represents the `price`  in  of currency. Take care not to confuse these two representations when working with both APIs.

## See Also

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
- [var signatureData: Data](verificationresult/signaturedata-4pyv8.md)
  The signature component of the JWS transaction.
- [var signature: P256.Signing.ECDSASignature](verificationresult/signature-7t1ne.md)
  The signature component of the JSON web signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/jwsrepresentation-21vgo)*