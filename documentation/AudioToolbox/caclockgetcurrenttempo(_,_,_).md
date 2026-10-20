# CAClockGetCurrentTempo(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetCurrentTempo(_ inCAClock: CAClockRef, _ outTempo: UnsafeMutablePointer<CAClockTempo>, _ outTimestamp: UnsafeMutablePointer<CAClockTime>?) -> OSStatus
```

## See Also

- [func CAClockSetCurrentTempo(CAClockRef, CAClockTempo, UnsafePointer<CAClockTime>?) -> OSStatus](caclocksetcurrenttempo(_:_:_:).md)
- [func CAClockGetPlayRate(CAClockRef, UnsafeMutablePointer<Float64>) -> OSStatus](caclockgetplayrate(_:_:).md)
- [func CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus](caclocksetplayrate(_:_:).md)
- [typealias CAClockTempo](caclocktempo.md)
- [struct CATempoMapEntry](catempomapentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetcurrenttempo(_:_:_:))*