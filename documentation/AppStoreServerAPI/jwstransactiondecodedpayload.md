# JWSTransactionDecodedPayload

**Framework**: App Store Server API  
**Kind**: dictionary

A decoded payload that contains transaction information.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
object JWSTransactionDecodedPayload
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

> ❗ **Important**:  Don’t use the `price` or `currency` values for any revenue reconciliation or recognition. App Store Connect reporting is your source of record for financial and accounting purposes. For more information, see [`Overview of reporting tools`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

## Properties

- `appAccountToken` (appAccountToken): A UUID you create at the time of purchase that associates the transaction with a customer on your own service. If your app doesn’t provide an `appAccountToken`, this field is omitted. For more information, see [`appAccountToken(_:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)).
- `appTransactionId` (appTransactionId): The unique identifier of the app download transaction.
- `bundleId` (bundleId): The bundle identifier of the app.
- `currency` (currency): The three-letter ISO 4217 currency code associated with the `price` parameter. This value is present only if `price` is present.
- `environment` (environment): The server environment, either sandbox or production.
- `expiresDate` (expiresDate): The UNIX time, in milliseconds, that the subscription expires or renews.
- `inAppOwnershipType` (inAppOwnershipType): A string that describes whether the transaction was purchased by the customer, or is available to them through Family Sharing.
- `isUpgraded` (isUpgraded): A Boolean value that indicates whether the customer upgraded to another subscription.
- `offerDiscountType` (offerDiscountType): The payment mode you configure for the offer.
- `offerIdentifier` (offerIdentifier): The identifier that contains the offer code or the promotional offer identifier.
- `offerPeriod` (offerPeriod): The duration of the offer applied to the transaction.
- `offerType` (offerType): A value that represents the promotional offer type.
- `originalPurchaseDate` (originalPurchaseDate): The UNIX time, in milliseconds, that represents the purchase date of the original transaction identifier.
- `originalTransactionId` (originalTransactionId): The transaction identifier of the original purchase.
- `price` (price): An integer value that represents the price multiplied by 1000 of the in-app purchase or subscription offer you configured in App Store Connect and that the system records at the time of the purchase. For more information, see [`price`](https://developer.apple.com/documentation/AppStoreServerNotifications/price). The `currency` parameter indicates the currency of this price.
- `productId` (productId): The unique identifier of the product.
- `purchaseDate` (purchaseDate): The UNIX time, in milliseconds, that the App Store charged the customer’s account for a purchase, restored product, subscription, or subscription renewal after a lapse.
- `quantity` (quantity): The number of consumable products the customer purchased.
- `revocationDate` (revocationDate): The UNIX time, in milliseconds, that the App Store refunded the transaction or revoked it from Family Sharing.
- `revocationPercentage` (revocationPercentage): The percentage, in milliunits, of the transaction that the App Store has refunded or revoked.
- `revocationReason` (revocationReason): The reason that the App Store refunded the transaction or revoked it from Family Sharing.
- `revocationType` (revocationType): The type of the refund or revocation that applies to the transaction.
- `signedDate` (signedDate): The UNIX time, in milliseconds, that the App Store signed the JSON Web Signature (JWS) data.
- `storefront` (storefront): The three-letter code that represents the country or region associated with the App Store storefront for the purchase.
- `storefrontId` (storefrontId): An Apple-defined value that uniquely identifies the App Store storefront associated with the purchase.
- `subscriptionGroupIdentifier` (subscriptionGroupIdentifier): The identifier of the subscription group to which the subscription belongs.
- `transactionId` (transactionId): The unique identifier of the transaction.
- `transactionReason` (transactionReason): The reason for the purchase transaction, which indicates whether it’s a customer’s purchase or a renewal for an auto-renewable subscription that the system initates.
- `type` (type): The type of the in-app purchase.
- `webOrderLineItemId` (webOrderLineItemId): The unique identifier of subscription purchase events across devices, including subscription renewals.
- `advancedCommerceInfo` (advancedCommerceTransactionInfo): Transaction information that is present only for Advanced Commerce SKUs.

## See Also

- [object JWSDecodedHeader](jwsdecodedheader.md)
  A decoded JSON Web Signature (JWS) header containing transaction or renewal information.
- [type JWSAppTransaction](jwsapptransaction.md)
  App transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [object JWSAppTransactionDecodedPayload](jwsapptransactiondecodedpayload.md)
  A decoded payload that contains app transaction information.
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [type JWSRenewalInfo](jwsrenewalinfo.md)
  Subscription renewal information, signed by the App Store, in JSON Web Signature (JWS) format.
- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [Data types](data-types.md)
  Refer to these data types for decoded transaction and renewal information payloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/jwstransactiondecodedpayload)*