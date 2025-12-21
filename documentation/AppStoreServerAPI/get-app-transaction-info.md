# Get App Transaction Info

**Framework**: App Store Server API  
**Kind**: httpRequest

Get a customer’s app transaction information for your app.

**Availability**:
- App Store Server API 1.17+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Use this endpoint to get the app transaction information for a customer of your app. You can provide any transaction ID that belongs to the customer to get their app transaction information.

App transaction information represents the customer’s purchase of the app, cryptographically signed by the App Store. The App Store generates a single, globally unique [`appTransactionId`](apptransactionid.md) for each Apple Account that downloads your app and for each family group member for apps that support Family Sharing. The `appTransactionId` value remains the same for the same Apple Account and app if the customer redownloads the app on any device, receives a refund, repurchases the app, or changes the storefront. For apps that support Family Sharing, the `appTransactionId` is unique for each family group member.

App transaction information includes details about the app the customer purchased, such as its bundleID, original version, original purchase date, and more. You can also get app transaction information in your app from StoreKit, using [`AppTransaction`](https://developer.apple.com/documentation/StoreKit/AppTransaction).

## See Also

- [object AppTransactionInfoResponse](apptransactioninforesponse.md)
  A response that contains signed app transaction information for a customer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-app-transaction-info)*