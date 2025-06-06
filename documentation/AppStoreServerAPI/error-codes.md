# Error codes

**Framework**: App Store Server API

Understand the error codes that App Store Server API responses return.

## Topics

### Errors
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
- [object InvalidStatusError](invalidstatuserror.md)
  An error that indicates the status parameter is invalid.
- [object InvalidStorefrontCountryCodeError](invalidstorefrontcountrycodeerror.md)
  An error that indicates a storefront code is invalid.
- [object InvalidTransactionIdError](invalidtransactioniderror.md)
  An error that indicates an invalid transaction identifier.
- [object OriginalTransactionIdNotFoundError](originaltransactionidnotfounderror.md)
  An error that indicates an original transaction identifier wasn’t found.
- [object RateLimitExceededError](ratelimitexceedederror.md)
  An error that indicates the request exceeded the rate limit.
- [object StatusRequestNotFoundError](statusrequestnotfounderror.md)
  An error that indicates the server didn’t find a subscription-renewal-date extension request for the request identifier and product identifier you provided.
- [object SubscriptionExtensionIneligibleError](subscriptionextensionineligibleerror.md)
  An error that indicates the subscription doesn’t qualify for a renewal-date extension due to its subscription state.
- [object SubscriptionMaxExtensionError](subscriptionmaxextensionerror.md)
  An error that indicates the subscription doesn’t qualify for a renewal-date extension because it has already received the maximum extensions.
- [object TransactionIdNotFoundError](transactionidnotfounderror.md)
  An error that indicates a transaction identifier wasn’t found.
### Errors to retry
- [object AccountNotFoundRetryableError](accountnotfoundretryableerror.md)
  An error response that indicates the App Store account wasn’t found, but you can try again.
- [object AppNotFoundRetryableError](appnotfoundretryableerror.md)
  An error response that indicates the app wasn’t found, but you can try again.
- [object GeneralInternalRetryableError](generalinternalretryableerror.md)
  An error response that indicates an unknown error occurred, but you can try again.
- [object OriginalTransactionIdNotFoundRetryableError](originaltransactionidnotfoundretryableerror.md)
  An error response that indicates the original transaction identifier wasn’t found, but you can try again.
### Consumption request errors
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
- [object InvalidTransactionTypeNotSupportedError](invalidtransactiontypenotsupportederror.md)
  An error that indicates the transaction identifier represents an unsupported In-App Purchase type.
- [object InvalidUserStatusError](invaliduserstatuserror.md)
  An error that indicates the value in the user status field is invalid.
- [object InvalidTransactionNotConsumableError](invalidtransactionnotconsumableerror.md)
  An error that indicates the transaction identifier doesn’t represent a consumable In-App Purchase.
### Notification test and history errors
- [object InvalidEndDateError](invalidenddateerror.md)
  An error that indicates the end date is invalid.
- [object InvalidNotificationTypeError](invalidnotificationtypeerror.md)
  An error that indicates the notification type or subtype is invalid.
- [object InvalidPaginationTokenError](invalidpaginationtokenerror.md)
  An error that indicates the pagination token is invalid.
- [object InvalidStartDateError](invalidstartdateerror.md)
  An error that indicates the start date is invalid.
- [object InvalidTestNotificationTokenError](invalidtestnotificationtokenerror.md)
  An error that indicates the test notification token is invalid.
- [object InvalidInAppOwnershipTypeError](invalidinappownershiptypeerror.md)
  An error that indicates an invalid in-app ownership type parameter.
- [object InvalidProductIdError](invalidproductiderror.md)
  An error that indicates the product ID parameter is invalid.
- [object InvalidProductTypeError](invalidproducttypeerror.md)
  An error that indicates the product type parameter is invalid.
- [object InvalidSortError](invalidsorterror.md)
  An error that indicates the sort parameter is invalid.
- [object InvalidSubscriptionGroupIdentifierError](invalidsubscriptiongroupidentifiererror.md)
  An error that indicates the subscription group identifier is invalid.
- [object MultipleFiltersSuppliedError](multiplefilterssuppliederror.md)
  An error that indicates the request is invalid because it has too many applied constraints.
- [object PaginationTokenExpiredError](paginationtokenexpirederror.md)
  An error that indicates the pagination token expired.
- [object ServerNotificationURLNotFoundError](servernotificationurlnotfounderror.md)
  An error that indicates the App Store server couldn’t find a notifications URL for your app in the environment.
- [object StartDateAfterEndDateError](startdateafterenddateerror.md)
  An error that indicates the end date precedes the start date, or the two dates are equal.
- [object StartDateTooFarInPastError](startdatetoofarinpasterror.md)
  An error that indicates the start date is earlier than the earliest allowed date.
- [object TestNotificationNotFoundError](testnotificationnotfounderror.md)
  An error that indicates the test notification token is expired or the test notification status isn’t available.
- [object InvalidExcludeRevokedError](invalidexcluderevokederror.md)
  An error that indicates the query parameter exclude-revoked is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/error-codes)*