# AlarmManager.AlarmConfiguration

**Framework**: AlarmKit  
**Kind**: struct

An object that contains all the properties necessary to schedule an alarm.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct AlarmConfiguration<Metadata> where Metadata : AlarmMetadata
```

#### Overview

Pass the schedule or countdown and any attributes you define to the `AlarmConfiguration` for the system to schedule. You can pass in an optional secondary intent that the system executes when a person taps a secondary button. This is only available after first unlock. You can also include custom sounds for your alarm.

The following example configures an alarm with a countdown duration.

```swift
let configuration = AlarmManager.AlarmConfiguration(countdownDuration: Alarm.CountdownDuration(preAlert: 10, postAlert: 10),
    schedule: nil,
    attributes: attributes,
    secondaryIntent: repeatIntent,
    alertConfiguration: AlertConfiguration(title: "Eggs are ready!", body: "Time to eat!", sound: .default))
```

## Topics

### Configuring a scheduled alarm
- [static func alarm(schedule: Alarm.Schedule?, attributes: AlarmAttributes<Metadata>, stopIntent: (any LiveActivityIntent)?, secondaryIntent: (any LiveActivityIntent)?, sound: AlertConfiguration.AlertSound) -> AlarmManager.AlarmConfiguration<Metadata>](alarmmanager/alarmconfiguration/alarm(schedule:attributes:stopintent:secondaryintent:sound:).md)
  Creates a configuration that behaves like a traditional alarm.
### Configuring a countdown
- [init(countdownDuration: Alarm.CountdownDuration?, schedule: Alarm.Schedule?, attributes: AlarmAttributes<Metadata>, stopIntent: (any LiveActivityIntent)?, secondaryIntent: (any LiveActivityIntent)?, sound: AlertConfiguration.AlertSound)](alarmmanager/alarmconfiguration/init(countdownduration:schedule:attributes:stopintent:secondaryintent:sound:).md)
  Creates a configuration that behaves like a countdown.
- [static func timer(duration: TimeInterval, attributes: AlarmAttributes<Metadata>, stopIntent: (any LiveActivityIntent)?, secondaryIntent: (any LiveActivityIntent)?, sound: AlertConfiguration.AlertSound) -> AlarmManager.AlarmConfiguration<Metadata>](alarmmanager/alarmconfiguration/timer(duration:attributes:stopintent:secondaryintent:sound:).md)
  Creates a configuration that behaves like a traditional timer.

## See Also

- [func schedule<Metadata>(id: Alarm.ID, configuration: AlarmManager.AlarmConfiguration<Metadata>) async throws -> Alarm](alarmmanager/schedule(id:configuration:).md)
  Schedules a new alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmconfiguration)*