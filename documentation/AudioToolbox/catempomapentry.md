# CATempoMapEntry

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct CATempoMapEntry
```

```c
struct CATempoMapEntry;
```

## Topics

### Initializers
- [init()](./catempomapentry/init%28%29.md)
- [init(beats: CAClockBeats, tempoBPM: CAClockTempo)](./catempomapentry/init%28beats,tempobpm%29.md)
### Instance Properties
- [var beats: CAClockBeats](./catempomapentry/beats.md)
- [var tempoBPM: CAClockTempo](./catempomapentry/tempobpm.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Accessing Tempo Information
- [func CAClockGetCurrentTempo(CAClockRef, UnsafeMutablePointer<CAClockTempo>, UnsafeMutablePointer<CAClockTime>?) -> OSStatus](./caclockgetcurrenttempo%28_,_,_%29.md)
- [func CAClockSetCurrentTempo(CAClockRef, CAClockTempo, UnsafePointer<CAClockTime>?) -> OSStatus](./caclocksetcurrenttempo%28_,_,_%29.md)
- [func CAClockGetPlayRate(CAClockRef, UnsafeMutablePointer<Float64>) -> OSStatus](./caclockgetplayrate%28_,_%29.md)
- [func CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus](./caclocksetplayrate%28_,_%29.md)
- [typealias CAClockTempo](./caclocktempo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/catempomapentry)*