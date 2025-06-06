# InvalidTransactionTypeNotSupportedError

**Framework**: App Store Server API  
**Kind**: dictionary

An error that indicates the transaction identifier represents an unsupported In-App Purchase type.

**Availability**:
- App Store Server API 1.11+

## Declaration

```swift
object InvalidTransactionTypeNotSupportedError
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The [`Send Consumption Information`](send-consumption-information.md) endpoint returns this error if the `transactionId` doesn’t represent a supported in-app purchase. Be sure to provide the same `transactionId` that you receive to your [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint in a notification with a `CONSUMPTION_REQUEST` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType).

## See Also

- [object InvalidAccountTenureError](invalidaccounttenureerror.md)
  An error that indicates the value of the account tenure field is invalid.
- [object InvalidAppAccountTokenError](invalidappaccounttokenerror.md)
  An error that indicates the value of the app account token field is invalid.
- [object InvalidConsumptionStatusError](invalidconsumptionstatuserror.md)
  An error that indicates the value of the consumption status field is invalid.
- [object InvalidCustomerConsentedError](invalidcustomerconsentederror.md)
  An error that indicates the customer consented field is invalid or doesn’t indicate that the customer consented.
- [object InvalidDeliveryStatusError](invaliddeliverystatuserror.md)
  An error that indicates the value in the delivery status field is invalid.
- [object InvalidLifetimeDollarsPurchasedError](invalidlifetimedollarspurchasederror.md)
  An error that indicates the value in the lifetime dollars purchased field is invalid.
- [object InvalidLifetimeDollarsRefundedError](invalidlifetimedollarsrefundederror.md)
  An error that indicates the value in the lifetime dollars refunded field is invalid.
- [object InvalidPlatformError](invalidplatformerror.md)
  An error that indicates the value in the platform field is invalid.
- [object InvalidPlayTimeError](invalidplaytimeerror.md)
  An error that indicates the value in the playtime field is invalid.
- [object InvalidSampleContentProvidedError](invalidsamplecontentprovidederror.md)
  An error that indicates the value in the sample content provided field is invalid.
- [object InvalidUserStatusError](invaliduserstatuserror.md)
  An error that indicates the value in the user status field is invalid.
- [object InvalidTransactionNotConsumableError](invalidtransactionnotconsumableerror.md)
  An error that indicates the transaction identifier doesn’t represent a consumable In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/invalidtransactiontypenotsupportederror)*