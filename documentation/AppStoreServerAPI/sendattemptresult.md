# sendAttemptResult

**Framework**: App Store Server API  
**Kind**: typealias

The success or error information the App Store server records when it attempts to send an App Store server notification to your server.

**Availability**:
- App Store Server API 1.8+

## Declaration

```swift
string sendAttemptResult
```

#### Discussion

The [`Get Notification History`](get-notification-history.md) and [`Get Test Notification Status`](get-test-notification-status.md) endpoints return a [`sendAttemptResult`](sendattemptresult.md) for each notification attempt in their responses. This value describes the success or error the server encountered on its attempt to send the notification to your server.

In the production environment, the App Store server retries sending the notfications if it doesn’t receive a `200` response from your server. Your server may have successfully received the notification on the App Store server’s subsequent attempt if the [`sendAttemptResult`](sendattemptresult.md) value shows an error.

In the sandbox environment, the App Store server attempts to send the notification one time.

For more information about the timing of retry attempts, see [`Responding to App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications).

## See Also

- [object sendAttemptItem](sendattemptitem.md)
  The success or error information and the date the App Store server records when it attempts to send a server notification to your server.
- [type signedPayload](signedpayload.md)
  A cryptographically signed payload, in JSON Web Signature (JWS) format, containing the response body for a version 2 notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/sendattemptresult)*