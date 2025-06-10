# alarm(schedule:attributes:stopIntent:secondaryIntent:sound:)

**Framework**: AlarmKit  
**Kind**: method

Creates a configuration that behaves like a traditional alarm.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
static func alarm(schedule: Alarm.Schedule? = nil, attributes: AlarmAttributes<Metadata>, stopIntent: (any LiveActivityIntent)? = nil, secondaryIntent: (any LiveActivityIntent)? = nil, sound: AlertConfiguration.AlertSound = .default) -> AlarmManager.AlarmConfiguration<Metadata>
```

#### Discussion

At the scheduled time, based on the `schedule` parameter you supply, the alarm alerts.

## Parameters

- `schedule`: The schedule for the alarm.
- `attributes`: The attributes to use when presenting the alert.
- `stopIntent`: The intent to execute when a person taps the stop button.
- `secondaryIntent`: The intent to execute when a person taps the secondary button.
- `sound`: The sound to play when the alarm fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmconfiguration/alarm(schedule:attributes:stopintent:secondaryintent:sound:))*