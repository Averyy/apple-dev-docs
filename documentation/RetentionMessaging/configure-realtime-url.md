# Configure Realtime URL

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Configures the URL for your Get Retention Message endpoint in the sandbox and production environments.

**Availability**:
- Retention Messaging API 1.4+

## Mentions

- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
- [Identifying rate limits](identifying-rate-limits.md)
- [Retention Messaging API changelog](retention-messaging-changelog.md)

#### Discussion

Call this endpoint to configure the URLs for your `Get Retention Message` endpoints in the sandbox and production environments. For more information, including endpoint specifications and server requirements, see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md).

> **Note**:  Your server needs to pass a performance test before you can configure your `Get Retention Message` endpoint for the production environment. For more information, see [`Initiate Performance Test`](initiate-performance-test.md).

As a best practice, use different URLs for the sandbox and production environments.

##### Configure Your Url for the Sandbox Environment

To configure your `Get Retention Message` endpoint for the sandbox environment, call [`Configure Realtime URL`](configure-realtime-url.md) using its sandbox URL. Provide your endpoint’s sandbox URL.

##### Configure Your Url for the Production Environment

To configure your `Get Retention Message` endpoint for the production environment, first configure your `Get Retention Message` endpoint for the sandbox environment, then:

1. Call [`Initiate Performance Test`](initiate-performance-test.md) to test your endpoint in the sandbox environment.
2. Call [`Get Performance Test Results`](get-performance-test-results.md) and ensure your server passes the performance test.
3. To configure your `Get Retention Message` endpoint for the production environment, call [`Configure Realtime URL`](configure-realtime-url.md) using its production URL. Provide your endpoint’s production URL.

##### Change Your Endpoints Url

To change your endpoint’s URL, just call [`Configure Realtime URL`](configure-realtime-url.md) again. The Retention Messaging API uses your most recent successful configuration. To check the URL you set, call [`Get Realtime URL`](get-realtime-url.md).

To delete—or deconfigure—your endpoint’s URL entirely, call [`Delete Realtime URL`](delete-realtime-url.md).

## Endpoint

`PUT https://api.storekit-sandbox.itunes.apple.com/inApps/v1/messaging/realtime/url`

## Request Body

The request body that includes your endpoint’s URL.

## See Also

- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
  Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
- [Get Realtime URL](get-realtime-url.md)
  Gets the URL for real-time messages that points to your Get Retention Message endpoint, which you previously configured.
- [Delete Realtime URL](delete-realtime-url.md)
  Deletes the URL for your Get Retention Message endpoint, in the sandbox or production environments.
- [object RealtimeUrlRequest](realtimeurlrequest.md)
  The request body for configuring the URL of your Get Retention Message endpoint.
- [object RealtimeRequestBody](realtimerequestbody.md)
  The request body the App Store server sends to your Get Retention Message endpoint.
- [object RealtimeUrlResponse](realtimeurlresponse.md)
  The response body that contains the URL for your Get Retention Message endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/configure-realtime-url)*