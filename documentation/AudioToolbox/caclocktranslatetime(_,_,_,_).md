# CAClockTranslateTime(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockTranslateTime(_ inCAClock: CAClockRef, _ inTime: UnsafePointer<CAClockTime>, _ inOutputTimeFormat: CAClockTimeFormat, _ outTime: UnsafeMutablePointer<CAClockTime>) -> OSStatus
```

```c
extern OSStatus CAClockTranslateTime(CAClockRef inCAClock, const CAClockTime *inTime, CAClockTimeFormat inOutputTimeFormat, CAClockTime *outTime);
```

## See Also

### Converting Time Values
- [func CAClockBarBeatTimeToBeats(CAClockRef, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<CAClockBeats>) -> OSStatus](./caclockbarbeattimetobeats%28_,_,_%29.md)
- [func CAClockBeatsToBarBeatTime(CAClockRef, CAClockBeats, UInt16, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](./caclockbeatstobarbeattime%28_,_,_,_%29.md)
- [func CAClockSMPTETimeToSeconds(CAClockRef, UnsafePointer<SMPTETime>, UnsafeMutablePointer<CAClockSeconds>) -> OSStatus](./caclocksmptetimetoseconds%28_,_,_%29.md)
- [func CAClockSecondsToSMPTETime(CAClockRef, CAClockSeconds, UInt16, UnsafeMutablePointer<SMPTETime>) -> OSStatus](./caclocksecondstosmptetime%28_,_,_,_%29.md)
- [enum CAClockTimebase](./caclocktimebase.md)
- [typealias CAClockSeconds](./caclockseconds.md)
- [typealias CAClockBeats](./caclockbeats.md)
- [typealias CAClockSMPTEFormat](./caclocksmpteformat.md)
- [struct CABarBeatTime](./cabarbeattime.md)
- [struct CAMeterTrackEntry](./cametertrackentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocktranslatetime(_:_:_:_:))*