# Get Notification History

**Framework**: App Store Server API  
**Kind**: httpRequest

Get a list of notifications that the App Store server attempted to send to your server.

**Availability**:
- App Store Server API 1.5+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Call this endpoint to get a paginated list of the version 2 [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications) that the App Store attempted to send to your server’s [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint in a specified timespan. Choose a start date for the timespan that’s within the past 180 days.

You can further limit the request by specifying a `notificationType` or `notificationSubtype` in the [`NotificationHistoryRequest`](notificationhistoryrequest.md) object. Alternatively, to get the notification history for a single user, provide a `transactionId`. The response, [`NotificationHistoryResponse`](notificationhistoryresponse.md), contains the full contents of the original notifications.

Each time you call this endpoint, it returns a maximum of 20 notification history records. If the [`hasMore`](hasmore.md) field in the [`NotificationHistoryResponse`](notificationhistoryresponse.md) is `true`, use the [`paginationToken`](get-notification-history/paginationtoken.md) from the response in your subsequent request to get the next set of records. Use the same [`NotificationHistoryRequest`](notificationhistoryrequest.md) body on subsequent requests.

This endpoint is available in the production and sandbox environments. For more information about configuring App Store Server Notifications, see [`Enabling App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications) and [`Enter a URL for App Store server notifications`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev0067a330b).

> **Note**:  For notifications that relate to in-app purchases, the history records reflect the state of an in-app purchase at the time the App Store originally sent the notification, and may not reflect its current state. To get the current state of auto-renewable subscriptions, call the [`Get All Subscription Statuses`](get-all-subscription-statuses.md) endpoint. For all other in-app purchase types, call the [`Get Transaction History V1`](get-transaction-history-v1.md) endpoint.

 For notifications that relate to in-app purchases, the history records reflect the state of an in-app purchase at the time the App Store originally sent the notification, and may not reflect its current state. To get the current state of auto-renewable subscriptions, call the [`Get All Subscription Statuses`](get-all-subscription-statuses.md) endpoint. For all other in-app purchase types, call the [`Get Transaction History V1`](get-transaction-history-v1.md) endpoint.

## Request Body

The request body that includes the start and end dates, and optional query constraints.

## See Also

- [object NotificationHistoryRequest](notificationhistoryrequest.md)
  The request body for notification history.
- [object NotificationHistoryResponse](notificationhistoryresponse.md)
  A response that contains the App Store Server Notifications history for your app.
- [object notificationHistoryResponseItem](notificationhistoryresponseitem.md)
  The App Store server notification history record, including the signed notification payload and the result of the server’s first send attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-notification-history)*