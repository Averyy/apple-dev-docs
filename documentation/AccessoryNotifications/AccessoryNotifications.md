# Accessory Notifications

**Framework**: Accessory Notifications  
**Kind**: module

Receive forwarded iOS system notifications on an accessory that you develop.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

#### Overview

The Accessory Notifications framework allows accessory companion apps to request notification forwarding from people, and receive notification content from the system through an extension model. People can choose to forward notifications from all apps, no apps, or a subset of apps on their device.

> ❗ **Important**: This framework supports iPhone only. You can develop and test an app that uses this framework on devices in any region. The framework currently builds only for development or Ad Hoc testing. The framework will support App Store submission, TestFlight, and alternative distribution at a later time. Customer installations of your app can use the framework only on devices located in the EU that are signed in with an Apple Account with an EU country or region.

#### Request Notification Forwarding

Call [`requestForwarding(for:)`](accessorynotificationcenter/requestforwarding(for:).md) from your companion app to prompt the person to allow notification forwarding. The system identifies your accessory through the reference you receive from [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit). The method returns a [`ForwardingDecision`](forwardingdecision.md) that indicates the person’s choice.

#### Receive and Process Notifications

To receive notifications, implement [`NotificationsForwarding.AccessoryNotificationsHandler`](notificationsforwarding/accessorynotificationshandler.md) in an [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) extension of the [`Accessory Transport Extension`](https://developer.apple.com/documentation/AccessoryTransportExtension) framework. The system calls your handler’s methods for notification arrivals, updates, or removals. Curate just the notification information that your accessory needs from the [`AccessoryNotification`](accessorynotification.md) structure, which includes content for display, icons, related file attachments, and interactions.

Return the curated data to the system using the session’s doc://com.apple.documentation/documentation/accessorytransportextension/AccessoryFeatureSession/sendMessage(_:) method. The system encrypts the data using keys you provide through your app’s [`AccessoryTransportSecurity`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSecurity) extension. Then, the system delivers the encrypted data to your app’s [`AccessoryTransportAppExtension`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportAppExtension) for transmission to the accessory.

#### Decrypt and Display Notifications

Your accessory receives the encrypted notification data and implements [`HPKE (RFC9180)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/rfc9180/) decryption to parse the notification details. Use [`AlertingContext`](alertingcontext.md) to determine whether to send an alert for the notification. The [`shouldAlert`](alertingcontext/shouldalert.md) property provides the recommended behavior that matches the system’s alerting logic.

> **Note**: In a future release, the framework will support receiving information from the accessory, such as confirmation of notification receipt and user interactions.

## Topics

### Essentials
- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage notifications for your accessory.
### Authorization
- [class AccessoryNotificationCenter](accessorynotificationcenter.md)
  A class that enables an app to request permission for notification forwarding.
- [enum ForwardingDecision](forwardingdecision.md)
  Possible decisions in response to the notification forwarding permission prompt.
### Notification receipt
- [class NotificationsForwarding](notificationsforwarding.md)
  A class for handling notification forwarding in your accessory’s data provider extension.
- [NotificationsForwarding.AccessoryNotificationsHandler](notificationsforwarding/accessorynotificationshandler.md)
  A protocol that defines methods for handling notification lifecycle events in your extension.
- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that enables communication between your extension and the system.
### Data curation and alerting
- [struct AccessoryNotification](accessorynotification.md)
  A structure that contains the details of a notification that iOS provides to your accessory.
- [struct AlertingContext](alertingcontext.md)
  A structure that provides guidance for how to alert for a notification.
### Interactive support
- [struct NotificationResponse](notificationresponse.md)
  A person’s response to a notification.
### Errors
- [enum AccessoryError](accessoryerror.md)
  Errors the Accessory Notifications framework can throw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AccessoryNotifications)*