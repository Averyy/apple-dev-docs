# CAClockTimebase

**Framework**: Audio Toolbox  
**Kind**: enum

**Availability**:
- macOS ?+

## Declaration

```swift
enum CAClockTimebase
```

## Topics

### Constants
- [CAClockTimebase.audioDevice](caclocktimebase/audiodevice.md)
- [CAClockTimebase.audioOutputUnit](caclocktimebase/audiooutputunit.md)
- [CAClockTimebase.hostTime](caclocktimebase/hosttime.md)
### Initializers
- [init?(rawValue: UInt32)](caclocktimebase/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func CAClockBarBeatTimeToBeats(CAClockRef, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<CAClockBeats>) -> OSStatus](caclockbarbeattimetobeats(_:_:_:).md)
- [func CAClockBeatsToBarBeatTime(CAClockRef, CAClockBeats, UInt16, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](caclockbeatstobarbeattime(_:_:_:_:).md)
- [func CAClockSMPTETimeToSeconds(CAClockRef, UnsafePointer<SMPTETime>, UnsafeMutablePointer<CAClockSeconds>) -> OSStatus](caclocksmptetimetoseconds(_:_:_:).md)
- [func CAClockSecondsToSMPTETime(CAClockRef, CAClockSeconds, UInt16, UnsafeMutablePointer<SMPTETime>) -> OSStatus](caclocksecondstosmptetime(_:_:_:_:).md)
- [func CAClockTranslateTime(CAClockRef, UnsafePointer<CAClockTime>, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclocktranslatetime(_:_:_:_:).md)
- [typealias CAClockSeconds](caclockseconds.md)
- [typealias CAClockBeats](caclockbeats.md)
- [typealias CAClockSMPTEFormat](caclocksmpteformat.md)
- [struct CABarBeatTime](cabarbeattime.md)
- [struct CAMeterTrackEntry](cametertrackentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocktimebase)*