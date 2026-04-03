# RealtimeUrlRequest

**Framework**: Retention Messaging API  
**Kind**: dictionary

The request body for configuring the URL of your Get Retention Message endpoint.

**Availability**:
- Retention Messaging API 1.4+

## Declaration

```swift
object RealtimeUrlRequest
```

## Mentions

- [Retention Messaging API changelog](retention-messaging-changelog.md)

#### Discussion

To configure your `Get Retention Message` endpoint’s URL, call [`Configure Realtime URL`](configure-realtime-url.md) and provide the URL in this request body. For more information, see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md).

## Properties

- `realtimeURL` (realtimeURL) *(required)*: A string that contains the URL of your `Get Retention Message` endpoint for configuration.

## See Also

- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
  Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
- [Configure Realtime URL](configure-realtime-url.md)
  Configures the URL for your Get Retention Message endpoint in the sandbox and production environments.
- [Get Realtime URL](get-realtime-url.md)
  Gets the URL for real-time messages that points to your Get Retention Message endpoint, which you previously configured.
- [Delete Realtime URL](delete-realtime-url.md)
  Deletes the URL for your Get Retention Message endpoint, in the sandbox or production environments.
- [object RealtimeRequestBody](realtimerequestbody.md)
  The request body the App Store server sends to your Get Retention Message endpoint.
- [object RealtimeUrlResponse](realtimeurlresponse.md)
  The response body that contains the URL for your Get Retention Message endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/realtimeurlrequest)*