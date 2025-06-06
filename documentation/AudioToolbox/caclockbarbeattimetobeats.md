# CAClockBarBeatTimeToBeats(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockBarBeatTimeToBeats(_ inCAClock: CAClockRef, _ inBarBeatTime: UnsafePointer<CABarBeatTime>, _ outBeats: UnsafeMutablePointer<CAClockBeats>) -> OSStatus
```

## See Also

- [func CAClockBeatsToBarBeatTime(CAClockRef, CAClockBeats, UInt16, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](caclockbeatstobarbeattime(_:_:_:_:).md)
- [func CAClockSMPTETimeToSeconds(CAClockRef, UnsafePointer<SMPTETime>, UnsafeMutablePointer<CAClockSeconds>) -> OSStatus](caclocksmptetimetoseconds(_:_:_:).md)
- [func CAClockSecondsToSMPTETime(CAClockRef, CAClockSeconds, UInt16, UnsafeMutablePointer<SMPTETime>) -> OSStatus](caclocksecondstosmptetime(_:_:_:_:).md)
- [func CAClockTranslateTime(CAClockRef, UnsafePointer<CAClockTime>, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclocktranslatetime(_:_:_:_:).md)
- [enum CAClockTimebase](caclocktimebase.md)
- [typealias CAClockSeconds](caclockseconds.md)
- [typealias CAClockBeats](caclockbeats.md)
- [typealias CAClockSMPTEFormat](caclocksmpteformat.md)
- [struct CABarBeatTime](cabarbeattime.md)
- [struct CAMeterTrackEntry](cametertrackentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockbarbeattimetobeats(_:_:_:))*