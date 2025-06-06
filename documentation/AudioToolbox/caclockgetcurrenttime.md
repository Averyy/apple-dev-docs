# CAClockGetCurrentTime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetCurrentTime(_ inCAClock: CAClockRef, _ inTimeFormat: CAClockTimeFormat, _ outTime: UnsafeMutablePointer<CAClockTime>) -> OSStatus
```

## See Also

- [func CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus](caclocksetcurrenttime(_:_:).md)
- [func CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclockgetstarttime(_:_:_:).md)
- [struct CAClockTime](caclocktime.md)
- [enum CAClockTimeFormat](caclocktimeformat.md)
- [typealias CAClockSamples](caclocksamples.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetcurrenttime(_:_:_:))*