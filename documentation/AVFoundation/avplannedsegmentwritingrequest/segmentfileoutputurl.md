# segmentFileOutputURL

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The URL of the file where this incremental segment should be written to.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var segmentFileOutputURL: URL { get }
```

```objc
@property (readonly) NSURL * segmentFileOutputURL;
```

## Discussion

AVAssetWritingPlanner will request each incremental segment to be written to a different file. If the file already exists from a previous session, the client should delete it to allow the subsequent asset writer session to succeed.

## See Also

### Inspecting the request
- [var timeRange: CMTimeRange](./timerange.md)
  The PTS range for this segment.
- [var progress: Float](./progress.md)
  The current progress for the track identified by assemblyTrackID.
- [var assemblyTrackID: CMPersistentTrackID](./assemblytrackid.md)
  The trackID identifies which track should be written to this segment file. This is the same track ID in the AVAssetTrackPlan object. This is also the trackID the AVAssetWritingPlanner uses to build the assembled AVComposition before it calls the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/segmentfileoutputurl)*