# Get Transaction History V1

**Framework**: App Store Server API  
**Kind**: httpRequest

Get a customer’s in-app purchase transaction history for your app, except finished consumable in-app purchases.

**Availability**:
- App Store Server API 1.0+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

The [`Get Transaction History V1`](get-transaction-history-v1.md) endpoint returns results for the following product types:

- Auto-renewable subscriptions
- Non-renewing subscriptions
- Non-consumable in-app purchases
- Consumable in-app purchases if the transaction is refunded or revoked, or if the app hasn’t finished processing the transaction. The results don’t include consumable in-app purchases that the app marks as finished. For more information about finishing transactions, see [`finish()`](https://developer.apple.com/documentation/StoreKit/Transaction/finish()) and [`finishTransaction(_:)`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)).

> **Note**:  Use [`Get Transaction History`](get-transaction-history.md) instead to get all the product types, including consumable in-app purchases in the finished state.

You can customize your request by including query parameters that filter the transaction history. The query parameters limit the scope of the request by dates, product IDs, product types, and subscription group identifiers. You can also exclude revoked or nonrevoked transactions, and limit the transactions by in-app ownership type. If you provide multiple filters in the query, the transactions that return match all the filters.

You can also specify a sort order. The App Store sorts the transactions based on their recently modified dates. Use a `DESCENDING` order to get the most recent transactions first. The App Store updates the recently modified date if the customer upgrades a subscription or the App Store revokes an in-app purchase. If a transaction updates while you’re receiving transaction history and the response is sorted in `ASCENDING` order, you may receive the transaction again with updated data.

The `productId`, `productType`, and `subscriptionGroupIdentifier` query parameters allow you to specify multiple values. To specify more than one value for a query parameter, include it in the request multiple times. For example, to filter the transaction history by non-consumable and auto-renewable product types, include the following within your request:

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v1/history/{transactionId}?productType=NON_CONSUMABLE&productType=AUTO_RENEWABLE
```

When you specify multiple values for a single query parameter, the response contains transactions that match any of the values.

> **Note**:  If you use optional query parameters, be sure to use the same query parameters on subsequent requests that include the `revision` parameter.

To request a full transaction history in ascending order for your app, start by calling the endpoint without any query parameters, as follows:

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v1/history/{transactionId}
```

For subsequent requests, include the `revision` token from the previous [`HistoryResponse`](historyresponse.md).

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v1/history/{transactionId}?revision={revision}
```

## See Also

- [Get Transaction History](get-transaction-history.md)
  Get a customer’s in-app purchase transaction history for your app.
- [object HistoryResponse](historyresponse.md)
  A response that contains the customer’s transaction history for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-history-v1)*