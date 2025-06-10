# state

**Framework**: AlarmKit  
**Kind**: property

The current state of the alarm.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var state: Alarm.State
```

#### Discussion

This is a snapshot of the state captured when the alarm was fetched from the daemon.  It won’t update if the state changes on the daemon.

## See Also

- [struct CountdownDuration](alarm/countdownduration-swift.struct.md)
  An object that defines the durations used in an alarm that has a countdown.
- [var countdownDuration: Alarm.CountdownDuration?](alarm/countdownduration-swift.property.md)
  The time left before an alert, in seconds.
- [var id: UUID](alarm/id-swift.property.md)
  The unique identifier of the alarm.
- [Alarm.State](alarm/state-swift.enum.md)
  An enum that lists all possible states of an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/state-swift.property)*