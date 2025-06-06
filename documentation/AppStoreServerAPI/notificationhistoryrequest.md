# NotificationHistoryRequest

**Framework**: App Store Server API  
**Kind**: dictionary

The request body for notification history.

**Availability**:
- App Store Server API 1.5+

## Declaration

```swift
object NotificationHistoryRequest
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

Specify the constraints for the App Store Server Notification history entries you’re requesting from [`Get Notification History`](get-notification-history.md). The request requires the `startDate` and `endDate` fields; all other fields are optional. Include only the fields in your request that you need to constrain the response.

If you provide both the `notificationType` and `subtype`, they need to be a valid combination, otherwise, the request returns an [`InvalidNotificationTypeError`](invalidnotificationtypeerror.md) error. For more information, see [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) and [`subtype`](https://developer.apple.com/documentation/AppStoreServerNotifications/subtype).

> **Note**:  Notification history is available for the past 180 days. Choose a `startDate` that’s within 180 days of the current date.

 Notification history is available for the past 180 days. Choose a `startDate` that’s within 180 days of the current date.

## Topics

### Data types
- [type startDate](startdate.md)
  The start date of a timespan, expressed in UNIX time, in milliseconds.
- [type endDate](enddate.md)
  The end date of a timespan, expressed in UNIX time, in milliseconds.
- [type notificationType](notificationtype.md)
  A notification type value that App Store Server Notifications 2 uses.
- [type notificationSubtype](notificationsubtype.md)
  A notification subtype value that App Store Server Notifications 2 uses.
- [type onlyFailures](onlyfailures.md)
  A Boolean value that indicates whether the response includes only notifications that failed to reach your server.

## See Also

- [Get Notification History](get-notification-history.md)
  Get a list of notifications that the App Store server attempted to send to your server.
- [object NotificationHistoryResponse](notificationhistoryresponse.md)
  A response that contains the App Store Server Notifications history for your app.
- [object notificationHistoryResponseItem](notificationhistoryresponseitem.md)
  The App Store server notification history record, including the signed notification payload and the result of the server’s first send attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/notificationhistoryrequest)*