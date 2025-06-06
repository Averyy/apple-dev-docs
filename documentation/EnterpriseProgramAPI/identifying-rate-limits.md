# Identifying Rate Limits

**Framework**: Enterprise Program API

Recognize the rate limits that REST API responses provide and handle them in your code.

#### Overview

The Enterprise Program API limits the volume of requests that you can submit within a specified timeframe. The limits apply to requests you send using the same API key.

##### Identify Limits Provided in the Http Header

The API presents rate limits to users in an HTTP header. Every response from the API includes an `X-Rate-Limit` HTTP header. Its value has the form:

```other
user-hour-lim:3500;user-hour-rem:500;
```

The header info includes:

- `user-hour-lim`, which indicates the number of requests you can make per hour with the same API key.
- `user-hour-rem`, which shows the number of requests remaining.

In this example, you are limited to 3500 requests per hour, with 500 remaining. Actual limits can vary.

The time frame is a “rolling hour.” At any moment, the `user-hour-rem` value is your per-hour limit, minus the total requests you’ve made in the previous 60 minutes.

##### Interpret the Error Response

If you exceed a per-hour limit, the API rejects requests with an HTTP 429 response, with the `RATE_LIMIT_EXCEEDED` error code. See [`About the HTTP Status Code`](about-the-http-status-code.md) for more information.

##### Handle Exceeded Limits Gracefully

Consider rate limits as you integrate the API:

- If you periodically call the API to check a value, throttle your requests to avoid exceeding the per-hour limit for that endpoint.
- Manage the HTTP 429 `RATE_LIMIT_EXCEEDED` error in your error-handling process. For example, log the failure and queue the job to be processed again at a later time.

## See Also

- [Creating API Keys for Enterprise Program API](creating-api-keys-for-enterprise-program-api.md)
  Create API keys to sign JSON Web Tokens (JWTs) and authorize API requests.
- [Generating Tokens for API Requests](generating-tokens-for-api-requests.md)
  Create JSON Web Tokens (JWTs) signed with your private key to authorize API requests.
- [Revoking API Keys](revoking-api-keys.md)
  Revoke unused, lost, or compromised private keys.
- [Enterprise Program API Release Notes](enterprise-api-release-notes.md)
  Learn about new features and updates in the Enterprise Program API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/identifying-rate-limits)*