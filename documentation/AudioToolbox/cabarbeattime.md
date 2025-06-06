# CABarBeatTime

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct CABarBeatTime
```

## Topics

### Initializers
- [init()](cabarbeattime/init.md)
- [init(bar: Int32, beat: UInt16, subbeat: UInt16, subbeatDivisor: UInt16, reserved: UInt16)](cabarbeattime/init(bar:beat:subbeat:subbeatdivisor:reserved:).md)
### Instance Properties
- [var bar: Int32](cabarbeattime/bar.md)
- [var beat: UInt16](cabarbeattime/beat.md)
- [var reserved: UInt16](cabarbeattime/reserved.md)
- [var subbeat: UInt16](cabarbeattime/subbeat.md)
- [var subbeatDivisor: UInt16](cabarbeattime/subbeatdivisor.md)

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
- [struct CAMeterTrackEntry](cametertrackentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/cabarbeattime)*