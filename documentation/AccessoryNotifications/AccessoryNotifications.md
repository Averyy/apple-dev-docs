# Accessory Notifications

**Framework**: Accessory Notifications  
**Kind**: module

Receive forwarded iOS system notifications on an accessory that you develop.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

#### Overview

The Accessory Notifications framework allows accessory companion apps to request notification forwarding from people, and receive notification content from the system through an extension model. People can choose to forward notifications from all apps, no apps, or a subset of apps on their device.

> ❗ **Important**: This framework supports iPhone only. You can develop and test an app that uses this framework on devices in any region. The framework currently builds only for development or Ad Hoc testing. The framework will support App Store submission and alternative distribution at a later time. Customer installations of your app can use the framework only on devices located in the EU that are signed in with an Apple Account with an EU country or region.

#### Request Notification Forwarding

Call [`requestForwarding(for:)`](accessorynotificationcenter/requestforwarding(for:).md) from your companion app to prompt the person to allow notification forwarding. The system identifies your accessory through the reference you receive from [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit). The method returns a [`ForwardingDecision`](forwardingdecision.md) that indicates the person’s choice.

Check the current forwarding status for an accessory using [`forwardingStatus(for:)`](accessorynotificationcenter/forwardingstatus(for:).md), or present notification settings using [`presentSettings(for:scenePersistentIdentifier:)`](accessorynotificationcenter/presentsettings(for:scenepersistentidentifier:).md).

#### Receive and Process Notifications

To receive notifications, implement [`NotificationsForwarding.AccessoryNotificationsHandler`](notificationsforwarding/accessorynotificationshandler.md) in an [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) extension of the [`Accessory Transport Extension`](https://developer.apple.com/documentation/AccessoryTransportExtension) framework. The system calls your handler’s methods for notification arrivals, updates, or removals. Curate just the notification information that your accessory needs from the [`AccessoryNotification`](accessorynotification.md) structure, which includes content for display, icons, related file attachments, and interactive actions.

Send the curated data to your accessory using the session’s [`send(message:)`](notificationsforwarding/accessorynotificationssession/send(message:).md) method. The system encrypts the data using keys established through your app’s [`AccessoryTransportSecurity`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSecurity) extension, then delivers the encrypted data to your app’s [`AccessoryTransportAppExtension`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportAppExtension) for transmission to the accessory.

Your handler’s [`addNotification(_:alertingContext:)`](notificationsforwarding/accessorynotificationshandler/addnotification(_:alertingcontext:).md) method returns a Boolean value that indicates whether your accessory alerted for the notification. Return `true` if the accessory successfully alerts the person. The system considers that information to coordinate alerting across multiple devices.

#### Decrypt and Display Notifications

Your accessory receives the encrypted notification data and implements [`HPKE (RFC9180)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/rfc9180/) decryption to parse the notification details. Use [`AlertingContext`](alertingcontext.md) to determine whether to send an alert for the notification. The [`shouldAlert`](alertingcontext/shouldalert.md) property provides the recommended behavior that matches the system’s alerting logic.

For incoming call notifications, check [`isIncomingCall`](alertingcontext/isincomingcall.md) to apply special handling. Use [`sound`](alertingcontext/sound-swift.property.md) to determine sound characteristics, including whether the notification ignores silent mode.

## Topics

### Essentials
- [Receiving iOS notifications on an accessory](../AccessoryTransportExtension/receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage iOS system notifications for your accessory.
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
  A session object that enables communication between the system and your extension.
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