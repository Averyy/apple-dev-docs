# AlertConfiguration.AlertSound

**Framework**: ActivityKit  
**Kind**: struct

An object that describes the sound to play for a Live Activity update alert.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct AlertSound
```

## Topics

### Configuring the alert sound
- [static func named(String) -> AlertConfiguration.AlertSound](alertconfiguration/alertsound/named(_:).md)
  A function you use to configure a custom sound for a Live Activity update alert.
- [static var `default`: AlertConfiguration.AlertSound](alertconfiguration/alertsound/default.md)
  A value that represents the system’s default alert sound.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(title: LocalizedStringResource, body: LocalizedStringResource, sound: AlertConfiguration.AlertSound)](alertconfiguration/init(title:body:sound:).md)
  Initializes a new alert configuration for a Live Activity update.
- [var title: LocalizedStringResource](alertconfiguration/title.md)
  A short title that describes the purpose of the Live Activity update on Apple Watch.
- [var body: LocalizedStringResource](alertconfiguration/body.md)
  The main text that appears on the alert for a Live Activity update on Apple Watch.
- [var sound: AlertConfiguration.AlertSound](alertconfiguration/sound.md)
  The sound the system plays when the Live Activity alert appears on a person’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/alertconfiguration/alertsound)*