# title

**Framework**: ActivityKit  
**Kind**: property

A short title that describes the purpose of the Live Activity update on Apple Watch.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
var title: LocalizedStringResource
```

#### Discussion

Apple Watch displays this string briefly as part of the alert that appears when you update a Live Activity and choose to alert people about the update. Choose text that’s easy to read at a glance. For example, a pizza delivery app could use “On the way.”

## See Also

- [init(title: LocalizedStringResource, body: LocalizedStringResource, sound: AlertConfiguration.AlertSound)](alertconfiguration/init(title:body:sound:).md)
  Initializes a new alert configuration for a Live Activity update.
- [var body: LocalizedStringResource](alertconfiguration/body.md)
  The main text that appears on the alert for a Live Activity update on Apple Watch.
- [var sound: AlertConfiguration.AlertSound](alertconfiguration/sound.md)
  The sound the system plays when the Live Activity alert appears on a person’s device.
- [AlertConfiguration.AlertSound](alertconfiguration/alertsound.md)
  An object that describes the sound to play for a Live Activity update alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/alertconfiguration/title)*