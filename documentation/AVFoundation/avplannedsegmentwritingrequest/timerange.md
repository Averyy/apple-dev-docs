# timeRange

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
var timeRange: CMTimeRange { get }
```

#### Discussion

The PTS range for this segment.

The client is responsible for delivering the appropriate sample corresponding to timeRange.start if we are resuming a previous session that has already made incremental progress for this track.

## See Also

- [var segmentFileOutputURL: URL](avplannedsegmentwritingrequest/segmentfileoutputurl.md)
- [var progress: Float](avplannedsegmentwritingrequest/progress.md)
- [var assemblyTrackID: CMPersistentTrackID](avplannedsegmentwritingrequest/assemblytrackid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/timerange)*