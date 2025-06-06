# sampleContentProvided

**Framework**: App Store Server API  
**Kind**: typealias

A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
boolean sampleContentProvided
```

#### Discussion

Set this value to `true` if you provided any of the following prior to the customer’s purchase:

- A free sample or free trial of the purchased content
- Information about the content and how it works, such as expected game play

Set this value to `false` otherwise.

## See Also

- [type accountTenure](accounttenure.md)
  The age of the customer’s account.
- [type appAccountToken](appaccounttoken.md)
  The UUID that an app optionally generates to map a customer’s In-App Purchase with its resulting App Store transaction.
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
- [type userStatus](userstatus.md)
  The status of a customer’s account within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/samplecontentprovided)*