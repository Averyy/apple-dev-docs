# Alarm.State

**Framework**: AlarmKit  
**Kind**: enum

An enum that lists all possible states of an alarm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum State
```

## Topics

### Setting alarm states
- [Alarm.State.alerting](alarm/state-swift.enum/alerting.md)
  The alarm is currently firing.
- [Alarm.State.countdown](alarm/state-swift.enum/countdown.md)
  The alarm is counting down to its alert time.
- [Alarm.State.paused](alarm/state-swift.enum/paused.md)
  A person paused the countdown.
- [Alarm.State.scheduled](alarm/state-swift.enum/scheduled.md)
  The alarm is scheduled and ready to alert at the appropriate time.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct CountdownDuration](alarm/countdownduration-swift.struct.md)
  An object that defines the durations used in an alarm that has a countdown.
- [var countdownDuration: Alarm.CountdownDuration?](alarm/countdownduration-swift.property.md)
  The time left before an alert, in seconds.
- [var id: UUID](alarm/id.md)
  The unique identifier of the alarm.
- [var state: Alarm.State](alarm/state-swift.property.md)
  The current state of the alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/state-swift.enum)*