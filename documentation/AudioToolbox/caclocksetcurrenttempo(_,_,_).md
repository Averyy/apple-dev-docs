# CAClockSetCurrentTempo(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockSetCurrentTempo(_ inCAClock: CAClockRef, _ inTempo: CAClockTempo, _ inTimestamp: UnsafePointer<CAClockTime>?) -> OSStatus
```

```c
extern OSStatus CAClockSetCurrentTempo(CAClockRef inCAClock, CAClockTempo inTempo, const CAClockTime *inTimestamp);
```

## See Also

### Accessing Tempo Information
- [func CAClockGetCurrentTempo(CAClockRef, UnsafeMutablePointer<CAClockTempo>, UnsafeMutablePointer<CAClockTime>?) -> OSStatus](./caclockgetcurrenttempo%28_,_,_%29.md)
- [func CAClockGetPlayRate(CAClockRef, UnsafeMutablePointer<Float64>) -> OSStatus](./caclockgetplayrate%28_,_%29.md)
- [func CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus](./caclocksetplayrate%28_,_%29.md)
- [typealias CAClockTempo](./caclocktempo.md)
- [struct CATempoMapEntry](./catempomapentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocksetcurrenttempo(_:_:_:))*