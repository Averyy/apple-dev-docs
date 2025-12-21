# Identifying rate limits

**Framework**: Retention Messaging API

Recognize the rate limits that apply to Retention Messaging API endpoints, and handle them in your code.

#### Overview

The Retention Messaging API limits the number of requests that you can submit to each endpoint within a specified timespan. The request limits apply per app.

The following table lists the rate limits for each endpoint in the production environment, expressed in requests per second. The system enforces rate limits on an hourly basis.

| Endpoint | Rate limit (per second) |
| --- | --- |
| [`Configure Default Message`](configure-default-message.md) | 1 |
| [`Delete Default Message`](delete-default-message.md) | 1 |
| [`Upload Image`](upload-image.md) | 1 |
| [`Delete Image`](delete-image.md) | 1 |
| [`Get Image List`](get-image-list.md) | 1 |
| [`Upload Message`](upload-message.md) | 1 |
| [`Delete Message`](delete-message.md) | 1 |
| [`Get Message List`](get-message-list.md) | 1 |
| [`Initiate Performance Test`](initiate-performance-test.md) | 1 |
| [`Get Performance Test Results`](get-performance-test-results.md) | 1 |

The rate limits in the sandbox environment are 10% of the limits in the table above.

The App Store server may make adjustments to reduce or increase these rate limits as needed at any time.

##### Handle Exceeded Rate Limits Gracefully

If you exceed a per-hour limit, the API rejects the request with an `HTTP` `429` response with a [`RateLimitExceededError`](ratelimitexceedederror.md) object in the body.  Consider the following as you integrate the API:

- If you periodically call the API, throttle your requests to avoid exceeding the per-hour limit for an endpoint.
- Manage the `HTTP` `429` `RateLimitExceededError` response in your error-handling process. For example, log the failure and queue the job to process it again at a later time.
- Check the `Retry-After` header if you receive the `HTTP` `429` error. This header contains a UNIX time, in milliseconds, that indicates when you can next send a request.

## See Also

- [Setting up retention messages](setting-up-retention-messages.md)
  Upload images and messages for retention messaging, configure default messages, and complete the setup for promotional-offer and switch-plan messages.
- [Retention Messaging API changelog](retention-messaging-changelog.md)
  Learn about new features and updates in the Retention Messaging API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/identifying-rate-limits)*