# RealtimeUrlResponse

**Framework**: Retention Messaging API  
**Kind**: dictionary

The response body that contains the URL for your Get Retention Message endpoint.

**Availability**:
- Retention Messaging API 1.4+

## Declaration

```swift
object RealtimeUrlResponse
```

#### Discussion

This is the response body for the [`Get Realtime URL`](get-realtime-url.md) endpoint.

## Properties

- `realtimeURL` (realtimeURL) *(required)*: A string that contains the URL you provided for your Get Retention Message endpoint.

## See Also

- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
  Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
- [Configure Realtime URL](configure-realtime-url.md)
  Configures the URL for your Get Retention Message endpoint in the sandbox and production environments.
- [Get Realtime URL](get-realtime-url.md)
  Gets the URL for real-time messages that points to your Get Retention Message endpoint, which you previously configured.
- [Delete Realtime URL](delete-realtime-url.md)
  Deletes the URL for your Get Retention Message endpoint, in the sandbox or production environments.
- [object RealtimeUrlRequest](realtimeurlrequest.md)
  The request body for configuring the URL of your Get Retention Message endpoint.
- [object RealtimeRequestBody](realtimerequestbody.md)
  The request body the App Store server sends to your Get Retention Message endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/realtimeurlresponse)*