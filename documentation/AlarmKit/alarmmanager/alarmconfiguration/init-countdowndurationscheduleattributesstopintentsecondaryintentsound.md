# init(countdownDuration:schedule:attributes:stopIntent:secondaryIntent:sound:)

**Framework**: AlarmKit  
**Kind**: init

Creates a configuration that behaves like a countdown.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
init(countdownDuration: Alarm.CountdownDuration? = nil, schedule: Alarm.Schedule? = nil, attributes: AlarmAttributes<Metadata>, stopIntent: (any LiveActivityIntent)? = nil, secondaryIntent: (any LiveActivityIntent)? = nil, sound: AlertConfiguration.AlertSound = .default)
```

## Parameters

- `countdownDuration`: The optional countdown duration. When   set to a non-nil value, a countdown shows in the Lock Screen for the specified duration.
- `schedule`: The schedule that determines when the alarm alerts.
- `attributes`: The attributes of the alarm.
- `stopIntent`: The intent to execute when a person stops the countdown.
- `secondaryIntent`: The intent to execute when a person taps the secondary button.
- `sound`: The sound to play when the alarm fires.

## See Also

- [static func timer(duration: TimeInterval, attributes: AlarmAttributes<Metadata>, stopIntent: (any LiveActivityIntent)?, secondaryIntent: (any LiveActivityIntent)?, sound: AlertConfiguration.AlertSound) -> AlarmManager.AlarmConfiguration<Metadata>](alarmmanager/alarmconfiguration/timer(duration:attributes:stopintent:secondaryintent:sound:).md)
  Creates a configuration that behaves like a traditional timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmconfiguration/init(countdownduration:schedule:attributes:stopintent:secondaryintent:sound:))*