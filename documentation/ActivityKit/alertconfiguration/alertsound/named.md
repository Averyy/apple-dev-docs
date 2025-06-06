# named(_:)

**Framework**: ActivityKit  
**Kind**: method

A function you use to configure a custom sound for a Live Activity update alert.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
static func named(_ name: String) -> AlertConfiguration.AlertSound
```

## Parameters

- `name`: The name of the sound file to use for the alert. Choose a file that’s in your app’s main bundle   or the   folder of your app’s data container.

## See Also

- [static var `default`: AlertConfiguration.AlertSound](alertconfiguration/alertsound/default.md)
  A value that represents the system’s default alert sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/alertconfiguration/alertsound/named(_:))*