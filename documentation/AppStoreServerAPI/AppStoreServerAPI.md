# App Store Server API

**Framework**: App Store Server API  
**Kind**: module

Manage your customers’ App Store transactions from your server.

**Availability**:
- App Store Server API 1.0+

## Mentions

- [Generating JSON Web Tokens for API requests](generating-json-web-tokens-for-api-requests.md)
- [Simplifying your implementation by using the App Store Server Library](simplifying-your-implementation-by-using-the-app-store-server-library.md)
- [Creating API keys to authorize API requests](creating-api-keys-to-authorize-api-requests.md)

#### Overview

The App Store Server API is a REST API that you call from your server to request and provide information about your customers’ in-app purchases. The App Store signs the transaction and subscription renewal information that this API returns using the [`JSON Web Signature (JWS)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification. Most endpoints return data for a single customer of your app, indicated by a transaction identifier that you provide.

The App Store Server API is independent of the app’s installation status on the customers’ devices. The App Store server returns information based on a customer’s in-app purchase history regardless of whether the customer installs, removes, or reinstalls the app on their devices.

This API provides the following functionality:

-  Get information for single transactions by calling [`Get Transaction Info`](get-transaction-info.md) or a customer’s entire transaction history using [`Get Transaction History`](get-transaction-history.md). Call [`Get All Subscription Statuses`](get-all-subscription-statuses.md) for up-to-date subscription status. Use this information to keep your customers’ purchase information current on your server.
-  Call [`Get Refund History`](get-refund-history.md) to get a customer’s refund history. Use the [`Send Consumption Information`](send-consumption-information.md) endpoint to send information to the App Store when customers request a refund for a consumable in-app purchase, after you receive the `CONSUMPTION_REQUEST` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) from [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2). Your data helps inform refund decisions.
-  Call [`Get Notification History`](get-notification-history.md) to request the notifications your server may have missed in the past 180 days. Call [`Request a Test Notification`](request-a-test-notification.md) and [`Get Test Notification Status`](get-test-notification-status.md) to test if your server is successfully receiving notifications at its [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint.
-  Call [`Extend a Subscription Renewal Date`](extend-a-subscription-renewal-date.md) and related endpoints to compensate your customers for temporary service outages, canceled events, or interruptions to live-streamed events by extending the renewal date of their paid, active subscription. For more information, see [`Extending the renewal date for auto-renewable subscriptions`](extending-the-renewal-date-for-auto-renewable-subscriptions.md).
-  Call [`Look Up Order ID`](look-up-order-id.md) to get in-app purchase information based on a customer’s order ID, found on the App Store receipt that customers receive in email.

Your server must support the Transport Layer Security (TLS) protocol 1.2 or later to use the App Store Server API.

Check the [`App Store Server API changelog`](app-store-server-api-changelog.md) to learn about the latest changes to this API. Look for videos about the App Store Server API on the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/videos/all-videos/?q=%22App%20Store%20Server%20API%22).

##### Authorize Your Api Calls

Calls to the API require JSON Web Tokens (JWTs) for authorization; you obtain keys to create the tokens from your organization’s App Store Connect account. See [`Creating API keys to authorize API requests`](creating-api-keys-to-authorize-api-requests.md) to create your keys. See [`Generating JSON Web Tokens for API requests`](generating-json-web-tokens-for-api-requests.md) to generate tokens using your keys, and send API requests.

After you have a complete and signed token, provide the token in the request’s authorization header as a bearer token. Generate a new token for each new API request, or reuse tokens until they expire.

##### Create Jwts Verify Transactions and More Using the App Store Server Library

The App Store Server Library is an open source library from Apple, available in four languages. It provides a client that make it easier to adopt the App Store Server APIs, including creating the JWTs to authorize calls. For more information, see [`Simplifying your implementation by using the App Store Server Library`](simplifying-your-implementation-by-using-the-app-store-server-library.md) and the WWDC23 session [`Meet the App Store Server Library`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10143/).

##### Test Using the Sandbox Environment

All App Store Server API endpoints are available for testing in the sandbox environment, except [`Look Up Order ID`](look-up-order-id.md). Access the sandbox environment by sending requests to the endpoints using the following base URL:

```other
https://api.storekit-sandbox.itunes.apple.com/
```

For example, to call [`Get Transaction History`](get-transaction-history.md) in the sandbox environment, send a request using the sandbox URL:

```other
https://api.storekit-sandbox.itunes.apple.com/inApps/v2/history/{transactionId}
```

Note that `/inApps` in the path is case-sensitive.

For endpoints that take a [`transactionId`](transactionid.md) as a parameter, be sure to call the endpoint using the same environment that creates the transaction identifier. Environment information is present in the [`environment`](environment.md) property of the [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md).

If you don’t have environment information, follow these steps:

1. Call the endpoint using the production URL. If the call succeeds, the transaction identifier belongs to the production environment.
2. If you receive an error code `4040010` [`TransactionIdNotFoundError`](transactionidnotfounderror.md), call the endpoint using the sandbox environment.
3. If the call succeeds, the transaction identifier belongs to the sandbox environment. If the call fails with the `4040010` error code, the transaction identifier isn’t present in either environment.

## Topics

### Essentials
- [Simplifying your implementation by using the App Store Server Library](simplifying-your-implementation-by-using-the-app-store-server-library.md)
  Use Apple’s open source library to create JSON Web Tokens (JWT) to authorize your calls, verify transactions, extract transaction identifiers from receipts, and more.
- [Creating API keys to authorize API requests](creating-api-keys-to-authorize-api-requests.md)
  Create API keys you use to sign JSON Web Tokens and authorize API requests.
- [Generating JSON Web Tokens for API requests](generating-json-web-tokens-for-api-requests.md)
  Create JSON Web Tokens signed with your private key to authorize requests for App Store Server API and External Purchase Server API.
- [Identifying rate limits](identifying-rate-limits.md)
  Recognize the rate limits that apply to App Store Server API endpoints and handle them in your code.
- [App Store Server API changelog](app-store-server-api-changelog.md)
  Learn about new features and updates in the App Store Server API.
### In-app purchase history
- [Get Transaction History](get-transaction-history.md)
  Get a customer’s in-app purchase transaction history for your app.
- [object HistoryResponse](historyresponse.md)
  A response that contains the customer’s transaction history for an app.
- [Get Transaction History V1](get-transaction-history-v1.md)
  Get a customer’s in-app purchase transaction history for your app, except finished consumable in-app purchases.
### Transaction information
- [Get Transaction Info](get-transaction-info.md)
  Get information about a single transaction for your app.
- [object TransactionInfoResponse](transactioninforesponse.md)
  A response that contains signed transaction information for a single transaction.
### Subscription status
- [Get All Subscription Statuses](get-all-subscription-statuses.md)
  Get the statuses for all of a customer’s auto-renewable subscriptions in your app.
- [object StatusResponse](statusresponse.md)
  A response that contains status information for all of a customer’s auto-renewable subscriptions in your app.
### App Account Token
- [Set App Account Token](set-app-account-token.md)
  Sets the app account token value for a purchase the customer makes outside of your app, or updates its value in an existing transaction.
- [object UpdateAppAccountTokenRequest](updateappaccounttokenrequest.md)
  The request body that contains an app account token value.
### Consumption information
- [Send Consumption Information](send-consumption-information.md)
  Send consumption information about a consumable in-app purchase or auto-renewable subscription to the App Store after your server receives a consumption request notification.
- [object ConsumptionRequest](consumptionrequest.md)
  The request body containing consumption information.
### Order ID lookup
- [Look Up Order ID](look-up-order-id.md)
  Get a customer’s in-app purchases from a receipt using the order ID.
- [type orderId](orderid.md)
  The customer’s order ID from an App Store receipt for in-app purchases.
- [object OrderLookupResponse](orderlookupresponse.md)
  A response that includes the order lookup status and an array of signed transactions for the in-app purchases in the order.
### Refund lookup
- [Get Refund History](get-refund-history.md)
  Get a paginated list of all of a customer’s refunded in-app purchases for your app.
- [object RefundHistoryResponse](refundhistoryresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) refunded transactions, and paging information.
- [Get Refund History V1](get-refund-history-v1.md)
  Get a list of up to 50 of a customer’s refunded in-app purchases for your app.
- [object RefundLookupResponse](refundlookupresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) transactions.
### Subscription-renewal-date extension
- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)
  Compensate eligible active subscribers for service interruptions by extending a subscription’s renewal date.
- [Extend a Subscription Renewal Date](extend-a-subscription-renewal-date.md)
  Extends the renewal date of a customer’s active subscription using the original transaction identifier.
- [Extend Subscription Renewal Dates for All Active Subscribers](extend-subscription-renewal-dates-for-all-active-subscribers.md)
  Uses a subscription’s product identifier to extend the renewal date for all of its eligible active subscribers.
- [Get Status of Subscription Renewal Date Extensions](get-status-of-subscription-renewal-date-extensions.md)
  Checks whether a renewal date extension request completed, and provides the final count of successful or failed extensions.
- [object ExtendRenewalDateRequest](extendrenewaldaterequest.md)
  The request body that contains subscription-renewal-extension data for an individual subscription.
- [object ExtendRenewalDateResponse](extendrenewaldateresponse.md)
  A response that indicates whether an individual renewal-date extension succeeded, and related details.
- [object MassExtendRenewalDateRequest](massextendrenewaldaterequest.md)
  The request body that contains subscription-renewal-extension data to apply for all eligible active subscribers.
- [object MassExtendRenewalDateResponse](massextendrenewaldateresponse.md)
  A response that indicates the server successfully received the subscription-renewal-date extension request.
- [object MassExtendRenewalDateStatusResponse](massextendrenewaldatestatusresponse.md)
  A response that indicates the current status of a request to extend the subscription renewal date to all eligible subscribers.
### App Store Server Notifications history
- [Get Notification History](get-notification-history.md)
  Get a list of notifications that the App Store server attempted to send to your server.
- [object NotificationHistoryRequest](notificationhistoryrequest.md)
  The request body for notification history.
- [object NotificationHistoryResponse](notificationhistoryresponse.md)
  A response that contains the App Store Server Notifications history for your app.
- [object notificationHistoryResponseItem](notificationhistoryresponseitem.md)
  The App Store server notification history record, including the signed notification payload and the result of the server’s first send attempt.
### App Store Server Notifications testing
- [Request a Test Notification](request-a-test-notification.md)
  Ask App Store Server Notifications to send a test notification to your server.
- [Get Test Notification Status](get-test-notification-status.md)
  Check the status of the test App Store server notification sent to your server.
- [object SendTestNotificationResponse](sendtestnotificationresponse.md)
  A response that contains the test notification token.
- [object CheckTestNotificationResponse](checktestnotificationresponse.md)
  A response that contains the contents of the App Store server’s test notification and the result from your server.
### JWS headers and payloads
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [type JWSRenewalInfo](jwsrenewalinfo.md)
  Subscription renewal information, signed by the App Store, in JSON Web Signature (JWS) format.
- [object JWSDecodedHeader](jwsdecodedheader.md)
  A decoded JSON Web Signature (JWS) header containing transaction or renewal information.
- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.
- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [Data types](data-types.md)
  Refer to these data types for decoded transaction and renewal information payloads.
### Error information
- [Error codes](error-codes.md)
  Understand the error codes that App Store Server API responses return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreServerAPI)*