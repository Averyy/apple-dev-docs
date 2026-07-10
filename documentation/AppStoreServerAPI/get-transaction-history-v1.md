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
GET https://api.storekit.apple.com/inApps/v1/history/{anyTransactionId}?productType=NON_CONSUMABLE&productType=AUTO_RENEWABLE
```

When you specify multiple values for a single query parameter, the response contains transactions that match any of the values.

> **Note**:  If you use optional query parameters, be sure to use the same query parameters on subsequent requests that include the `revision` parameter.

To request a full transaction history in ascending order for your app, start by calling the endpoint without any query parameters, as follows:

```javascript
GET https://api.storekit.apple.com/inApps/v1/history/{anyTransactionId}
```

For subsequent requests, include the `revision` token from the previous [`HistoryResponse`](historyresponse.md).

```javascript
GET https://api.storekit.apple.com/inApps/v1/history/{anyTransactionId}?revision={revision}
```

## Endpoint

`GET https://api.storekit-sandbox.apple.com/inApps/v1/history/{anyTransactionId}`

## Parameters

- `revision` (revision): A token you provide to get the next set of up to 20 transactions. All responses include a `revision` token. Use the `revision` token from the previous [`HistoryResponse`](historyresponse.md). Note: The `revision` token is required in all requests except the initial request. For requests that use the `revision` token, include the same query parameters from the initial request.
- `startDate` (startDate): An optional start date of the timespan for the transaction history records you’re requesting. The `startDate` needs to precede the `endDate` if you specify both dates. The results include a transaction if its [`purchaseDate`](purchasedate.md) is equal to or greater than the `startDate`.
- `endDate` (endDate): An optional end date of the timespan for the transaction history records you’re requesting. Choose an `endDate` that’s later than the `startDate` if you specify both dates. Using an `endDate` in the future is valid. The results include a transaction if its [`purchaseDate`](purchasedate.md) is less than the `endDate`.
- `productId` ([productId]): An optional filter that indicates the product identifier to include in the transaction history. Your query may specify more than one `productID`.
- `productType` ([string]): An optional filter that indicates the product type to include in the transaction history. Your query may specify more than one `productType`.
- `sort` (string): An optional sort order for the transaction history records. The response sorts the transaction records by their recently modified date. The default value is `ASCENDING`, so you receive the oldest records first.
- `subscriptionGroupIdentifier` ([subscriptionGroupIdentifier]): An optional filter that indicates the subscription group identifier to include in the transaction history. Your query may specify more than one `subscriptionGroupIdentifier`.
- `inAppOwnershipType` (inAppOwnershipType): An optional filter that limits the transaction history by the in-app ownership type.
- `revoked` (boolean): An optional Boolean value that indicates whether the response includes only revoked transactions when the value is `true`, or contains only nonrevoked transactions when the value is `false`. By default, the request doesn’t include this parameter.
- `excludeRevoked` (boolean): Set `revoked` to `false` to exclude revoked transactions instead.

## See Also

- [Get Refund History V1](get-refund-history-v1.md)
  Get a list of up to 50 of a customer’s refunded in-app purchases for your app.
- [object RefundLookupResponse](refundlookupresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-history-v1)*