# AlertingContext

**Framework**: Accessory Notifications  
**Kind**: struct

A structure that provides guidance for how to alert for a notification.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct AlertingContext
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Overview

To alert for a notification, present it on screen, play a sound, or trigger a haptic effect that uses touch to give users feedback.

## Topics

### Determining alerting behavior
- [var shouldAlert: Bool](alertingcontext/shouldalert.md)
  A Boolean value that indicates the recommended alerting behavior.
- [var notificationCanAlert: Bool](alertingcontext/notificationcanalert.md)
  A Boolean value that indicates whether the accessory can alert the person for the notification.
- [var isSuppressedByFocus: Bool](alertingcontext/issuppressedbyfocus.md)
  A Boolean value that indicates whether the device’s Focus state suppresses notification alerts.
### Creating an alerting context
- [init(notificationCanAlert: Bool, suppressedByFocus: Bool)](alertingcontext/init(notificationcanalert:suppressedbyfocus:).md)
  Initializes an alerting context with the given alert conditions.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)

## See Also

- [struct AccessoryNotification](accessorynotification.md)
  A structure that contains the details of a notification that iOS provides to your accessory.
- [protocol AlertCoordinating](alertcoordinating.md)
  A protocol that communicates whether the accessory completes the process of alerting for a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertingcontext)*