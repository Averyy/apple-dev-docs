# FamilyTransactionNotSupportedError

**Framework**: App Store Server API  
**Kind**: dictionary

An error that indicates the transaction is for a product the customer obtains through Family Sharing, which the endpoint doesn’t support.

**Availability**:
- App Store Server API 1.16+

## Declaration

```swift
object FamilyTransactionNotSupportedError
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

## See Also

- [object AccountNotFoundError](accountnotfounderror.md)
  An error that indicates the App Store account wasn’t found.
- [object AdvancedCommerceTransactionNotSupportedError](advancedcommercetransactionnotsupportederror.md)
  An error that indicates Advanced Commerce API transactions are not supported by the endpoint.
- [object AppNotFoundError](appnotfounderror.md)
  An error that indicates the app wasn’t found.
- [object AppTransactionDoesNotExistError](apptransactiondoesnotexisterror.md)
  An error response that indicates an app transaction doesn’t exist for the specified customer.
- [object AppTransactionIdNotSupportedError](apptransactionidnotsupportederror.md)
  An error that indicates the endpoint doesn’t support an app transaction ID.
- [object FamilySharedSubscriptionExtensionIneligibleError](familysharedsubscriptionextensionineligibleerror.md)
  An error that indicates a subscription isn’t directly eligible for a renewal date extension because the customer obtained it through Family Sharing.
- [object GeneralInternalError](generalinternalerror.md)
  An error that indicates a general internal error.
- [object GeneralBadRequestError](generalbadrequesterror.md)
  An error that indicates an invalid request.
- [object InvalidAppAccountTokenUUIDError](invalidappaccounttokenuuiderror.md)
  An error that indicates the app account token value is not a valid UUID.
- [object InvalidAppIdentifierError](invalidappidentifiererror.md)
  An error that indicates an invalid app identifier.
- [object InvalidEmptyStorefrontCountryCodeListError](invalidemptystorefrontcountrycodelisterror.md)
  An error that indicates a required storefront country code is empty.
- [object InvalidExtendByDaysError](invalidextendbydayserror.md)
  An error that indicates an invalid extend-by-days value.
- [object InvalidExtendReasonCodeError](invalidextendreasoncodeerror.md)
  An error that indicates an invalid reason code.
- [object InvalidOriginalTransactionIdError](invalidoriginaltransactioniderror.md)
  An error that indicates an invalid original transaction identifier.
- [object InvalidRefundPreferenceError](invalidrefundpreferenceerror.md)
  An error that indicates an invalid refund preference value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/familytransactionnotsupportederror)*