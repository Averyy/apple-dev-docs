# timer(duration:attributes:stopIntent:secondaryIntent:sound:)

**Framework**: AlarmKit  
**Kind**: method

Creates a configuration that behaves like a traditional timer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static func timer(duration: TimeInterval, attributes: AlarmAttributes<Metadata>, stopIntent: (any LiveActivityIntent)? = nil, secondaryIntent: (any LiveActivityIntent)? = nil, sound: AlertConfiguration.AlertSound = .default) -> AlarmManager.AlarmConfiguration<Metadata>
```

#### Discussion

The timer starts immediately, runs for `duration` seconds, and then alerts.  If you provide a secondary button with a behavior that indicates that the timer can repeat, the alert has a repeat button.

## Parameters

- `duration`: The duration of the timer in seconds.
- `attributes`: The attributes to use when presenting the alert.
- `stopIntent`: The intent to execute when a person stops the timer.
- `secondaryIntent`: The intent to execute when a person taps the secondary button.
- `sound`: The sound to play when the alarm fires.

## See Also

- [init(countdownDuration: Alarm.CountdownDuration?, schedule: Alarm.Schedule?, attributes: AlarmAttributes<Metadata>, stopIntent: (any LiveActivityIntent)?, secondaryIntent: (any LiveActivityIntent)?, sound: AlertConfiguration.AlertSound)](alarmmanager/alarmconfiguration/init(countdownduration:schedule:attributes:stopintent:secondaryintent:sound:).md)
  Creates a configuration that behaves like a countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmconfiguration/timer(duration:attributes:stopintent:secondaryintent:sound:))*