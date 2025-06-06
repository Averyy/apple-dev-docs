# CheckTestNotificationResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains the contents of the App Store server’s test notification and the result from your server.

**Availability**:
- App Store Server API 1.5+

## Declaration

```swift
object CheckTestNotificationResponse
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The [`Get Test Notification Status`](get-test-notification-status.md) endpoint returns this response.

The `sendAttempts` array contains up to six [`sendAttemptItem`](sendattemptitem.md) items: one for the initial attempt, and up to five for the retries. Use this information to troubleshoot your server if it doesn’t receive notifications at its [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint successfully.

The `signedPayload` contains the `TEST` notification that the App Store server attempted to send to your server.

## Topics

### Data types
- [object sendAttemptItem](sendattemptitem.md)
  The success or error information and the date the App Store server records when it attempts to send a server notification to your server.
- [type signedPayload](signedpayload.md)
  A cryptographically signed payload, in JSON Web Signature (JWS) format, containing the response body for a version 2 notification.

## See Also

- [Request a Test Notification](request-a-test-notification.md)
  Ask App Store Server Notifications to send a test notification to your server.
- [Get Test Notification Status](get-test-notification-status.md)
  Check the status of the test App Store server notification sent to your server.
- [object SendTestNotificationResponse](sendtestnotificationresponse.md)
  A response that contains the test notification token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/checktestnotificationresponse)*