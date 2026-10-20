# CAClockSetPlayRate(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockSetPlayRate(_ inCAClock: CAClockRef, _ inPlayRate: Float64) -> OSStatus
```

```c
extern OSStatus CAClockSetPlayRate(CAClockRef inCAClock, Float64 inPlayRate);
```

## See Also

### Accessing Tempo Information
- [func CAClockGetCurrentTempo(CAClockRef, UnsafeMutablePointer<CAClockTempo>, UnsafeMutablePointer<CAClockTime>?) -> OSStatus](./caclockgetcurrenttempo%28_,_,_%29.md)
- [func CAClockSetCurrentTempo(CAClockRef, CAClockTempo, UnsafePointer<CAClockTime>?) -> OSStatus](./caclocksetcurrenttempo%28_,_,_%29.md)
- [func CAClockGetPlayRate(CAClockRef, UnsafeMutablePointer<Float64>) -> OSStatus](./caclockgetplayrate%28_,_%29.md)
- [typealias CAClockTempo](./caclocktempo.md)
- [struct CATempoMapEntry](./catempomapentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocksetplayrate(_:_:))*