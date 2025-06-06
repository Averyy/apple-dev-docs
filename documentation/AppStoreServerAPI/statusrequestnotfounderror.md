# StatusRequestNotFoundError

**Framework**: App Store Server API  
**Kind**: dictionary

An error that indicates the server didn’t find a subscription-renewal-date extension request for the request identifier and product identifier you provided.

**Availability**:
- App Store Server API 1.8+

## Declaration

```swift
object StatusRequestNotFoundError
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

This error applies to the [`Get Status of Subscription Renewal Date Extensions`](get-status-of-subscription-renewal-date-extensions.md) endpoint. Check that the `productId` and `requestIdentifier` parameters match the values associated with your request to the [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md) endpoint.

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
- [object InvalidEmptyStorefrontCountryCodeListError](invalidemptystorefrontcountrycodelisterror.md)
  An error that indicates a required storefront country code is empty.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/statusrequestnotfounderror)*