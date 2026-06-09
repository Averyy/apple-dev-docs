# init(countdownDuration:schedule:attributes:appEntityIdentifier:stopIntent:secondaryIntent:sound:)

**Framework**: AlarmKit  
**Kind**: init

Creates a configuration that behaves like a countdown.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(countdownDuration: Alarm.CountdownDuration? = nil, schedule: Alarm.Schedule? = nil, attributes: AlarmAttributes<Metadata>, appEntityIdentifier: EntityIdentifier? = nil, stopIntent: (any LiveActivityIntent)? = nil, secondaryIntent: (any LiveActivityIntent)? = nil, sound: AlertConfiguration.AlertSound = .default)
```

## Parameters

- `countdownDuration`: The optional countdown duration. When set to a non-nil value, a countdown shows in the Lock Screen for the specified duration.
- `schedule`: The schedule that determines when the alarm alerts.
- `attributes`: The attributes of the alarm.
- `appEntityIdentifier`: The entity associated with the alarm.
- `stopIntent`: The intent to execute when a person stops the countdown.
- `secondaryIntent`: The intent to execute when a person taps the secondary button.
- `sound`: The sound to play when the alarm fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmconfiguration/init(countdownduration:schedule:attributes:appentityidentifier:stopintent:secondaryintent:sound:))*