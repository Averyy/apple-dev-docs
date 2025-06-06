# App Store Server API changelog

**Framework**: App Store Server API

Learn about new features and updates in the App Store Server API.

#### Overview

Use this changelog to learn about feature updates, deprecations, and removals for the App Store Server API.

##### 115 20250221

- Updated the [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) and [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) to include the new [`appTransactionId`](apptransactionid.md) and [`offerPeriod`](offerperiod.md) fields.
- Updated the [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) to include the [`appAccountToken`](appaccounttoken.md) field.
- Added the [`AppTransactionIdNotSupportedError`](apptransactionidnotsupportederror.md) error object.

##### 114 20250117

- Added support for Advanced Commerce API.

##### 113 20240708

- Updated the [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) to include the new [`eligibleWinBackOfferIds`](eligiblewinbackofferids.md) field.
- Added the win-back offer type in [`offerType`](offertype.md).

##### 112 20240610

- Added the endpoint [`Get Transaction History`](get-transaction-history.md), which provides transaction history for all In-App Purchases, including consumable In-App Purchases in a finished state.
- Added the fields [`renewalPrice`](renewalprice.md), [`currency`](currency.md) and [`offerDiscountType`](offerdiscounttype.md) to the [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md).

- The [`Get Transaction History V1`](get-transaction-history-v1.md) endpoint is deprecated. Use the new [`Get Transaction History`](get-transaction-history.md) endpoint instead.

##### 111 20240411

New features

- Added the [`refundPreference`](refundpreference.md) field to the  [`ConsumptionRequest`](consumptionrequest.md) request body.
- [`Send Consumption Information`](send-consumption-information.md) added  support for receiving information for auto-renewable subscriptions.
- Added the [`InvalidTransactionTypeNotSupportedError`](invalidtransactiontypenotsupportederror.md) error object.

- The system no longer sends the [`InvalidTransactionNotConsumableError`](invalidtransactionnotconsumableerror.md) error object. It uses [`InvalidTransactionTypeNotSupportedError`](invalidtransactiontypenotsupportederror.md) instead.

##### 1101 20240312

- The type of the [`price`](https://developer.apple.com/documentation/AppStoreServerNotifications/price) field changed from `int32` to `int64`.

##### Server Update 20240229

- The [`Get Notification History`](get-notification-history.md) endpoint adds support for the new notification type for unreported external purchase tokens.

##### 110 20231026

New features

- Added the following new properties in the decoded transaction payload [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md): [`price`](price.md), [`currency`](currency.md), and [`offerDiscountType`](offerdiscounttype.md).

##### 19 20230927

New features

- Updated the error format of the [`Send Consumption Information`](send-consumption-information.md) endpoint to match that of other endpoints. The endpoint now returns a JSON body that can contain an error code.
- New error codes for the [`Send Consumption Information`](send-consumption-information.md) endpoint include: [`InvalidAccountTenureError`](invalidaccounttenureerror.md), [`InvalidAppAccountTokenError`](invalidappaccounttokenerror.md), [`InvalidConsumptionStatusError`](invalidconsumptionstatuserror.md), [`InvalidCustomerConsentedError`](invalidcustomerconsentederror.md), [`InvalidDeliveryStatusError`](invaliddeliverystatuserror.md), [`InvalidLifetimeDollarsPurchasedError`](invalidlifetimedollarspurchasederror.md), [`InvalidLifetimeDollarsRefundedError`](invalidlifetimedollarsrefundederror.md), [`InvalidPlatformError`](invalidplatformerror.md), [`InvalidPlayTimeError`](invalidplaytimeerror.md), [`InvalidSampleContentProvidedError`](invalidsamplecontentprovidederror.md), [`InvalidTransactionNotConsumableError`](invalidtransactionnotconsumableerror.md), [`InvalidUserStatusError`](invaliduserstatuserror.md).

##### 18 20230605

New features

- Added a new endpoint [`Get Transaction Info`](get-transaction-info.md) with its response  [`TransactionInfoResponse`](transactioninforesponse.md), which provides information about a single transaction.
- The [`Get Notification History`](get-notification-history.md) endpoint adds a new filter parameter, [`onlyFailures`](onlyfailures.md). When you set it to `true`, the endpoint returns only the notifications that failed to reach the developer’s server.
- The following endpoints changed their path parameters from [`originalTransactionId`](originaltransactionid.md) to [`transactionId`](transactionid.md): [`Get All Subscription Statuses`](get-all-subscription-statuses.md), [`Get Transaction History V1`](get-transaction-history-v1.md), [`Get Refund History`](get-refund-history.md), and [`Send Consumption Information`](send-consumption-information.md). These endpoints now accept any transaction identifier, including original transaction identifiers.
- The [`Get Notification History`](get-notification-history.md) endpoint now accepts a [`transactionId`](transactionid.md) instead of requiring an original transaction identifier ([`originalTransactionId`](originaltransactionid.md)) in the [`NotificationHistoryRequest`](notificationhistoryrequest.md) body.
- The [`Get Transaction History V1`](get-transaction-history-v1.md) endpoint adds a new filter parameter, `revoked`, that filters the response to return only revoked transactions or only nonrevoked transactions.
- The [`Get All Subscription Statuses`](get-all-subscription-statuses.md) endpoint adds a new filter parameter, `status`, that enables you to request subscriptions with the status values you specify.
- Added the [`storefront`](storefront.md), [`storefrontId`](storefrontid.md), and [`transactionReason`](transactionreason.md) fields to the [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) object.
- Added the [`renewalDate`](renewaldate.md) field to the  [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) object.
- Added the `sendAttempts` field to the  [`CheckTestNotificationResponse`](checktestnotificationresponse.md) and the [`notificationHistoryResponseItem`](notificationhistoryresponseitem.md) of the [`NotificationHistoryResponse`](notificationhistoryresponse.md) to provide information about all the send attempts for App Store Server Notifications.
- Added the error codes [`FamilySharedSubscriptionExtensionIneligibleError`](familysharedsubscriptionextensionineligibleerror.md), [`StatusRequestNotFoundError`](statusrequestnotfounderror.md), [`InvalidStatusError`](invalidstatuserror.md), [`InvalidRevokedError`](invalidrevokederror.md), [`InvalidTransactionIdError`](invalidtransactioniderror.md), [`TransactionIdNotFoundError`](transactionidnotfounderror.md),  and [`RateLimitExceededError`](ratelimitexceedederror.md).
- All endpoints are subject to a rate limit and can return a [`RateLimitExceededError`](ratelimitexceedederror.md) with an HTTP 429 error code. For more information, see [`Identifying rate limits`](identifying-rate-limits.md).

- The `excludeRevoked` filter in [`Get Transaction History V1`](get-transaction-history-v1.md) is deprecated. Use the new `revoked` filter instead.
- The `firstSendAttemptResult` field is deprecated in the [`CheckTestNotificationResponse`](checktestnotificationresponse.md) and [`notificationHistoryResponseItem`](notificationhistoryresponseitem.md) objects. Use the first [`sendAttemptItem`](sendattemptitem.md) in the `sendAttempts` array instead.

##### 17 20230130

New features

- The new endpoint [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md) takes a subscription product identifier and extends the renewal date for all eligible subscribers. It responds with [`MassExtendRenewalDateResponse`](massextendrenewaldateresponse.md). For more information, see [`Extending the renewal date for auto-renewable subscriptions`](extending-the-renewal-date-for-auto-renewable-subscriptions.md). For information about new App Store server notifications related to this endpoint, see the [`App Store Server Notifications changelog`](https://developer.apple.com/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog).
- The new endpoint [`Get Status of Subscription Renewal Date Extensions`](get-status-of-subscription-renewal-date-extensions.md) checks the status of a subscription-renewal-date extension, and responds with the [`MassExtendRenewalDateStatusResponse`](massextendrenewaldatestatusresponse.md).

##### 16 20220808

New features

- The new version 2 endpoint [`Get Refund History`](get-refund-history.md) returns a paginated list of refunded transactions in the [`RefundHistoryResponse`](refundhistoryresponse.md).

Deprecations

- The endpoint [`Get Refund History V1`](get-refund-history-v1.md) and its response [`RefundLookupResponse`](refundlookupresponse.md) are deprecated.
- In `firstSendAttemptResult`, the `SSL_ISSUE` value is deprecated and replaced with `TLS_ISSUE`.

##### 15 20220606

New features

- The API has two new endpoints to support testing how your server receives App Store Server Notifications. The endpoints are: [`Request a Test Notification`](request-a-test-notification.md) and [`Get Test Notification Status`](get-test-notification-status.md).
- The API adds the new [`Get Notification History`](get-notification-history.md) endpoint.
- The [`Get Transaction History V1`](get-transaction-history-v1.md) endpoint is enhanced with new parameters to support filtering and sorting functionality.
- The [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) now includes the [`recentSubscriptionStartDate`](recentsubscriptionstartdate.md) field.

##### 14

This version doesn’t contain any public changes.

##### 13

This version doesn’t contain any public changes.

##### Server Update 20220317

Removals

- The [`JWSDecodedHeader`](jwsdecodedheader.md) object no longer includes the `kid` field.

##### 12 20220224

New features

- The [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) and [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) objects now include the [`environment`](environment.md) field.

##### Server Update 20220223

- The [`Get Refund History V1`](get-refund-history-v1.md) endpoint now returns a maximum of 50 refunded transactions.

##### 11 20221021

New features

- The API adds three endpoints: [`Look Up Order ID`](look-up-order-id.md), [`Get Refund History V1`](get-refund-history-v1.md), and [`Extend a Subscription Renewal Date`](extend-a-subscription-renewal-date.md).

##### Server Update 20210920

The API is now available in the production environment, using the following base URL:

```other
https://api.storekit.itunes.apple.com/inApps/
```

##### 10b1 20210607

Initial version of the App Store Server API.

New features

- This API has three endpoints, available in the sandbox environment: [`Get Transaction History V1`](get-transaction-history-v1.md), [`Send Consumption Information`](send-consumption-information.md), and [`Get All Subscription Statuses`](get-all-subscription-statuses.md).

## See Also

- [Simplifying your implementation by using the App Store Server Library](simplifying-your-implementation-by-using-the-app-store-server-library.md)
  Use Apple’s open source library to create JSON Web Tokens (JWT) to authorize your calls, verify transactions, extract transaction identifiers from receipts, and more.
- [Creating API keys to authorize API requests](creating-api-keys-to-authorize-api-requests.md)
  Create API keys you use to sign JSON Web Tokens and authorize API requests.
- [Generating JSON Web Tokens for API requests](generating-json-web-tokens-for-api-requests.md)
  Create JSON Web Tokens signed with your private key to authorize requests for App Store Server API and External Purchase Server API.
- [Identifying rate limits](identifying-rate-limits.md)
  Recognize the rate limits that apply to App Store Server API endpoints and handle them in your code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/app-store-server-api-changelog)*