# preAlert

**Framework**: AlarmKit  
**Kind**: property

The duration applied before the alarm fires.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var preAlert: TimeInterval?
```

#### Discussion

For example, this would be the duration of a timer.

## See Also

- [init(preAlert: TimeInterval?, postAlert: TimeInterval?)](alarm/countdownduration-swift.struct/init(prealert:postalert:).md)
  Creates an instance of a countdown duration.
- [var postAlert: TimeInterval?](alarm/countdownduration-swift.struct/postalert.md)
  The duration applied after the alarm has alerted at least once and moves back to the countdown state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/countdownduration-swift.struct/prealert)*