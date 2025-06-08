# App Store Server Notifications

**Framework**: App Store Server Notifications  
**Kind**: module

Monitor In-App Purchase events in real time and learn of unreported external purchase tokens, with server notifications from the App Store.

**Availability**:
- App Store Server Notifications 1.0+

## Mentions

- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md)

#### Overview

App Store Server Notifications is a server-to-server service that sends real-time notifications for In-App Purchase events, and notifications for unreported external purchase tokens. Use the data in the notifications to update your user-account database, and to monitor and respond to in-app purchase refunds. For notifications related to the [`External Purchase`](https://developer.apple.com/documentation/StoreKit/external-purchase) API, see [`externalPurchaseToken`](externalpurchasetoken.md).

> ❗ **Important**:  The [`App Store Server Notifications V1`](app-store-server-notifications-v1.md) endpoint and version 1 notifications, [`notification_type`](notification_type.md), are deprecated. Implement the [`App Store Server Notifications V2`](app-store-server-notifications-v2.md) endpoint on your server to receive version 2 notifications instead.

To receive server notifications from the App Store, provide your server’s HTTPS URL in App Store Connect. Opt in to receive notifications for the production environment and the sandbox environment. For more information, see [`Enabling App Store Server Notifications`](enabling-app-store-server-notifications.md).

Your server is responsible for parsing, interpreting, and responding to all server-to-server notification posts. For more information, see [`Receiving App Store Server Notifications`](receiving-app-store-server-notifications.md) and [`Responding to App Store Server Notifications`](responding-to-app-store-server-notifications.md).

##### Process in App Purchase Notifications

Notifications cover events in the in-app purchase life cycle, including purchases, subscription renewals, offer redemptions, refunds, and more. For a complete list of notification types, see [`notificationType`](notificationtype.md) for [`App Store Server Notifications V2`](app-store-server-notifications-v2.md).

Use the notification type, along with the transaction and subscription renewal information, to update a customer’s service or to present promotional offers according to your business logic.

##### Process External Purchase Token Notifications

A [`notificationType`](notificationtype.md) of `EXTERNAL_PURCHASE_TOKEN` with an `UNREPORTED` [`subtype`](subtype.md) indicates that Apple generated an external purchase token for your app but hasn’t received a report for the token. The notification includes the token in the [`externalPurchaseToken`](externalpurchasetoken.md) field of the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md). Use the token information to report it to Apple, including if you don’t recognize the token in your system. To report tokens, with or without associated transactions, call the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI)’s [`Send External Purchase Report`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report) endpoint.

For more information about token reporting requirements, see [`Using alternative payment options on the App Store in the European Union`](https://developer.apple.comhttps://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu/).

##### Test Your Server Setup

To determine whether your server is receiving notifications, call the [`Request a Test Notification`](https://developer.apple.com/documentation/AppStoreServerAPI/Request-a-Test-Notification) endpoint in the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI) to ask the App Store server to send a notification with the [`notificationType`](notificationtype.md) `TEST`. Use the `testNotificationToken` you receive to call the [`Get Test Notification Status`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Test-Notification-Status) endpoint to learn how your server responds to the test notification.

The App Store server sends the `TEST` notification in the version 2 notification format, however, it sends it to your server regardless of whether you configure a version 1 or version 2 notification URL in App Store Connect. For more information about configuring your URL in App Store Connect, see [`Enter a URL for App Store server notifications`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev0067a330b).

## Topics

### Essentials
- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md)
  Configure your server and provide an HTTPS URL to receive notifications about in-app purchase events and unreported external purchase tokens.
- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)
  Implement server-side code to receive and parse notification posts.
- [Responding to App Store Server Notifications](responding-to-app-store-server-notifications.md)
  Send HTTP status codes to indicate the success of a notification post.
- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)
  Learn about changes to the App Store Server Notifications service.
### Server notifications version 2
- [App Store Server Notifications V2](app-store-server-notifications-v2.md)
  Specify your secure server’s URL in App Store Connect to receive version 2 notifications.
- [object responseBodyV2](responsebodyv2.md)
  The response body the App Store sends in a version 2 server notification.
- [object responseBodyV2DecodedPayload](responsebodyv2decodedpayload.md)
  A decoded payload that contains the version 2 notification data.
- [type notificationType](notificationtype.md)
  The type that describes the in-app purchase or external purchase event for which the App Store sends the version 2 notification.
- [type subtype](subtype.md)
  A string that provides details about select notification types in version 2.
### Deprecated
- [App Store Server Notifications Version 1](app-store-server-notifications-version-1.md)
  Receive, parse, and interpret App Store Server Notifications version 1.

## See Also

- [In-App Purchase](../StoreKit/in-app-purchase.md)
  Offer content and services in your app across Apple platforms using a Swift-based interface.
- [App Store Server API](../AppStoreServerAPI/AppStoreServerAPI.md)
  Manage your customers’ App Store transactions from your server.
- [App Store Receipts](../appstorereceipts/appstorereceipts.md)
  Validate app and In-App Purchase receipts with the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreServerNotifications)*