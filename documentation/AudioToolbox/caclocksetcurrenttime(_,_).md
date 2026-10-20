# CAClockSetCurrentTime(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockSetCurrentTime(_ inCAClock: CAClockRef, _ inTime: UnsafePointer<CAClockTime>) -> OSStatus
```

```c
extern OSStatus CAClockSetCurrentTime(CAClockRef inCAClock, const CAClockTime *inTime);
```

## See Also

### Accessing the Current Time
- [func CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclockgetcurrenttime%28_,_,_%29.md)
- [func CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclockgetstarttime%28_,_,_%29.md)
- [struct CAClockTime](./caclocktime.md)
- [enum CAClockTimeFormat](./caclocktimeformat.md)
- [typealias CAClockSamples](./caclocksamples.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocksetcurrenttime(_:_:))*