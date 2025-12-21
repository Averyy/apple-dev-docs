# Set App Account Token

**Framework**: App Store Server API  
**Kind**: httpRequest

Sets the app account token value for a purchase the customer makes outside of your app, or updates its value in an existing transaction.

**Availability**:
- App Store Server API 1.16+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

An [`appAccountToken`](appaccounttoken.md) is a UUID you create to associate a transaction with a customer account in your system. Use the [`Set App Account Token`](set-app-account-token.md) endpoint to set or reset the `appAccountToken` associated with the transaction you specify in the `originalTransactionId` parameter.

Typically, your app sets the [`appAccountToken(_:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) when a customer makes a purchase in your app. However, customers can also purchase in-app products outside of your app, for example, by redeeming an offer code in the App Store. In that case, the original transaction doesn’t include an app account token. Use the `Set App Account Token` endpoint to associate an app account token with such transactions.

This endpoint supports setting the `appAccountToken` for all product types, including one-time purchases (consumables, non-consumables, and non-renewing subscriptions) and auto-renewable subscriptions. If you call this endpoint for a transaction that already has an `appAccountToken`, the endpoint replaces the existing value with the new value you supply.

For auto-renewable subscriptions, the endpoint applies the `appAccountToken` to the current renewal transaction and subsequent renewals, but it doesn’t affect past transactions. The same `appAccountToken` continues to apply to renewal transactions if the customer upgrades, downgrades, or cross-grades the subscription.

This endpoint doesn’t support transactions for products shared through Family Sharing, where the transaction has an [`inAppOwnershipType`](inappownershiptype.md) value of `FAMILY_SHARED`.

You can assign the same `appAccountToken` value to more than one transaction, according to your needs. For example, you may choose to reuse the same `appAccountToken` value for every transaction that belongs to the same customer.

## Request Body

The request body that contains a valid app account token value.

## See Also

- [object UpdateAppAccountTokenRequest](updateappaccounttokenrequest.md)
  The request body that contains an app account token value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/set-app-account-token)*