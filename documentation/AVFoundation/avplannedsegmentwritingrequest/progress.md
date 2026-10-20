# progress

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current progress for the track identified by assemblyTrackID.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var progress: Float { get }
```

```objc
@property (readonly) float progress;
```

#### Discussion

Returns a float value between 0.0 and 1.0 representing the percentage of duration completed for this track. This value is updated as segments are completed.

## See Also

### Inspecting the request
- [var timeRange: CMTimeRange](./timerange.md)
  The PTS range for this segment.
- [var segmentFileOutputURL: URL](./segmentfileoutputurl.md)
  The URL of the file where this incremental segment should be written to.
- [var assemblyTrackID: CMPersistentTrackID](./assemblytrackid.md)
  The trackID identifies which track should be written to this segment file. This is the same track ID in the AVAssetTrackPlan object. This is also the trackID the AVAssetWritingPlanner uses to build the assembled AVComposition before it calls the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/progress)*