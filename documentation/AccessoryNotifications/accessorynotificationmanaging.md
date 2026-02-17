# AccessoryNotificationManaging

**Framework**: Accessory Notifications  
**Kind**: protocol

A protocol that enables the communication of notification responses to the system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol AccessoryNotificationManaging
```

#### Overview

The [`AccessoryNotificationManagerFactory`](accessorynotificationmanagerfactory.md) class provides access to a system-provided object that implements this protocol through [`defaultManager`](accessorynotificationmanagerfactory/defaultmanager.md).

> ❗ **Important**: The Accessory Notifications framework will support this feature in a future release.

## Topics

### Clearing notifications
- [func removeNotifications(forIdentifiers: Set<String>, sourceIdentifier: String, for: ASAccessory) async throws](accessorynotificationmanaging/removenotifications(foridentifiers:sourceidentifier:for:).md)
  Removes notifications posted by an application.
### Sending notification responses
- [func sendResponse(NotificationResponse, for: ASAccessory) async throws](accessorynotificationmanaging/sendresponse(_:for:).md)
  Sends a notification response from an accessory to the system.

## See Also

- [class AccessoryNotificationManagerFactory](accessorynotificationmanagerfactory.md)
  A factory class that provides access to the system notification manager.
- [struct NotificationResponse](notificationresponse.md)
  A person’s response to a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationmanaging)*