# Delete Realtime URL

**Framework**: Retention Messaging API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Deletes the URL for your Get Retention Message endpoint, in the sandbox or production environments.

**Availability**:
- Retention Messaging API 1.4+

## Mentions

- [Identifying rate limits](./identifying-rate-limits.md)
- [Retention Messaging API changelog](./retention-messaging-changelog.md)
- [Setting up your Get Retention Message endpoint](./setting-up-retention-messaging-endpoint.md)

## Discussion

Call this endpoint’s sandbox URL to delete the sandbox URL of your `Get Retention Message` endpoint.  Call this endpoint’s production URL to delete the production URL of your `Get Retention Message` endpoint.

After this call succeeds in the sandbox or production environment, the Retention Messaging API no longer provides real-time retention messages in the respective environment, unless you configure a URL again.

To configure URLs again, call [`Configure Realtime URL`](./configure-realtime-url.md). There’s no need to call [`Delete Realtime URL`](./delete-realtime-url.md) before reconfiguring endpoint URLs. To check the URL you have configured for your endpoint, call [`Get Realtime URL`](./get-realtime-url.md).

## Endpoint

`DELETE https://api.storekit-sandbox.apple.com/inApps/v1/messaging/realtime/url`

## Responses

- `200` OK: Request succeeded.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md).
- `404` Not Found: The request is invalid because the developer account doesn’t have access to this API. For more information, see [Request access to the Retention Messaging API](https://developer.apple.com/contact/request/retention-messaging-api/).
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`GeneralInternalError`, `application/json`): Server error. Try again later.

## See Also

### Real-time retention messaging setup
- [Setting up your Get Retention Message endpoint](./setting-up-retention-messaging-endpoint.md)
  Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
- [Configure Realtime URL](./configure-realtime-url.md)
  Configures the URL for your Get Retention Message endpoint in the sandbox and production environments.
- [Get Realtime URL](./get-realtime-url.md)
  Gets the URL for real-time messages that points to your Get Retention Message endpoint, which you previously configured.
- [object RealtimeUrlRequest](./realtimeurlrequest.md)
  The request body for configuring the URL of your Get Retention Message endpoint.
- [object RealtimeRequestBody](./realtimerequestbody.md)
  The request body the App Store server sends to your Get Retention Message endpoint.
- [object RealtimeUrlResponse](./realtimeurlresponse.md)
  The response body that contains the URL for your Get Retention Message endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/delete-realtime-url)*