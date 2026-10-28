# deliveryStatusV1

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

A value that indicates whether the app successfully delivered an In-App Purchase that works properly.

**Availability**:
- App Store Server API 1.0+

> **Deprecated**: Use [`deliveryStatus`](./deliverystatus.md) instead, along with the [`ConsumptionRequest`](./consumptionrequest.md) for the [`Send Consumption Information`](./send-consumption-information.md) endpoint.

## Declaration

```
int32 deliveryStatusV1
```

## Possible Values

- `0`: The app delivered the consumable In-App Purchase and it’s working properly.
- `1`: The app didn’t deliver the consumable In-App Purchase due to a quality issue.
- `2`: The app delivered the wrong item.
- `3`: The app didn’t deliver the consumable In-App Purchase due to a server outage.
- `4`: The app didn’t deliver the consumable In-App Purchase due to an in-game currency change.
- `5`: The app didn’t deliver the consumable In-App Purchase for other reasons.

## Discussion

Use these delivery status values in the [`ConsumptionRequestV1`](./consumptionrequestv1.md) request body.

## See Also

### Consumption data types
- [type accountTenure](./accounttenure.md)
  The age of the customer’s account.
- [type appAccountToken](./appaccounttoken.md)
  The UUID that you generate to associate a customer’s In-App Purchase with its resulting App Store transaction.
- [type consumptionStatus](./consumptionstatus.md)
  A value that indicates the extent to which the customer consumed the In-App Purchase.
- [type customerConsented](./customerconsented.md)
  A Boolean value that indicates whether the customer consented to provide consumption data to the App Store.
- [type lifetimeDollarsPurchased](./lifetimedollarspurchased.md)
  A value that indicates the dollar amount of in-app purchases the customer has made in your app, since purchasing the app, across all platforms.
- [type lifetimeDollarsRefunded](./lifetimedollarsrefunded.md)
  A value that indicates the dollar amount of refunds the customer has received in your app, since purchasing the app, across all platforms.
- [type platform](./platform.md)
  The platform on which the customer consumed the in-app purchase.
- [type playTime](./playtime.md)
  A value that indicates the amount of time that the customer used the app.
- [type refundPreferenceV1](./refundpreferencev1.md)
  A value that indicates your preferred outcome for the refund request.
- [type sampleContentProvided](./samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.
- [type userStatus](./userstatus.md)
  The status of a customer’s account within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/deliverystatusv1)*