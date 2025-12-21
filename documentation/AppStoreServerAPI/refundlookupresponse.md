# RefundLookupResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains an array of signed JSON Web Signature (JWS) transactions.

**Availability**:
- App Store Server API 1.1+

## Declaration

```swift
object RefundLookupResponse
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

If the customer hasn’t received any refunds for in-app purchases in your app, the `signedTransactions` array is empty. To read the transaction information, decode the payload for each [`JWSTransaction`](jwstransaction.md) object in the `signedTransactions` array. Use a [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) object to read the transaction information in the payload.

This response can contain a maximum of 50 transactions in the `signedTransactions` array.

## See Also

- [Get Transaction History V1](get-transaction-history-v1.md)
  Get a customer’s in-app purchase transaction history for your app, except finished consumable in-app purchases.
- [Get Refund History V1](get-refund-history-v1.md)
  Get a list of up to 50 of a customer’s refunded in-app purchases for your app.
- [Send Consumption Information V1](send-consumption-information-v1.md)
  Send consumption information about a consumable In-App Purchase or auto-renewable subscription to the App Store after your server receives a consumption request notification.
- [object ConsumptionRequestV1](consumptionrequestv1.md)
  The request body containing consumption information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/refundlookupresponse)*