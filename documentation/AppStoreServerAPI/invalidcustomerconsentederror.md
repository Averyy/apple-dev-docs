# InvalidCustomerConsentedError

**Framework**: App Store Server API  
**Kind**: dictionary

An error that indicates the customer consented field is invalid or doesn’t indicate that the customer consented.

**Availability**:
- App Store Server API 1.9+

## Declaration

```swift
object InvalidCustomerConsentedError
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

If the `customerConsented` field in a [`ConsumptionRequest`](consumptionrequest.md) is any value other than `true`, the App Store server rejects the request. For more information, see [`customerConsented`](customerconsented.md).

## See Also

- [object InvalidAccountTenureError](invalidaccounttenureerror.md)
  An error that indicates the value of the account tenure field is invalid.
- [object InvalidAppAccountTokenError](invalidappaccounttokenerror.md)
  An error that indicates the value of the app account token field is invalid.
- [object InvalidConsumptionStatusError](invalidconsumptionstatuserror.md)
  An error that indicates the value of the consumption status field is invalid.
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
- [object InvalidTransactionTypeNotSupportedError](invalidtransactiontypenotsupportederror.md)
  An error that indicates the transaction identifier represents an unsupported In-App Purchase type.
- [object InvalidUserStatusError](invaliduserstatuserror.md)
  An error that indicates the value in the user status field is invalid.
- [object InvalidTransactionNotConsumableError](invalidtransactionnotconsumableerror.md)
  An error that indicates the transaction identifier doesn’t represent a consumable In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/invalidcustomerconsentederror)*