# CAClockGetPlayRate(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetPlayRate(_ inCAClock: CAClockRef, _ outPlayRate: UnsafeMutablePointer<Float64>) -> OSStatus
```

## See Also

- [func CAClockGetCurrentTempo(CAClockRef, UnsafeMutablePointer<CAClockTempo>, UnsafeMutablePointer<CAClockTime>?) -> OSStatus](caclockgetcurrenttempo(_:_:_:).md)
- [func CAClockSetCurrentTempo(CAClockRef, CAClockTempo, UnsafePointer<CAClockTime>?) -> OSStatus](caclocksetcurrenttempo(_:_:_:).md)
- [func CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus](caclocksetplayrate(_:_:).md)
- [typealias CAClockTempo](caclocktempo.md)
- [struct CATempoMapEntry](catempomapentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetplayrate(_:_:))*