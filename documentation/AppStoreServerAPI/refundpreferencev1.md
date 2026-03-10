# refundPreferenceV1

**Framework**: App Store Server API  
**Kind**: typealias

A value that indicates your preferred outcome for the refund request.

**Availability**:
- App Store Server API 1.11+

## Declaration

```swift
int32 refundPreferenceV1
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

Your refund preference is one of a variety of factors that the App Store uses to inform its refund decisions.

## See Also

- [type accountTenure](accounttenure.md)
  The age of the customer’s account.
- [type appAccountToken](appaccounttoken.md)
  The UUID that you generate to associate a customer’s In-App Purchase with its resulting App Store transaction.
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
- [type sampleContentProvided](samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.
- [type userStatus](userstatus.md)
  The status of a customer’s account within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/refundpreferencev1)*