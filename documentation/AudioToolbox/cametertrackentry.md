# CAMeterTrackEntry

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct CAMeterTrackEntry
```

## Topics

### Initializers
- [init()](cametertrackentry/init.md)
- [init(beats: CAClockBeats, meterNumer: UInt16, meterDenom: UInt16)](cametertrackentry/init(beats:meternumer:meterdenom:).md)
### Instance Properties
- [var beats: CAClockBeats](cametertrackentry/beats.md)
- [var meterDenom: UInt16](cametertrackentry/meterdenom.md)
- [var meterNumer: UInt16](cametertrackentry/meternumer.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func CAClockBarBeatTimeToBeats(CAClockRef, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<CAClockBeats>) -> OSStatus](caclockbarbeattimetobeats(_:_:_:).md)
- [func CAClockBeatsToBarBeatTime(CAClockRef, CAClockBeats, UInt16, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](caclockbeatstobarbeattime(_:_:_:_:).md)
- [func CAClockSMPTETimeToSeconds(CAClockRef, UnsafePointer<SMPTETime>, UnsafeMutablePointer<CAClockSeconds>) -> OSStatus](caclocksmptetimetoseconds(_:_:_:).md)
- [func CAClockSecondsToSMPTETime(CAClockRef, CAClockSeconds, UInt16, UnsafeMutablePointer<SMPTETime>) -> OSStatus](caclocksecondstosmptetime(_:_:_:_:).md)
- [func CAClockTranslateTime(CAClockRef, UnsafePointer<CAClockTime>, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclocktranslatetime(_:_:_:_:).md)
- [enum CAClockTimebase](caclocktimebase.md)
- [typealias CAClockSeconds](caclockseconds.md)
- [typealias CAClockBeats](caclockbeats.md)
- [typealias CAClockSMPTEFormat](caclocksmpteformat.md)
- [struct CABarBeatTime](cabarbeattime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/cametertrackentry)*