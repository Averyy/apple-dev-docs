# JWSAppTransactionDecodedPayload

**Framework**: App Store Server API  
**Kind**: dictionary

A decoded payload that contains app transaction information.

**Availability**:
- App Store Server API 1.17+

## Declaration

```swift
object JWSAppTransactionDecodedPayload
```

#### Discussion

The [`Get App Transaction Info`](get-app-transaction-info.md) endpoint returns a [`JWSAppTransaction`](jwsapptransaction.md), which you decode to get `JWSAppTransactionDecodedPayload`.

You can also get app transaction information in your app from StoreKit, using [`AppTransaction`](https://developer.apple.com/documentation/StoreKit/AppTransaction).

## Properties

- `appAppleId` (appAppleId): The unique identifier the App Store uses to identify the app.
- `appTransactionId` (appTransactionId): The unique identifier of the app download transaction.
- `bundleId` (bundleId): The bundle identifier that the app transaction applies to.
- `originalApplicationVersion` (originalApplicationVersion): The app version that the customer originally purchased from the App Store.
- `originalPlatform` (originalPlatform): The platform on which the customer originally purchased the app.
- `originalPurchaseDate` (originalPurchaseDate): The date the customer originally purchased the app from the App Store.
- `preorderDate` (preorderDate): The date the customer placed an order for the app before it’s available in the App Store.
- `receiptCreationDate` (receiptCreationDate): The date that the App Store signed the JWS app transaction.
- `receiptType` (environment): The server environment, production or sandbox, that signed the app transaction.

## See Also

- [object JWSDecodedHeader](jwsdecodedheader.md)
  A decoded JSON Web Signature (JWS) header containing transaction or renewal information.
- [type JWSAppTransaction](jwsapptransaction.md)
  App transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.
- [type JWSRenewalInfo](jwsrenewalinfo.md)
  Subscription renewal information, signed by the App Store, in JSON Web Signature (JWS) format.
- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [Data types](data-types.md)
  Refer to these data types for decoded transaction and renewal information payloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/jwsapptransactiondecodedpayload)*