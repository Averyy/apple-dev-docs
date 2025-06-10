# AlertConfiguration

**Framework**: ActivityKit  
**Kind**: struct

A structure you use to configure an alert that appears when you update your Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct AlertConfiguration
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)

## Topics

### Configuring Live Activity alerts
- [init(title: LocalizedStringResource, body: LocalizedStringResource, sound: AlertConfiguration.AlertSound)](alertconfiguration/init(title:body:sound:).md)
  Initializes a new alert configuration for a Live Activity update.
- [var title: LocalizedStringResource](alertconfiguration/title.md)
  A short title that describes the purpose of the Live Activity update on Apple Watch.
- [var body: LocalizedStringResource](alertconfiguration/body.md)
  The main text that appears on the alert for a Live Activity update on Apple Watch.
- [var sound: AlertConfiguration.AlertSound](alertconfiguration/sound.md)
  The sound the system plays when the Live Activity alert appears on a person’s device.
- [AlertConfiguration.AlertSound](alertconfiguration/alertsound.md)
  An object that describes the sound to play for a Live Activity update alert.
### Operators
- [static func == (AlertConfiguration, AlertConfiguration) -> Bool](alertconfiguration/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](alertconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func update(ActivityContent<Activity<Attributes>.ContentState>) async](activity/update(_:).md)
  Updates the dynamic content of the Live Activity.
- [func update(ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration?) async](activity/update(_:alertconfiguration:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [func update(ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration?, timestamp: Date) async](activity/update(_:alertconfiguration:timestamp:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/alertconfiguration)*