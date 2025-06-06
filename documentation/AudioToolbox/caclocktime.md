# CAClockTime

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct CAClockTime
```

## Topics

### Initializers
- [init()](caclocktime/init.md)
- [init(format: CAClockTimeFormat, reserved: UInt32, time: CAClockTime.__Unnamed_union_time)](caclocktime/init(format:reserved:time:).md)
### Instance Properties
- [var format: CAClockTimeFormat](caclocktime/format.md)
- [var reserved: UInt32](caclocktime/reserved.md)
- [var time: CAClockTime.__Unnamed_union_time](caclocktime/time.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclockgetcurrenttime(_:_:_:).md)
- [func CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus](caclocksetcurrenttime(_:_:).md)
- [func CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclockgetstarttime(_:_:_:).md)
- [enum CAClockTimeFormat](caclocktimeformat.md)
- [typealias CAClockSamples](caclocksamples.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocktime)*