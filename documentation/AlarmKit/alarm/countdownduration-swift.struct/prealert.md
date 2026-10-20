# preAlert

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

The duration applied before the alarm fires.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var preAlert: TimeInterval?
```

#### Discussion

For example, this would be the duration of a timer.

## See Also

### Creating a countdown duration
- [init(preAlert: TimeInterval?, postAlert: TimeInterval?)](./init%28prealert,postalert%29.md)
  Creates an instance of a countdown duration.
- [var postAlert: TimeInterval?](./postalert.md)
  The duration applied after the alarm has alerted at least once and moves back to the countdown state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/countdownduration-swift.struct/prealert)*