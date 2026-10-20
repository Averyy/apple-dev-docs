# AlertConfiguration.AlertSound

**Framework**: ActivityKit  
**Kind**: struct  
**Role**: Structure

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
- [static func named(String) -> AlertConfiguration.AlertSound](./alertsound/named%28_%29.md)
  A function you use to configure a custom sound for a Live Activity update alert.
- [static var `default`: AlertConfiguration.AlertSound](./alertsound/default.md)
  A value that represents the system’s default alert sound.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring Live Activity alerts
- [init(title: LocalizedStringResource, body: LocalizedStringResource, sound: AlertConfiguration.AlertSound)](./init%28title,body,sound%29.md)
  Initializes a new alert configuration for a Live Activity update.
- [var title: LocalizedStringResource](./title.md)
  A short title that describes the purpose of the Live Activity update on Apple Watch.
- [var body: LocalizedStringResource](./body.md)
  The main text that appears on the alert for a Live Activity update on Apple Watch.
- [var sound: AlertConfiguration.AlertSound](./sound.md)
  The sound the system plays when the Live Activity alert appears on a person’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/alertconfiguration/alertsound)*