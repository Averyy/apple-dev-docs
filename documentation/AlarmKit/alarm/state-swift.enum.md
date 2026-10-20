# Alarm.State

**Framework**: AlarmKit  
**Kind**: enum  
**Role**: Enumeration

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
- [Alarm.State.alerting](./state-swift.enum/alerting.md)
  The alarm is currently firing.
- [Alarm.State.countdown](./state-swift.enum/countdown.md)
  The alarm is counting down to its alert time.
- [Alarm.State.paused](./state-swift.enum/paused.md)
  A person paused the countdown.
- [Alarm.State.scheduled](./state-swift.enum/scheduled.md)
  The alarm is scheduled and ready to alert at the appropriate time.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Defining a countdown duration
- [struct CountdownDuration](./countdownduration-swift.struct.md)
  An object that defines the durations used in an alarm that has a countdown.
- [var countdownDuration: Alarm.CountdownDuration?](./countdownduration-swift.property.md)
  The time left before an alert, in seconds.
- [var id: UUID](./id.md)
  The unique identifier of the alarm.
- [var state: Alarm.State](./state-swift.property.md)
  The current state of the alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/state-swift.enum)*