# Identifying rate limits

**Framework**: App Store Server API

Recognize the rate limits that apply to App Store Server API endpoints and handle them in your code.

#### Overview

The App Store Server API limits the number of requests that you can submit to each endpoint within a specified timespan. The request limits apply per app.

The following table lists the rate limits for each endpoint in the production environment, expressed in requests per second. The system enforces rate limits on an hourly basis.

| Endpoint | Rate limit (per second) |
| --- | --- |
| [`Get App Transaction Info`](get-app-transaction-info.md) | 50 |
| [`Get Transaction Info`](get-transaction-info.md) | 50 |
| [`Get Transaction History`](get-transaction-history.md) | 50 |
| [`Get Transaction History V1`](get-transaction-history-v1.md) | 50 |
| [`Get All Subscription Statuses`](get-all-subscription-statuses.md) | 50 |
| [`Send Consumption Information`](send-consumption-information.md) | 50 |
| [`Send Consumption Information V1`](send-consumption-information-v1.md) | 50 |
| [`Get Notification History`](get-notification-history.md) | 50 |
| [`Extend a Subscription Renewal Date`](extend-a-subscription-renewal-date.md) | 20 |
| [`Set App Account Token`](set-app-account-token.md) | 20 |
| [`Look Up Order ID`](look-up-order-id.md) | 10 |
| [`Get Refund History`](get-refund-history.md) | 10 |
| [`Get Refund History V1`](get-refund-history-v1.md) | 10 |
| [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md) | 1 |
| [`Request a Test Notification`](request-a-test-notification.md) | 1 |
| [`Get Test Notification Status`](get-test-notification-status.md) | 1 |

The rate limits in the sandbox environment are 10% of the limits in the table above.

The App Store server may make adjustments to reduce or increase these rate limits as needed at any time.

##### Handle Exceeded Rate Limits Gracefully

If you exceed a per-hour limit, the API rejects the request with an `HTTP` `429` response, with a [`RateLimitExceededError`](ratelimitexceedederror.md) in the body.  Consider the following as you integrate the API:

- If you periodically call the API, throttle your requests to avoid exceeding the per-hour limit for an endpoint.
- Manage the `HTTP` `429` [`RateLimitExceededError`](ratelimitexceedederror.md) in your error-handling process. For example, log the failure and queue the job to process it again at a later time.
- Check the `Retry-After` header if you receive the `HTTP` `429` error. This header contains a UNIX time, in milliseconds, that informs you when you can next send a request.

## See Also

- [Simplifying your implementation by using the App Store Server Library](simplifying-your-implementation-by-using-the-app-store-server-library.md)
  Use Apple’s open source library to create JSON Web Tokens (JWT) to authorize your calls, verify transactions, extract transaction identifiers from receipts, and more.
- [Creating API keys to authorize API requests](creating-api-keys-to-authorize-api-requests.md)
  Create API keys you use to sign JSON Web Tokens and authorize API requests.
- [Generating JSON Web Tokens for API requests](generating-json-web-tokens-for-api-requests.md)
  Create JSON Web Tokens signed with your private key to authorize requests for App Store Server API and External Purchase Server API.
- [App Store Server API changelog](app-store-server-api-changelog.md)
  Learn about new features and updates in the App Store Server API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/identifying-rate-limits)*