# assemblyTrackID

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
var assemblyTrackID: CMPersistentTrackID { get }
```

#### Discussion

The trackID identifies which track should be written to this segment file. This is the same track ID in the AVAssetTrackPlan object. This is also the trackID the AVAssetWritingPlanner uses to build the assembled AVComposition before it calls the completion handler.

## See Also

- [var timeRange: CMTimeRange](avplannedsegmentwritingrequest/timerange.md)
- [var segmentFileOutputURL: URL](avplannedsegmentwritingrequest/segmentfileoutputurl.md)
- [var progress: Float](avplannedsegmentwritingrequest/progress.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/assemblytrackid)*