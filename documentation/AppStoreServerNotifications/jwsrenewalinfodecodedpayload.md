# JWSRenewalInfoDecodedPayload

**Framework**: App Store Server Notifications  
**Kind**: dictionary

A decoded payload containing subscription renewal information for an auto-renewable subscription.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
object JWSRenewalInfoDecodedPayload
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

## Topics

### Data types
- [Transaction data types](transaction-data-types.md)
  Refer to these data types for decoded transaction and renewal information payloads.

## Properties

- `appAccountToken` (appAccountToken): A UUID you create at the time of purchase that associates the transaction with a customer on your own service. This is the token that applies to the upcoming renewal transaction. If your app doesn’t provide an `appAccountToken`, this field is omitted.  For more information, see [`appAccountToken(_:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)).
- `appTransactionId` (appTransactionId): The unique identifier of the app download transaction.
- `autoRenewProductId` (autoRenewProductId): The product identifier of the product that renews at the next billing period.
- `autoRenewStatus` (autoRenewStatus): The renewal status of the auto-renewable subscription.
- `currency` (currency): The currency code for the `renewalPrice` of the subscription.
- `eligibleWinBackOfferIds` (eligibleWinBackOfferIds): The list of win-back offer IDs that the customer is eligible for.
- `environment` (environment): The server environment, either sandbox or production.
- `expirationIntent` (expirationIntent): The reason the subscription expired.
- `gracePeriodExpiresDate` (gracePeriodExpiresDate): The time when the Billing Grace Period for subscription renewals expires.
- `isInBillingRetryPeriod` (isInBillingRetryPeriod): The Boolean value that indicates whether the App Store is attempting to automatically renew the expired subscription.
- `offerDiscountType` (offerDiscountType): The payment mode of the discount offer.
- `offerIdentifier` (offerIdentifier): The offer code or the promotional offer identifier.
- `offerPeriod` (offerPeriod): The duration of the offer.
- `offerType` (offerType): The type of offer.
- `originalTransactionId` (originalTransactionId): The transaction identifier of the original purchase associated with this transaction.
- `priceIncreaseStatus` (priceIncreaseStatus): The status that indicates whether the auto-renewable subscription is subject to a price increase.
- `productId` (productId): The product identifier of the In-App Purchase.
- `recentSubscriptionStartDate` (recentSubscriptionStartDate): The earliest start date of the auto-renewable subscription in a series of subscription purchases that ignores all lapses of paid service that are 60 days or fewer.
- `renewalDate` (renewalDate): The UNIX time, in milliseconds, when the most recent auto-renewable subscription purchase expires.
- `renewalPrice` (renewalPrice): The renewal price, in milliunits, of the auto-renewable subscription that renews at the next billing period.
- `signedDate` (signedDate): The UNIX time, in milliseconds, that the App Store signed the JSON Web Signature (JWS) data.
- `advancedCommerceInfo` (advancedCommerceRenewalInfo): Renewal information that is present only for Advanced Commerce API SKUs.

## See Also

- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.
- [object JWSDecodedHeader](jwsdecodedheader.md)
  A decoded JSON Web Signature header containing transaction or renewal information.
- [Transaction data types](transaction-data-types.md)
  Refer to these data types for decoded transaction and renewal information payloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/jwsrenewalinfodecodedpayload)*