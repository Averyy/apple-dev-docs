# FamilySharedSubscriptionExtensionIneligibleError

**Framework**: App Store Server API  
**Kind**: dictionary

An error that indicates a subscription isn’t directly eligible for a renewal date extension because the customer obtained it through Family Sharing.

**Availability**:
- App Store Server API 1.8+

## Declaration

```swift
object FamilySharedSubscriptionExtensionIneligibleError
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

A request returns this error if you call the [`Extend a Subscription Renewal Date`](extend-a-subscription-renewal-date.md) endpoint with an `originalTransactionId` that belongs to a subscription the user obtains through Family Sharing.

When the endpoint extends an eligible purchased subscription that supports Family Sharing, it automatically extends the family members’ subscriptions as well. However, the endpoint doesn’t support requests to extend a family member’s subscription directly.

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
- [object FamilyTransactionNotSupportedError](familytransactionnotsupportederror.md)
  An error that indicates the transaction is for a product the customer obtains through Family Sharing, which the endpoint doesn’t support.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/familysharedsubscriptionextensionineligibleerror)*