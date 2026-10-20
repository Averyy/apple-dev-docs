# CAClockGetCurrentTime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetCurrentTime(_ inCAClock: CAClockRef, _ inTimeFormat: CAClockTimeFormat, _ outTime: UnsafeMutablePointer<CAClockTime>) -> OSStatus
```

```c
extern OSStatus CAClockGetCurrentTime(CAClockRef inCAClock, CAClockTimeFormat inTimeFormat, CAClockTime *outTime);
```

## See Also

### Accessing the Current Time
- [func CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus](./caclocksetcurrenttime%28_,_%29.md)
- [func CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclockgetstarttime%28_,_,_%29.md)
- [struct CAClockTime](./caclocktime.md)
- [enum CAClockTimeFormat](./caclocktimeformat.md)
- [typealias CAClockSamples](./caclocksamples.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetcurrenttime(_:_:_:))*