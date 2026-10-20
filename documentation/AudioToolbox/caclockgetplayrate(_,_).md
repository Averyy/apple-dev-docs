# CAClockGetPlayRate(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetPlayRate(_ inCAClock: CAClockRef, _ outPlayRate: UnsafeMutablePointer<Float64>) -> OSStatus
```

```c
extern OSStatus CAClockGetPlayRate(CAClockRef inCAClock, Float64 *outPlayRate);
```

## See Also

### Accessing Tempo Information
- [func CAClockGetCurrentTempo(CAClockRef, UnsafeMutablePointer<CAClockTempo>, UnsafeMutablePointer<CAClockTime>?) -> OSStatus](./caclockgetcurrenttempo%28_,_,_%29.md)
- [func CAClockSetCurrentTempo(CAClockRef, CAClockTempo, UnsafePointer<CAClockTime>?) -> OSStatus](./caclocksetcurrenttempo%28_,_,_%29.md)
- [func CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus](./caclocksetplayrate%28_,_%29.md)
- [typealias CAClockTempo](./caclocktempo.md)
- [struct CATempoMapEntry](./catempomapentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetplayrate(_:_:))*