# Look Up Order ID

**Framework**: App Store Server API  
**Kind**: httpRequest

Get a customer’s in-app purchases from a receipt using the order ID.

**Availability**:
- App Store Server API 1.1+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

> ❗ **Important**:  This endpoint isn’t available in the sandbox environment.

Call this endpoint to identify and validate a customer’s in-app purchases, based on their order ID.

When a customer contacts you for support, ask for their order ID and use that value to call this endpoint. Customers can retrieve their order IDs from their purchase history on the App Store; for more information, see [`See your purchase history for the App Store, iTunes store, and more`](https://developer.apple.comhttps://support.apple.com/en-gb/HT204088). The App Store also sends customers an email receipt with an order ID each time they make in-app purchases.

A successful response with an [`OrderLookupStatus`](orderlookupstatus.md) value of `0` contains an array of one or more signed transactions for the in-app purchase based on the order ID. Use the decoded transaction, [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md), to identify information such as the `productId` and `purchaseDate` that you can use to provide customer support.

A response with an [`OrderLookupStatus`](orderlookupstatus.md) value of `1` doesn’t contain a signed transactions array.

The App Store Server API returns information based on the customer’s in-app purchase history regardless of whether the customer installed, removed, or reinstalled the app on their devices.

## Topics

### Request data types
- [type orderId](orderid.md)
  The customer’s order ID from an App Store receipt for in-app purchases.

## See Also

- [type orderId](orderid.md)
  The customer’s order ID from an App Store receipt for in-app purchases.
- [object OrderLookupResponse](orderlookupresponse.md)
  A response that includes the order lookup status and an array of signed transactions for the in-app purchases in the order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/look-up-order-id)*