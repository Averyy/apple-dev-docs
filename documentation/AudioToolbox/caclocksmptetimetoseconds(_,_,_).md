# CAClockSMPTETimeToSeconds(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockSMPTETimeToSeconds(_ inCAClock: CAClockRef, _ inSMPTETime: UnsafePointer<SMPTETime>, _ outSeconds: UnsafeMutablePointer<CAClockSeconds>) -> OSStatus
```

```c
extern OSStatus CAClockSMPTETimeToSeconds(CAClockRef inCAClock, const SMPTETime *inSMPTETime, CAClockSeconds *outSeconds);
```

## See Also

### Converting Time Values
- [func CAClockBarBeatTimeToBeats(CAClockRef, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<CAClockBeats>) -> OSStatus](./caclockbarbeattimetobeats%28_,_,_%29.md)
- [func CAClockBeatsToBarBeatTime(CAClockRef, CAClockBeats, UInt16, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](./caclockbeatstobarbeattime%28_,_,_,_%29.md)
- [func CAClockSecondsToSMPTETime(CAClockRef, CAClockSeconds, UInt16, UnsafeMutablePointer<SMPTETime>) -> OSStatus](./caclocksecondstosmptetime%28_,_,_,_%29.md)
- [func CAClockTranslateTime(CAClockRef, UnsafePointer<CAClockTime>, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclocktranslatetime%28_,_,_,_%29.md)
- [enum CAClockTimebase](./caclocktimebase.md)
- [typealias CAClockSeconds](./caclockseconds.md)
- [typealias CAClockBeats](./caclockbeats.md)
- [typealias CAClockSMPTEFormat](./caclocksmpteformat.md)
- [struct CABarBeatTime](./cabarbeattime.md)
- [struct CAMeterTrackEntry](./cametertrackentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocksmptetimetoseconds(_:_:_:))*