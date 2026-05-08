# Finish Transaction

**Framework**: App Store Server API  
**Kind**: httpRequest

Notifies the App Store server that your system has finished processing the customer’s transaction.

**Availability**:
- App Store Server API 1.20+ - Deprecated

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

If you manage entitlement logic on your server, your server can call `Finish Transaction` after it finishes providing the customer with the new content. If you call [`finish()`](https://developer.apple.com/documentation/StoreKit/Transaction/finish()) in your app, there’s no need to call the `Finish Transaction` endpoint from your server.

## Endpoint

`POST https://api.storekit-sandbox.apple.com/inApps/v1/transactions/{transactionId}/finish`

## Parameters

- `transactionId` (transactionId) *(required)*: The transaction identifier of the transaction to mark as finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/finish-transaction)*