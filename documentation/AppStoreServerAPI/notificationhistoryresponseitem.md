# notificationHistoryResponseItem

**Framework**: App Store Server API  
**Kind**: dictionary

The App Store server notification history record, including the signed notification payload and the result of the server’s first send attempt.

**Availability**:
- App Store Server API 1.5+

## Declaration

```swift
object notificationHistoryResponseItem
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

## Topics

### Data types
- [type sendAttemptResult](sendattemptresult.md)
  The success or error information the App Store server records when it attempts to send an App Store server notification to your server.
- [object sendAttemptItem](sendattemptitem.md)
  The success or error information and the date the App Store server records when it attempts to send a server notification to your server.
- [type signedPayload](signedpayload.md)
  A cryptographically signed payload, in JSON Web Signature (JWS) format, containing the response body for a version 2 notification.

## See Also

- [Get Notification History](get-notification-history.md)
  Get a list of notifications that the App Store server attempted to send to your server.
- [object NotificationHistoryRequest](notificationhistoryrequest.md)
  The request body for notification history.
- [object NotificationHistoryResponse](notificationhistoryresponse.md)
  A response that contains the App Store Server Notifications history for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/notificationhistoryresponseitem)*