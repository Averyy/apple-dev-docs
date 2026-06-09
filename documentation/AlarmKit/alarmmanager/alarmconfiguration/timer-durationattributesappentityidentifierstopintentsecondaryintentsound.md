# timer(duration:attributes:appEntityIdentifier:stopIntent:secondaryIntent:sound:)

**Framework**: AlarmKit  
**Kind**: method

Creates a configuration that behaves like a traditional timer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
static func timer(duration: TimeInterval, attributes: AlarmAttributes<Metadata>, appEntityIdentifier: EntityIdentifier? = nil, stopIntent: (any LiveActivityIntent)? = nil, secondaryIntent: (any LiveActivityIntent)? = nil, sound: AlertConfiguration.AlertSound = .default) -> AlarmManager.AlarmConfiguration<Metadata>
```

#### Discussion

The timer starts immediately, runs for `duration` seconds, and then alerts.  If you provide a secondary button with a behavior that indicates that the timer can repeat, the alert will have a repeat button.

## Parameters

- `duration`: The duration of the timer in seconds.
- `attributes`: The attributes to use when presenting the alert.
- `appEntityIdentifier`: The entity associated with the alarm.
- `stopIntent`: The intent to execute when a person stops the timer.
- `secondaryIntent`: The intent to execute when a person taps the secondary button.
- `sound`: The sound to play when the alarm fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmconfiguration/timer(duration:attributes:appentityidentifier:stopintent:secondaryintent:sound:))*