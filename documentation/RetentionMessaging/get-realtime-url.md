# Get Realtime URL

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Gets the URL for real-time messages that points to your Get Retention Message endpoint, which you previously configured.

**Availability**:
- Retention Messaging API 1.4+

## Mentions

- [Identifying rate limits](identifying-rate-limits.md)
- [Retention Messaging API changelog](retention-messaging-changelog.md)
- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)

#### Discussion

This endpoint returns your `Get Retention Message` endpoint’s URL. The URL it provides is specific to the environment (sandbox or production) you use to call [`Get Realtime URL`](get-realtime-url.md).

This endpoint returns an `HTTP 404` error with [`RealtimeUrlNotFoundError`](realtimeurlnotfounderror.md) if the URL isn’t configured.

For more information on configuring your `Get Retention Message` endpoint, see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md).

## Endpoint

`GET https://api.storekit-sandbox.apple.com/inApps/v1/messaging/realtime/url`

## See Also

- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
  Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
- [Configure Realtime URL](configure-realtime-url.md)
  Configures the URL for your Get Retention Message endpoint in the sandbox and production environments.
- [Delete Realtime URL](delete-realtime-url.md)
  Deletes the URL for your Get Retention Message endpoint, in the sandbox or production environments.
- [object RealtimeUrlRequest](realtimeurlrequest.md)
  The request body for configuring the URL of your Get Retention Message endpoint.
- [object RealtimeRequestBody](realtimerequestbody.md)
  The request body the App Store server sends to your Get Retention Message endpoint.
- [object RealtimeUrlResponse](realtimeurlresponse.md)
  The response body that contains the URL for your Get Retention Message endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/get-realtime-url)*