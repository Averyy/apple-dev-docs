# Simplifying your implementation by using the App Store Server Library

**Framework**: App Store Server API

Use Apple’s open source library to create JSON Web Tokens (JWT) to authorize your calls, verify transactions, extract transaction identifiers from receipts, and more.

#### Overview

The App Store Server Library is an open source library from Apple, available in four languages. It makes adopting the [`App Store Server API`](AppStoreServerAPI.md) and working with JSON Web Signature (JWS) transactions easier. Find the App Store Server Library for each language in the following GitHub repositories:

- Swift: [`App Store Server Swift Library`](https://developer.apple.comhttps://github.com/apple/app-store-server-library-swift)
- Java: [`App Store Server Java Library`](https://developer.apple.comhttps://github.com/apple/app-store-server-library-java)
- Python: [`App Store Server Python Library`](https://developer.apple.comhttps://github.com/apple/app-store-server-library-python)
- Node: [`App Store Server Node Library`](https://developer.apple.comhttps://github.com/apple/app-store-server-library-node)

Choose the language that best supports your server and expertise.

The App Store Server Library offers four key capabilities:

- An API client that encodes [`App Store Server API`](AppStoreServerAPI.md) requests, decodes the responses, and creates the JSON Web Token (JWT) you use to authenticate the calls. For more information on using JWTs, see [`Generating JSON Web Tokens for API requests`](generating-json-web-tokens-for-api-requests.md).
- Functions that verify JWS transactions, to verify that Apple signed the transaction data you get in API responses, from [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) and from devices using [`StoreKit`](https://developer.apple.com/documentation/StoreKit). See the functions `verifyAndDecodeTransaction`, `verifyAndDecodeAppTransaction`, and `verifyAndDecodeRenewalInfo`, available in each language the library supports.
- A utility that extracts transaction identifiers from receipts. The App Store Server API endpoints take a transaction identifier in the path parameter. Use this utility as you migrate from using [`verifyReceipt`](https://developer.apple.com/documentation/appstorereceipts/verifyreceipt) with [`App Store Receipts`](https://developer.apple.com/documentation/appstorereceipts) to using the App Store Server API for transaction information.
- A function that generates signatures for subscription promotional offers. For more information on promotional offers, see [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions).

For more information, see the WWDC23 session [`Meet the App Store Server Library`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10143/).

## See Also

- [Creating API keys to authorize API requests](creating-api-keys-to-authorize-api-requests.md)
  Create API keys you use to sign JSON Web Tokens and authorize API requests.
- [Generating JSON Web Tokens for API requests](generating-json-web-tokens-for-api-requests.md)
  Create JSON Web Tokens signed with your private key to authorize requests for App Store Server API and External Purchase Server API.
- [Identifying rate limits](identifying-rate-limits.md)
  Recognize the rate limits that apply to App Store Server API endpoints and handle them in your code.
- [App Store Server API changelog](app-store-server-api-changelog.md)
  Learn about new features and updates in the App Store Server API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library)*