# InvalidEmptyStorefrontCountryCodeListError

**Framework**: App Store Server API  
**Kind**: dictionary

An error that indicates a required storefront country code is empty.

**Availability**:
- App Store Server API 1.7+

## Declaration

```swift
object InvalidEmptyStorefrontCountryCodeListError
```

#### Discussion

This error applies to the [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md) endpoint. If your request applies to all storefronts, omit the `storefrontCountryCodes` list from the [`MassExtendRenewalDateRequest`](massextendrenewaldaterequest.md) object.

## See Also

- [object AccountNotFoundError](accountnotfounderror.md)
  An error that indicates the App Store account wasn’t found.
- [object AppNotFoundError](appnotfounderror.md)
  An error that indicates the app wasn’t found.
- [object AppTransactionIdNotSupportedError](apptransactionidnotsupportederror.md)
  An error that indicates the endpoint doesn’t support an app transaction ID.
- [object FamilySharedSubscriptionExtensionIneligibleError](familysharedsubscriptionextensionineligibleerror.md)
  An error that indicates a subscription isn’t directly eligible for a renewal date extension because the customer obtained it through Family Sharing.
- [object GeneralInternalError](generalinternalerror.md)
  An error that indicates a general internal error.
- [object GeneralBadRequestError](generalbadrequesterror.md)
  An error that indicates an invalid request.
- [object InvalidAppIdentifierError](invalidappidentifiererror.md)
  An error that indicates an invalid app identifier.
- [object InvalidExtendByDaysError](invalidextendbydayserror.md)
  An error that indicates an invalid extend-by-days value.
- [object InvalidExtendReasonCodeError](invalidextendreasoncodeerror.md)
  An error that indicates an invalid reason code.
- [object InvalidOriginalTransactionIdError](invalidoriginaltransactioniderror.md)
  An error that indicates an invalid original transaction identifier.
- [object InvalidRefundPreferenceError](invalidrefundpreferenceerror.md)
  An error that indicates an invalid refund preference code.
- [object InvalidRequestIdentifierError](invalidrequestidentifiererror.md)
  An error that indicates an invalid request identifier.
- [object InvalidRequestRevisionError](invalidrequestrevisionerror.md)
  An error that indicates an invalid request revision.
- [object InvalidRevokedError](invalidrevokederror.md)
  An error that indicates the revoked parameter contains an invalid value.
- [object InvalidStatusError](invalidstatuserror.md)
  An error that indicates the status parameter is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/invalidemptystorefrontcountrycodelisterror)*