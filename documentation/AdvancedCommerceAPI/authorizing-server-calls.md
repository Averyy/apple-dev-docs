# Authorizing API requests from your server

**Framework**: Advanced Commerce API

Create JSON Web Tokens (JWTs) to authorize Advanced Commerce requests from your server.

#### Discussion

The following Advanced Commerce APIs are endpoints that you call from your server:

- [`Cancel a Subscription`](cancel-a-subscription.md)
- [`Change Subscription Metadata`](change-subscription-metadata.md)
- [`Change Subscription Price`](change-subscription-price.md)
- [`Migrate a Subscription to Advanced Commerce API`](migrate-subscription-to-advanced-commerce-api.md)
- [`Request Transaction Refund`](request-transaction-refund.md)
- [`Revoke Subscription`](revoke-subscription.md)

Calls to the Advanced Commerce API’s endpoints require JSON Web Tokens (JWTs) for authorization; you obtain keys to create the tokens from your organization’s App Store Connect account. See [`Creating API keys to authorize API requests`](https://developer.apple.com/documentation/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests) to create your keys. See [`Generating JSON Web Tokens for API requests`](https://developer.apple.com/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests) to generate tokens using your keys and send API requests.

After you have a complete and signed token, provide the token in the request’s authorization header as a bearer token. Generate a new token for each new API request, or reuse tokens until they expire.

> 💡 **Tip**: The App Store Server Library provides a client that makes it easier to adopt the Advanced Commerce APIs, including creating the JWTs to authorize calls. For more information, see [`Simplifying your implementation by using the App Store Server Library`](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

The App Store Server Library provides a client that makes it easier to adopt the Advanced Commerce APIs, including creating the JWTs to authorize calls. For more information, see [`Simplifying your implementation by using the App Store Server Library`](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

## See Also

- [Identifying rate limits for Advanced Commerce APIs](ratelimits.md)
  Recognize and handle the rate limits that apply to Advanced Commerce API endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/authorizing-server-calls)*