# AlertingContext

**Framework**: Accessory Notifications  
**Kind**: struct

A structure that provides guidance for how to alert for a notification.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
struct AlertingContext
```

#### Overview

To alert for a notification, present it on screen, play a sound, or trigger a haptic effect that uses touch to give users feedback.

## Topics

### Creating an alerting context
- [init(notificationCanAlert: Bool, suppressedByFocus: Bool, isIncomingCall: Bool, sound: AlertingContext.Sound?)](alertingcontext/init(notificationcanalert:suppressedbyfocus:isincomingcall:sound:).md)
### Determining alerting behavior
- [var shouldAlert: Bool](alertingcontext/shouldalert.md)
  A Boolean value that indicates the recommended alerting behavior.
- [var notificationCanAlert: Bool](alertingcontext/notificationcanalert.md)
  A Boolean value that indicates whether the accessory can alert the person for the notification.
- [var isSuppressedByFocus: Bool](alertingcontext/issuppressedbyfocus.md)
  A Boolean value that indicates whether the device’s Focus state suppresses notification alerts.
### Handling special notification types
- [var isIncomingCall: Bool](alertingcontext/isincomingcall.md)
  A Boolean value that indicates whether the notification represents an incoming call.
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