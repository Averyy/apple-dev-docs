# TransactionIdNotFoundError

**Framework**: App Store Server API  
**Kind**: dictionary

An error that indicates a transaction identifier wasn’t found.

**Availability**:
- App Store Server API 1.8+

## Declaration

```swift
object TransactionIdNotFoundError
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

Don’t unlock the service or content associated with the transaction ID for the app bundle ID and environment that you indicate in the request unless you successfully resolve this error. To resolve this error, check your request to ensure that:

- The JSON Web Token (JWT) payload contains the bundle ID (`bid`) of your app that’s associated with the transaction ID. For more information, see [`Generating JSON Web Tokens for API requests`](generating-json-web-tokens-for-api-requests.md).
- You’re making the request in the same environment, production or sandbox, that generated the transaction ID.

In rare cases, you might get this error for transaction IDs that previously returned data successfully. Don’t unlock the service or content for the app bundle ID and environment in the request if you’re unable to resolve this error using the steps above.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/transactionidnotfounderror)*