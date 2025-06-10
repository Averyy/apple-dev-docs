# NotificationHistoryResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains the App Store Server Notifications history for your app.

**Availability**:
- App Store Server API 1.5+

## Declaration

```swift
object NotificationHistoryResponse
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The [`Get Notification History`](get-notification-history.md) endpoint returns this response. Notification history records contain the notifications that the App Store server attempted to send to your server’s [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint.

The notification history response contains a maximum of 20 notification history records per response. If the history has more than 20 records, the [`hasMore`](notificationhistoryresponse/hasmore.md) value is `true`. Call [`Get Notification History`](get-notification-history.md) again with `paginationToken` in the query to receive the next page of responses. When the App Store has no more records to send, the `hasMore` value is `false`.

> **Note**:  The notifications in the history records reflect the state of an in-app purchase at the time the App Store originally sent the notification, and may not reflect its current state. To get the current state of auto-renewable subscriptions, call the [`Get All Subscription Statuses`](get-all-subscription-statuses.md) endpoint. For all other in-app purchase types, call the [`Get Transaction History V1`](get-transaction-history-v1.md) endpoint.

## Topics

### Data types
- [type paginationToken](paginationtoken.md)
  A pagination token that you return to the endpoint on a subsequent call to receive the next set of results.
- [type hasMore](hasmore.md)
  A Boolean value indicating whether the App Store has more transaction data.

## See Also

- [Get Notification History](get-notification-history.md)
  Get a list of notifications that the App Store server attempted to send to your server.
- [object NotificationHistoryRequest](notificationhistoryrequest.md)
  The request body for notification history.
- [object notificationHistoryResponseItem](notificationhistoryresponseitem.md)
  The App Store server notification history record, including the signed notification payload and the result of the server’s first send attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/notificationhistoryresponse)*