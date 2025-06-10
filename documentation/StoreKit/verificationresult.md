# VerificationResult

**Framework**: StoreKit  
**Kind**: enum

A type that describes the result of a StoreKit verification.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
enum VerificationResult<SignedType>
```

#### Overview

StoreKit automatically verifies the [`Transaction`](transaction.md), [`Product.SubscriptionInfo.RenewalInfo`](product/subscriptioninfo/renewalinfo.md), and [`AppTransaction`](apptransaction.md) values. To access the wrapped values, check whether the values are verified or unverified.

In addition to getting a verification result from StoreKit, you might want to verify the signed information yourself, either on the device, or on your server for the most control and security. Perform the verification on the [`jwsRepresentation`](verificationresult/jwsrepresentation-178oj.md) property for subscription renewal information, the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) property for transactions, and the [`jwsRepresentation`](verificationresult/jwsrepresentation-6ma59.md) property for an app transaction.

To verify the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) on your server, consider using the verification functions in the App Store Server Library. The library provides the functions `verifyAndDecodeTransaction`, `verifyAndDecodeAppTransaction`, and `verifyAndDecodeRenewalInfo` in each language the library supports. For more information, see [`Simplifying your implementation by using the App Store Server Library`](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

The [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) string is in JWS Compact Serialization format and is the same as its counterpart in the App Store server APIs, as follows:

| StoreKit string | Equivalent in the App Store Server API | Equivalent in App Store Server Notifications |
| --- | --- | --- |
| [`jwsRepresentation`](verificationresult/jwsrepresentation-178oj.md) for subscription renewal information | [`JWSRenewalInfo`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSRenewalInfo) | [`JWSRenewalInfo`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSRenewalInfo) |
| [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) for transactions | [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransaction) | [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSTransaction) |

The decoded payload of the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) contains  two additional fields: `deviceVerification` and `deviceVerificationNonce`. Use these fields on the device to verify that JWS information belongs to the device. For more information, see [`deviceVerificationID`](appstore/deviceverificationid.md).

> ❗ **Important**:  The decoded payloads of [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) and [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransaction) strings contain [`price`](https://developer.apple.com/documentation/AppStoreServerAPI/price) or [`renewalPrice`](https://developer.apple.com/documentation/AppStoreServerAPI/renewalPrice) fields specified in  of the currency.  StoreKit represents the `price` and [`renewalPrice`](product/subscriptioninfo/renewalinfo/renewalprice.md) values in is  of the currency. Take care not to confuse these two representations when working with both APIs.

## Topics

### Getting the verification results
- [VerificationResult.verified(_:)](verificationresult/verified(_:).md)
  The associated value passed StoreKit automatic verification checks.
- [case unverified(SignedType, VerificationResult<SignedType>.VerificationError)](verificationresult/unverified(_:_:).md)
  The associated value failed StoreKit automatic verification checks.
- [var payloadValue: SignedType](verificationresult/payloadvalue.md)
  The verified value of the signed type that StoreKit confirms as verified.
- [var unsafePayloadValue: SignedType](verificationresult/unsafepayloadvalue.md)
  The associated value of the verification result that StoreKit doesn’t confirm as verified.
- [VerificationResult.VerificationError](verificationresult/verificationerror.md)
  Error cases for StoreKit JWS verification.
### Getting properties for transactions
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
- [var signatureData: Data](verificationresult/signaturedata-4pyv8.md)
  The signature component of the JWS transaction.
- [var signature: P256.Signing.ECDSASignature](verificationresult/signature-7t1ne.md)
  The signature component of the JSON web signature.
### Getting properties for subscription renewal information
- [var jwsRepresentation: String](verificationresult/jwsrepresentation-178oj.md)
  The subscription renewal information signed by the App Store, in JWS Compact Serialization format.
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
### Getting properties for app transactions
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
- [var signature: P256.Signing.ECDSASignature](verificationresult/signature-6d5ue.md)
  The signature component of the JSON web signature.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [VerificationResult.VerificationError](verificationresult/verificationerror.md)
  Error cases for StoreKit JWS verification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult)*