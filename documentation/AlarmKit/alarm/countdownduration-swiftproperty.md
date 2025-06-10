# countdownDuration

**Framework**: AlarmKit  
**Kind**: property

The time left before an alert, in seconds.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var countdownDuration: Alarm.CountdownDuration?
```

#### Discussion

When set to a non-nil value, the system shows the countdown in the Lock Screen for the specified duration. The UI will appear at a time equal to the next scheduled alert date minus the duration.

## See Also

- [struct CountdownDuration](alarm/countdownduration-swift.struct.md)
  An object that defines the durations used in an alarm that has a countdown.
- [var id: UUID](alarm/id-swift.property.md)
  The unique identifier of the alarm.
- [Alarm.State](alarm/state-swift.enum.md)
  An enum that lists all possible states of an alarm.
- [var state: Alarm.State](alarm/state-swift.property.md)
  The current state of the alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/countdownduration-swift.property)*