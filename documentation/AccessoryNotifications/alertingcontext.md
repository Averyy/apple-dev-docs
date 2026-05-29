# AlertingContext

**Framework**: Accessory Notifications  
**Kind**: struct

A structure that provides guidance for how to alert for a notification.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
struct AlertingContext
```

#### Overview

To alert for a notification, present it on screen, play a sound, or trigger a haptic effect that uses touch to give users feedback.

## Topics

### Creating an alerting context
- [init(notificationCanAlert: Bool, suppressedByFocus: Bool, kind: AlertingContext.Kind, sound: AlertingContext.Sound?)](alertingcontext/init(notificationcanalert:suppressedbyfocus:kind:sound:).md)
  Initializes an alerting context with notification alert conditions.
### Determining alerting behavior
- [var shouldAlert: Bool](alertingcontext/shouldalert.md)
  A Boolean value that indicates the recommended alerting behavior.
- [var notificationCanAlert: Bool](alertingcontext/notificationcanalert.md)
  A Boolean value that indicates whether the accessory can alert the person for the notification.
- [var isSuppressedByFocus: Bool](alertingcontext/issuppressedbyfocus.md)
  A Boolean value that indicates whether the device’s Focus state suppresses notification alerts.
### Classifying the notification type
- [var kind: AlertingContext.Kind](alertingcontext/kind-swift.property.md)
  A classification for the notification type.
- [AlertingContext.Kind](alertingcontext/kind-swift.enum.md)
  Notification types for specialized handling.
### Configuring notification sound
- [var sound: AlertingContext.Sound?](alertingcontext/sound-swift.property.md)
  An optional sound configuration for the notification.
- [AlertingContext.Sound](alertingcontext/sound-swift.struct.md)
  A structure that describes sound characteristics for a notification.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertingcontext)*