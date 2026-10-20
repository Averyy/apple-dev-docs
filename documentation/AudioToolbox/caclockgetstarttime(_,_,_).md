# CAClockGetStartTime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetStartTime(_ inCAClock: CAClockRef, _ inTimeFormat: CAClockTimeFormat, _ outTime: UnsafeMutablePointer<CAClockTime>) -> OSStatus
```

```c
extern OSStatus CAClockGetStartTime(CAClockRef inCAClock, CAClockTimeFormat inTimeFormat, CAClockTime *outTime);
```

## See Also

### Accessing the Current Time
- [func CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclockgetcurrenttime%28_,_,_%29.md)
- [func CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus](./caclocksetcurrenttime%28_,_%29.md)
- [struct CAClockTime](./caclocktime.md)
- [enum CAClockTimeFormat](./caclocktimeformat.md)
- [typealias CAClockSamples](./caclocksamples.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetstarttime(_:_:_:))*