# init(preAlert:postAlert:)

**Framework**: AlarmKit  
**Kind**: init

Creates an instance of a countdown duration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(preAlert: TimeInterval?, postAlert: TimeInterval?)
```

## Parameters

- `preAlert`: The duration applied before the alarm fires.
- `postAlert`: The duration applied after the alarm has alerted at least once and   moves back to the countdown state.

## See Also

- [var postAlert: TimeInterval?](alarm/countdownduration-swift.struct/postalert.md)
  The duration applied after the alarm has alerted at least once and moves back to the countdown state.
- [var preAlert: TimeInterval?](alarm/countdownduration-swift.struct/prealert.md)
  The duration applied before the alarm fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/countdownduration-swift.struct/init(prealert:postalert:))*