# CAClockBeatsToBarBeatTime(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockBeatsToBarBeatTime(_ inCAClock: CAClockRef, _ inBeats: CAClockBeats, _ inSubbeatDivisor: UInt16, _ outBarBeatTime: UnsafeMutablePointer<CABarBeatTime>) -> OSStatus
```

```c
extern OSStatus CAClockBeatsToBarBeatTime(CAClockRef inCAClock, CAClockBeats inBeats, UInt16 inSubbeatDivisor, CABarBeatTime *outBarBeatTime);
```

## See Also

### Converting Time Values
- [func CAClockBarBeatTimeToBeats(CAClockRef, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<CAClockBeats>) -> OSStatus](./caclockbarbeattimetobeats%28_,_,_%29.md)
- [func CAClockSMPTETimeToSeconds(CAClockRef, UnsafePointer<SMPTETime>, UnsafeMutablePointer<CAClockSeconds>) -> OSStatus](./caclocksmptetimetoseconds%28_,_,_%29.md)
- [func CAClockSecondsToSMPTETime(CAClockRef, CAClockSeconds, UInt16, UnsafeMutablePointer<SMPTETime>) -> OSStatus](./caclocksecondstosmptetime%28_,_,_,_%29.md)
- [func CAClockTranslateTime(CAClockRef, UnsafePointer<CAClockTime>, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclocktranslatetime%28_,_,_,_%29.md)
- [enum CAClockTimebase](./caclocktimebase.md)
- [typealias CAClockSeconds](./caclockseconds.md)
- [typealias CAClockBeats](./caclockbeats.md)
- [typealias CAClockSMPTEFormat](./caclocksmpteformat.md)
- [struct CABarBeatTime](./cabarbeattime.md)
- [struct CAMeterTrackEntry](./cametertrackentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockbeatstobarbeattime(_:_:_:_:))*