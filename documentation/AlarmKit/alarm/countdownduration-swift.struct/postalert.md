# postAlert

**Framework**: AlarmKit  
**Kind**: property

The duration applied after the alarm has alerted at least once and moves back to the countdown state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var postAlert: TimeInterval?
```

#### Discussion

For example, this would be the snooze duration for an alarm.  A timer with a repeat button could set this value to be the same as `preAlert`, or it could leave the value as `nil`.  If the value is `nil` we will use the `preAlert` duration for post-alarm countdowns.

## See Also

- [init(preAlert: TimeInterval?, postAlert: TimeInterval?)](alarm/countdownduration-swift.struct/init(prealert:postalert:).md)
  Creates an instance of a countdown duration.
- [var preAlert: TimeInterval?](alarm/countdownduration-swift.struct/prealert.md)
  The duration applied before the alarm fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/countdownduration-swift.struct/postalert)*