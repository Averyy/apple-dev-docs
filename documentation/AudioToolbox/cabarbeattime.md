# CABarBeatTime

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct CABarBeatTime
```

```c
struct CABarBeatTime;
```

## Topics

### Initializers
- [init()](./cabarbeattime/init%28%29.md)
- [init(bar: Int32, beat: UInt16, subbeat: UInt16, subbeatDivisor: UInt16, reserved: UInt16)](./cabarbeattime/init%28bar,beat,subbeat,subbeatdivisor,reserved%29.md)
### Instance Properties
- [var bar: Int32](./cabarbeattime/bar.md)
- [var beat: UInt16](./cabarbeattime/beat.md)
- [var reserved: UInt16](./cabarbeattime/reserved.md)
- [var subbeat: UInt16](./cabarbeattime/subbeat.md)
- [var subbeatDivisor: UInt16](./cabarbeattime/subbeatdivisor.md)

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
- [struct CAMeterTrackEntry](./cametertrackentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/cabarbeattime)*