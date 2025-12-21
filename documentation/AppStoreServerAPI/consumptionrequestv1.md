# ConsumptionRequestV1

**Framework**: App Store Server API  
**Kind**: dictionary

The request body containing consumption information.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
object ConsumptionRequestV1
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

Use `ConsumptionRequestV1` to provide information about the customer’s consumable in-app purchase or auto-renewable subscription when you call the [`Send Consumption Information V1`](send-consumption-information-v1.md) endpoint.

To create a valid request and avoid an `HTTP 400 Bad Request` error, [`ConsumptionRequestV1`](consumptionrequestv1.md) must contain all the required fields with proper data types and valid values. However, you can choose whether or not to provide information for most fields. Most fields have a valid option if you choose not to provide the information.

> **Note**:  Use the field value for , where available, if you choose not to provide information.

For example, if you choose not to provide information for the [`accountTenure`](accounttenure.md) field, set [`accountTenure`](accounttenure.md) to `0`. If you choose not to provide information for the [`appAccountToken`](appaccounttoken.md) field, set its value to an empty string. Refer to each field’s documentation for the list of valid values, including the undeclared value where available.

The App Store server rejects requests that have a [`customerConsented`](customerconsented.md) value other than `true` by returning an `HTTP 400` error with an [`InvalidCustomerConsentedError`](invalidcustomerconsentederror.md).

##### Provide the App Account Token in a Consumption Request

The [`ConsumptionRequestV1`](consumptionrequestv1.md) request body requires that you set the `appAccountToken` to a valid value of either a UUID or an empty string. Set the `appAccountToken` value to the value you received in the `CONSUMPTION_REQUEST` notification, or, if you choose not to provide this information, set the value to an empty string.

If you receive a `CONSUMPTION_REQUEST` notification for a transaction, find its associated `appAccountToken` value as follows:

- If you receive [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2), the `appAccountToken` value is in [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload).
- If you receive [`App Store Server Notifications Version 1`](https://developer.apple.com/documentation/AppStoreServerNotifications/app-store-server-notifications-version-1), the `appAccountToken` value is in [`unified_receipt.Latest_receipt_info`](https://developer.apple.com/documentation/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary).

The `appAccountToken` value may be an empty string if your app doesn’t use app account tokens.

For more information about App Store Server Notifications versions, see [`App Store Server Notifications changelog`](https://developer.apple.com/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog).

## Topics

### Consumption data types
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
- [type refundPreferenceV1](refundpreferencev1.md)
  A value that indicates your preferred outcome for the refund request.
- [type sampleContentProvided](samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.
- [type userStatus](userstatus.md)
  The status of a customer’s account within your app.

## See Also

- [Get Transaction History V1](get-transaction-history-v1.md)
  Get a customer’s in-app purchase transaction history for your app, except finished consumable in-app purchases.
- [Get Refund History V1](get-refund-history-v1.md)
  Get a list of up to 50 of a customer’s refunded in-app purchases for your app.
- [Send Consumption Information V1](send-consumption-information-v1.md)
  Send consumption information about a consumable In-App Purchase or auto-renewable subscription to the App Store after your server receives a consumption request notification.
- [object RefundLookupResponse](refundlookupresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/consumptionrequestv1)*