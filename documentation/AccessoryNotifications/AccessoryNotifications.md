# Accessory Notifications

**Framework**: Accessory Notifications  
**Kind**: module

Receive forwarded iOS system notifications on an accessory that you develop.

**Availability**:
- iOS 26.5+

#### Overview

The Accessory Notifications framework allows accessory companion apps to request notification forwarding from people, and receive notification content from the system through an extension model. People can choose to forward notifications from all apps, no apps, or a subset of apps on their device. Implement the extensions this framework calls into using [`Accessory Transport Extension`](https://developer.apple.com/documentation/accessorytransportextension), which transfers notification content and responses to and from your accessory.

> ❗ **Important**: This framework supports iPhone only. You can develop and test an app that uses this framework on devices in any region. Customer installations of your app can only use the framework on devices located in the EU that are signed in with an Apple Account with an EU country or region.

#### Forward Ios System Notifications to an Accessory

The framework prompts the person to allow notification forwarding when your accessory’s companion app calls [`requestForwarding(for:)`](accessorynotificationcenter/requestforwarding(for:).md). The method returns a [`ForwardingDecision`](forwardingdecision.md) that indicates the person’s choice. Check the current forwarding status for an accessory using [`forwardingStatus(for:)`](accessorynotificationcenter/forwardingstatus(for:).md), or present notification settings using [`presentSettings(for:scenePersistentIdentifier:)`](accessorynotificationcenter/presentsettings(for:scenepersistentidentifier:).md).

When a person approves the prompt and the system is ready to forward a notification, the system calls [`NotificationsForwarding.AccessoryNotificationsHandler`](notificationsforwarding/accessorynotificationshandler.md) in an [`AccessoryDataProvider`](https://developer.apple.com/documentation/accessorytransportextension/accessorydataprovider) extension you implement to curate the notification details specifically for your accessory. The [`AccessoryNotification`](accessorynotification.md) contains the complete notification data, from which you curate the details your accessory needs. [`AlertingContext`](alertingcontext.md) determines if your accessory alerts for the notification, and how that alert occurs.

#### Respond to Notifications

If someone interacts with the notification, such as tapping to dismiss it, or typing text in a quick reply, your accessory sends information back to the companion app using [`messageHandler(_:)`](notificationsforwarding/accessorynotificationshandler/messagehandler(_:).md). The [`NotificationResponse`](notificationresponse.md) structure details the reply and your app delivers it to the system by calling [`sendResponse(_:)`](notificationsforwarding/accessorynotificationssession/sendresponse(_:).md).

## Topics

### Authorization
- [class AccessoryNotificationCenter](accessorynotificationcenter.md)
  A class that asks a person for permission to forward notifications.
- [enum ForwardingDecision](forwardingdecision.md)
  Possible decisions in response to the notification forwarding permission prompt.
### Notification receipt
- [Receiving iOS notifications on an accessory](../accessorytransportextension/receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage iOS system notifications for your accessory.
- [class NotificationsForwarding](notificationsforwarding.md)
  A class for handling notification forwarding in your accessory’s data provider extension.
- [NotificationsForwarding.AccessoryNotificationsHandler](notificationsforwarding/accessorynotificationshandler.md)
  A protocol that defines methods for handling notification life cycle events in your extension.
- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that facilitates bidirectional communication between the system and your extension.
### Data curation and alerting
- [struct AccessoryNotification](accessorynotification.md)
  A structure that contains the details of a notification that iOS provides to your accessory.
- [struct AlertingContext](alertingcontext.md)
  A structure that provides guidance for how to alert for a notification.
### Interactive support
- [Responding to forwarded notifications](responding-to-forwarded-notifications.md)
  Enable people to interact with notifications on your accessory and convey their responses to iOS.
- [struct NotificationResponse](notificationresponse.md)
  A structure that represents a person’s response to a notification.
### Errors
- [enum AccessoryError](accessoryerror.md)
  Errors the Accessory Notifications framework can throw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AccessoryNotifications)*