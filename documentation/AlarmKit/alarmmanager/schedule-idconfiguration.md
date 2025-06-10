# schedule(id:configuration:)

**Framework**: AlarmKit  
**Kind**: method

Schedules a new alarm.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func schedule<Metadata>(id: Alarm.ID, configuration: AlarmManager.AlarmConfiguration<Metadata>) async throws -> Alarm where Metadata : AlarmMetadata
```

#### Discussion

If scheduling a new alarm is successful, the function returns the [`Alarm`](alarm.md) structure. If you provide a [`countdownDuration`](alarm/countdownduration-swift.property.md), the system shows a countdown UI for the specified duration before the alarm alerts. If you provide a `schedule`, the alarm alerts at the scheduled time. If you provide both a `countdownDuration` and a [`schedule`](alarm/schedule-swift.property.md), the system shows a countdown UI before the alarm alerts, possibly on a repeating schedule. Define the ID to encode it into your intent.

## Parameters

- `id`: The alarm’s identifier.
- `configuration`: The configuration for the new alarm.

## See Also

- [AlarmManager.AlarmConfiguration](alarmmanager/alarmconfiguration.md)
  An object that contains all the properties necessary to schedule an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/schedule(id:configuration:))*