# CAMeterTrackEntry

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct CAMeterTrackEntry
```

```c
struct CAMeterTrackEntry;
```

## Topics

### Initializers
- [init()](./cametertrackentry/init%28%29.md)
- [init(beats: CAClockBeats, meterNumer: UInt16, meterDenom: UInt16)](./cametertrackentry/init%28beats,meternumer,meterdenom%29.md)
### Instance Properties
- [var beats: CAClockBeats](./cametertrackentry/beats.md)
- [var meterDenom: UInt16](./cametertrackentry/meterdenom.md)
- [var meterNumer: UInt16](./cametertrackentry/meternumer.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Converting Time Values
- [func CAClockBarBeatTimeToBeats(CAClockRef, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<CAClockBeats>) -> OSStatus](./caclockbarbeattimetobeats%28_,_,_%29.md)
- [func CAClockBeatsToBarBeatTime(CAClockRef, CAClockBeats, UInt16, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](./caclockbeatstobarbeattime%28_,_,_,_%29.md)
- [func CAClockSMPTETimeToSeconds(CAClockRef, UnsafePointer<SMPTETime>, UnsafeMutablePointer<CAClockSeconds>) -> OSStatus](./caclocksmptetimetoseconds%28_,_,_%29.md)
- [func CAClockSecondsToSMPTETime(CAClockRef, CAClockSeconds, UInt16, UnsafeMutablePointer<SMPTETime>) -> OSStatus](./caclocksecondstosmptetime%28_,_,_,_%29.md)
- [func CAClockTranslateTime(CAClockRef, UnsafePointer<CAClockTime>, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclocktranslatetime%28_,_,_,_%29.md)
- [enum CAClockTimebase](./caclocktimebase.md)
- [typealias CAClockSeconds](./caclockseconds.md)
- [typealias CAClockBeats](./caclockbeats.md)
- [typealias CAClockSMPTEFormat](./caclocksmpteformat.md)
- [struct CABarBeatTime](./cabarbeattime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/cametertrackentry)*