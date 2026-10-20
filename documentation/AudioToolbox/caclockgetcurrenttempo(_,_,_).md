# CAClockGetCurrentTempo(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetCurrentTempo(_ inCAClock: CAClockRef, _ outTempo: UnsafeMutablePointer<CAClockTempo>, _ outTimestamp: UnsafeMutablePointer<CAClockTime>?) -> OSStatus
```

```c
extern OSStatus CAClockGetCurrentTempo(CAClockRef inCAClock, CAClockTempo *outTempo, CAClockTime *outTimestamp);
```

## See Also

### Accessing Tempo Information
- [func CAClockSetCurrentTempo(CAClockRef, CAClockTempo, UnsafePointer<CAClockTime>?) -> OSStatus](./caclocksetcurrenttempo%28_,_,_%29.md)
- [func CAClockGetPlayRate(CAClockRef, UnsafeMutablePointer<Float64>) -> OSStatus](./caclockgetplayrate%28_,_%29.md)
- [func CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus](./caclocksetplayrate%28_,_%29.md)
- [typealias CAClockTempo](./caclocktempo.md)
- [struct CATempoMapEntry](./catempomapentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetcurrenttempo(_:_:_:))*