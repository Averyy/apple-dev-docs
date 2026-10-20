# AlertConfiguration

**Framework**: ActivityKit  
**Kind**: struct  
**Role**: Structure

A structure you use to configure an alert that appears when you update your Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct AlertConfiguration
```

## Mentions

- [Displaying live data with Live Activities](./displaying-live-data-with-live-activities.md)

## Topics

### Configuring Live Activity alerts
- [init(title: LocalizedStringResource, body: LocalizedStringResource, sound: AlertConfiguration.AlertSound)](./alertconfiguration/init%28title,body,sound%29.md)
  Initializes a new alert configuration for a Live Activity update.
- [var title: LocalizedStringResource](./alertconfiguration/title.md)
  A short title that describes the purpose of the Live Activity update on Apple Watch.
- [var body: LocalizedStringResource](./alertconfiguration/body.md)
  The main text that appears on the alert for a Live Activity update on Apple Watch.
- [var sound: AlertConfiguration.AlertSound](./alertconfiguration/sound.md)
  The sound the system plays when the Live Activity alert appears on a person’s device.
- [AlertConfiguration.AlertSound](./alertconfiguration/alertsound.md)
  An object that describes the sound to play for a Live Activity update alert.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Updating a Live Activity
- [func update(ActivityContent<Activity<Attributes>.ContentState>) async](./activity/update%28_%29.md)
  Updates the dynamic content of the Live Activity.
- [func update(ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration?) async](./activity/update%28_,alertconfiguration%29.md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [func update(ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration?, timestamp: Date) async](./activity/update%28_,alertconfiguration,timestamp%29.md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/alertconfiguration)*