# CAClockSetCurrentTempo(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockSetCurrentTempo(_ inCAClock: CAClockRef, _ inTempo: CAClockTempo, _ inTimestamp: UnsafePointer<CAClockTime>?) -> OSStatus
```

## See Also

- [func CAClockGetCurrentTempo(CAClockRef, UnsafeMutablePointer<CAClockTempo>, UnsafeMutablePointer<CAClockTime>?) -> OSStatus](caclockgetcurrenttempo(_:_:_:).md)
- [func CAClockGetPlayRate(CAClockRef, UnsafeMutablePointer<Float64>) -> OSStatus](caclockgetplayrate(_:_:).md)
- [func CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus](caclocksetplayrate(_:_:).md)
- [typealias CAClockTempo](caclocktempo.md)
- [struct CATempoMapEntry](catempomapentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocksetcurrenttempo(_:_:_:))*