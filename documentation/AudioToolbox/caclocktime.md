# CAClockTime

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct CAClockTime
```

```c
struct CAClockTime;
```

## Topics

### Initializers
- [init()](./caclocktime/init%28%29.md)
- [init(format: CAClockTimeFormat, reserved: UInt32, time: CAClockTime.__Unnamed_union_time)](./caclocktime/init%28format,reserved,time%29.md)
### Instance Properties
- [var format: CAClockTimeFormat](./caclocktime/format.md)
- [var reserved: UInt32](./caclocktime/reserved.md)
- [var time: CAClockTime.__Unnamed_union_time](./caclocktime/time.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)

## See Also

### Accessing the Current Time
- [func CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclockgetcurrenttime%28_,_,_%29.md)
- [func CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus](./caclocksetcurrenttime%28_,_%29.md)
- [func CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclockgetstarttime%28_,_,_%29.md)
- [enum CAClockTimeFormat](./caclocktimeformat.md)
- [typealias CAClockSamples](./caclocksamples.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocktime)*