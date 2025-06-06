# CAClockGetStartTime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetStartTime(_ inCAClock: CAClockRef, _ inTimeFormat: CAClockTimeFormat, _ outTime: UnsafeMutablePointer<CAClockTime>) -> OSStatus
```

## See Also

- [func CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclockgetcurrenttime(_:_:_:).md)
- [func CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus](caclocksetcurrenttime(_:_:).md)
- [struct CAClockTime](caclocktime.md)
- [enum CAClockTimeFormat](caclocktimeformat.md)
- [typealias CAClockSamples](caclocksamples.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetstarttime(_:_:_:))*