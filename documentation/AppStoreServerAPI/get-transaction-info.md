# Get Transaction Info

**Framework**: App Store Server API  
**Kind**: httpRequest

Get information about a single transaction for your app.

**Availability**:
- App Store Server API 1.8+

## Mentions

- [Identifying rate limits](identifying-rate-limits.md)
- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

Use this endpoint to get transaction information for any transaction identifier, including original transaction identifiers.  This endpoint supports all in-app purchase types, including consumable, non-consumable, non-renewing subscriptions, and auto-renewable subscriptions. It also supports transactions that your app marked as finished using [`finish()`](https://developer.apple.com/documentation/StoreKit/Transaction/finish()) or [`finishTransaction(_:)`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)) in StoreKit.

## See Also

- [object TransactionInfoResponse](transactioninforesponse.md)
  A response that contains signed transaction information for a single transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-info)*