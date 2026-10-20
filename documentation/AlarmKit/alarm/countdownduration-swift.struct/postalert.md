# postAlert

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

The duration applied after the alarm has alerted at least once and moves back to the countdown state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var postAlert: TimeInterval?
```

#### Discussion

For example, this would be the snooze duration for an alarm.  A timer with a repeat button could set this value to be the same as `preAlert`, or it could leave the value as `nil`.  If the value is `nil` we will use the `preAlert` duration for post-alarm countdowns.

## See Also

### Creating a countdown duration
- [init(preAlert: TimeInterval?, postAlert: TimeInterval?)](./init%28prealert,postalert%29.md)
  Creates an instance of a countdown duration.
- [var preAlert: TimeInterval?](./prealert.md)
  The duration applied before the alarm fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/countdownduration-swift.struct/postalert)*