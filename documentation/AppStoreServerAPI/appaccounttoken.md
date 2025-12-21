# appAccountToken

**Framework**: App Store Server API  
**Kind**: typealias

The UUID that you generate to associate a customer’s In-App Purchase with its resulting App Store transaction.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
uuid appAccountToken
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

When a customer initiates an In-App Purchase in your app, you can optionally generate an app account token and call [`appAccountToken(_:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) to associate it with the purchase. If you use the [`Original API for In-App Purchase`](https://developer.apple.com/documentation/StoreKit/original-api-for-in-app-purchase), you can provide a UUID in the [`applicationUsername`](https://developer.apple.com/documentation/StoreKit/SKMutablePayment/applicationUsername) property. The App Store returns the same UUID in [`appAccountToken`](https://developer.apple.com/documentation/StoreKit/Transaction/appAccountToken) in the transaction information and subscription renewal information after the customer completes the purchase.

To provide an app account token for a transaction that the customer completes outside of your app, or to update the value of an existing app account token, call the [`Set App Account Token`](set-app-account-token.md) endpoint.

## See Also

- [type accountTenure](accounttenure.md)
  The age of the customer’s account.
- [type consumptionStatus](consumptionstatus.md)
  A value that indicates the extent to which the customer consumed the In-App Purchase.
- [type customerConsented](customerconsented.md)
  A Boolean value that indicates whether the customer consented to provide consumption data to the App Store.
- [type deliveryStatusV1](deliverystatusv1.md)
  A value that indicates whether the app successfully delivered an In-App Purchase that works properly.
- [type lifetimeDollarsPurchased](lifetimedollarspurchased.md)
  A value that indicates the dollar amount of in-app purchases the customer has made in your app, since purchasing the app, across all platforms.
- [type lifetimeDollarsRefunded](lifetimedollarsrefunded.md)
  A value that indicates the dollar amount of refunds the customer has received in your app, since purchasing the app, across all platforms.
- [type platform](platform.md)
  The platform on which the customer consumed the in-app purchase.
- [type playTime](playtime.md)
  A value that indicates the amount of time that the customer used the app.
- [type refundPreferenceV1](refundpreferencev1.md)
  A value that indicates your preferred outcome for the refund request.
- [type sampleContentProvided](samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.
- [type userStatus](userstatus.md)
  The status of a customer’s account within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/appaccounttoken)*