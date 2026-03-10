# AlertCoordinating

**Framework**: Accessory Notifications  
**Kind**: protocol

A protocol that communicates whether the accessory completes the process of alerting for a notification.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
protocol AlertCoordinating : Sendable
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Overview

> ❗ **Important**: The Accessory Notifications framework will support this feature in a future release.

## Topics

### Completing coordination
- [func complete(didAlert: Bool)](alertcoordinating/complete(didalert:).md)
  Notifies the system of whether your accessory successfully alerted the person for the notification.
### Reporting coordination failure
- [func fail(any Error)](alertcoordinating/fail(_:).md)
  Notifies the system that alerting for a notification failed.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AccessoryNotification](accessorynotification.md)
  A structure that contains the details of a notification that iOS provides to your accessory.
- [struct AlertingContext](alertingcontext.md)
  A structure that provides guidance for how to alert for a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertcoordinating)*