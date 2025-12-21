# consumptionStatus

**Framework**: App Store Server API  
**Kind**: typealias

A value that indicates the extent to which the customer consumed the In-App Purchase.

**Availability**:
- App Store Server API ?+ - Deprecated

## Declaration

```swift
int32 consumptionStatus
```

#### Discussion

Some examples of consumption status include the following scenarios:

- A customer purchases a “bag of 100 coins” in your app and spends all 100 coins. The In-App Purchase is considered fully consumed.
- If your app has an exchange platform that has bartering, or if your app transferred an In-App Purchase from one account to another customer’s account, the In-App Purchase is considered fully consumed.

## See Also

- [type accountTenure](accounttenure.md)
  The age of the customer’s account.
- [type appAccountToken](appaccounttoken.md)
  The UUID that you generate to associate a customer’s In-App Purchase with its resulting App Store transaction.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/consumptionstatus)*