# CAClockSetCurrentTime(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockSetCurrentTime(_ inCAClock: CAClockRef, _ inTime: UnsafePointer<CAClockTime>) -> OSStatus
```

## See Also

- [func CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclockgetcurrenttime(_:_:_:).md)
- [func CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclockgetstarttime(_:_:_:).md)
- [struct CAClockTime](caclocktime.md)
- [enum CAClockTimeFormat](caclocktimeformat.md)
- [typealias CAClockSamples](caclocksamples.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocksetcurrenttime(_:_:))*