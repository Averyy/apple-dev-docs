# appAccountToken

**Framework**: App Store Server API  
**Kind**: typealias

The UUID that an app optionally generates to map a customer’s In-App Purchase with its resulting App Store transaction.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
uuid appAccountToken
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

When a customer initiates an in-app purchase, you can optionally generate an [`appAccountToken(_:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) and send it to the App Store. If you use the [`Original API for In-App Purchase`](https://developer.apple.com/documentation/StoreKit/original-api-for-in-app-purchase), you may provide a UUID in the [`applicationUsername`](https://developer.apple.com/documentation/StoreKit/SKMutablePayment/applicationUsername) property. The App Store returns the same UUID in [`appAccountToken`](https://developer.apple.com/documentation/StoreKit/Transaction/appAccountToken) in the transaction information after the customer completes the purchase.

The [`ConsumptionRequest`](consumptionrequest.md) response body requires that you set the `appAccountToken` value to a valid value of either a UUID or an empty string. Set the `appAccountToken` value to the value you received in the `CONSUMPTION_REQUEST` notification, or, if you choose not to provide this information, set the value to an empty string.

If you receive a `CONSUMPTION_REQUEST` notification for a transaction, find its associated `appAccountToken` value as follows:

- If you receive App Store Server Notifications version 2, the `appAccountToken` value is in [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload).
- If you receive App Store Server Notifications version 1, the `appAccountToken` value is in [`unified_receipt.Latest_receipt_info`](https://developer.apple.com/documentation/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary).

The `appAccountToken` value may be an empty string if your app doesn’t use app account tokens.

For more information about App Store Server Notifications versions, see [`App Store Server Notifications changelog`](https://developer.apple.com/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog).

## See Also

- [type accountTenure](accounttenure.md)
  The age of the customer’s account.
- [type consumptionStatus](consumptionstatus.md)
  A value that indicates the extent to which the customer consumed the in-app purchase.
- [type customerConsented](customerconsented.md)
  A Boolean value that indicates whether the customer consented to provide consumption data to the App Store.
- [type deliveryStatus](deliverystatus.md)
  A value that indicates whether the app successfully delivered an in-app purchase that works properly.
- [type lifetimeDollarsPurchased](lifetimedollarspurchased.md)
  A value that indicates the dollar amount of in-app purchases the customer has made in your app, since purchasing the app, across all platforms.
- [type lifetimeDollarsRefunded](lifetimedollarsrefunded.md)
  A value that indicates the dollar amount of refunds the customer has received in your app, since purchasing the app, across all platforms.
- [type platform](platform.md)
  The platform on which the customer consumed the in-app purchase.
- [type playTime](playtime.md)
  A value that indicates the amount of time that the customer used the app.
- [type refundPreference](refundpreference.md)
  A value that indicates your preferred outcome for the refund request.
- [type sampleContentProvided](samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.
- [type userStatus](userstatus.md)
  The status of a customer’s account within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/appaccounttoken)*