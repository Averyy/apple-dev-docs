# CATempoMapEntry

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct CATempoMapEntry
```

## Topics

### Initializers
- [init()](catempomapentry/init.md)
- [init(beats: CAClockBeats, tempoBPM: CAClockTempo)](catempomapentry/init(beats:tempobpm:).md)
### Instance Properties
- [var beats: CAClockBeats](catempomapentry/beats.md)
- [var tempoBPM: CAClockTempo](catempomapentry/tempobpm.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func CAClockGetCurrentTempo(CAClockRef, UnsafeMutablePointer<CAClockTempo>, UnsafeMutablePointer<CAClockTime>?) -> OSStatus](caclockgetcurrenttempo(_:_:_:).md)
- [func CAClockSetCurrentTempo(CAClockRef, CAClockTempo, UnsafePointer<CAClockTime>?) -> OSStatus](caclocksetcurrenttempo(_:_:_:).md)
- [func CAClockGetPlayRate(CAClockRef, UnsafeMutablePointer<Float64>) -> OSStatus](caclockgetplayrate(_:_:).md)
- [func CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus](caclocksetplayrate(_:_:).md)
- [typealias CAClockTempo](caclocktempo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/catempomapentry)*