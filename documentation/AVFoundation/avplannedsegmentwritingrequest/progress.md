# progress

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var progress: Float { get }
```

#### Discussion

The current progress for the track identified by assemblyTrackID.

Returns a float value between 0.0 and 1.0 representing the percentage of duration completed for this track. This value is updated as segments are completed.

## See Also

- [var timeRange: CMTimeRange](avplannedsegmentwritingrequest/timerange.md)
- [var segmentFileOutputURL: URL](avplannedsegmentwritingrequest/segmentfileoutputurl.md)
- [var assemblyTrackID: CMPersistentTrackID](avplannedsegmentwritingrequest/assemblytrackid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/progress)*