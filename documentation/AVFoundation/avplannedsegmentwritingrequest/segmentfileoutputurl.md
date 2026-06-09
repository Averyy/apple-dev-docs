# segmentFileOutputURL

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
var segmentFileOutputURL: URL { get }
```

#### Discussion

The URL of the file where this incremental segment should be written to.

AVAssetWritingPlanner will request each incremental segment to be written to a different file. If the file already exists from a previous session, the client should delete it to allow the subsequent asset writer session to succeed.

## See Also

- [var timeRange: CMTimeRange](avplannedsegmentwritingrequest/timerange.md)
- [var progress: Float](avplannedsegmentwritingrequest/progress.md)
- [var assemblyTrackID: CMPersistentTrackID](avplannedsegmentwritingrequest/assemblytrackid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/segmentfileoutputurl)*