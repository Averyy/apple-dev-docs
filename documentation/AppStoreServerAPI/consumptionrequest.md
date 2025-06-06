# ConsumptionRequest

**Framework**: App Store Server API  
**Kind**: dictionary

The request body containing consumption information.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
object ConsumptionRequest
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

Use `ConsumptionRequest` to provide information about the customer’s consumable in-app purchase or auto-renewable subscription when you call the [`Send Consumption Information`](send-consumption-information.md) endpoint.

To create a valid request and avoid an `HTTP 400 Bad Request` error, [`ConsumptionRequest`](consumptionrequest.md) must contain all the required fields with proper data types and valid values. However, you can choose whether or not to provide information for most fields. Most fields have a valid option if you choose not to provide the information.

> **Note**:  Use the field value for , where available, if you choose not to provide information.

 Use the field value for , where available, if you choose not to provide information.

For example, if you choose not to provide information for the [`accountTenure`](consumptionrequest/accounttenure.md) field, set [`accountTenure`](consumptionrequest/accounttenure.md) to `0`. If you choose not to provide information for the [`appAccountToken`](consumptionrequest/appaccounttoken.md) field, set its value to an empty string. Refer to each field’s documentation for the list of valid values, including the undeclared value where available.

The App Store server rejects requests that have a [`customerConsented`](consumptionrequest/customerconsented.md) value other than `true` by returning an `HTTP 400` error with an `InvalidCustomerConsentError`.

## Topics

### Consumption Data Types
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
- [type sampleContentProvided](samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.
- [type userStatus](userstatus.md)
  The status of a customer’s account within your app.

## See Also

- [Send Consumption Information](send-consumption-information.md)
  Send consumption information about a consumable in-app purchase or auto-renewable subscription to the App Store after your server receives a consumption request notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/consumptionrequest)*