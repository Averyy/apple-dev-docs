# AVPlannedSegmentWritingRequest

**Framework**: AVFoundation  
**Kind**: class

AVPlannedSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental track segment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class AVPlannedSegmentWritingRequest
```

#### Overview

The client should respond to this request by writing the specified time range of data to a movie file at the specified segmentFileOutputURL, with start PTS zero. The client’s writing work may be completed asynchronously. If it completes successfully, clients must call the `-finish` or `-finishWithClientState` method on the request object. If writing the segment fails, clients must call the `-finishWithError:` method on the request object. If segment writing needs to be stopped before reaching the end of the segment, clients must call `-cancel`.

## Topics

### Inspecting the request
- [var timeRange: CMTimeRange](avplannedsegmentwritingrequest/timerange.md)
  The PTS range for this segment.
- [var segmentFileOutputURL: URL](avplannedsegmentwritingrequest/segmentfileoutputurl.md)
  The URL of the file where this incremental segment should be written to.
- [var progress: Float](avplannedsegmentwritingrequest/progress.md)
  The current progress for the track identified by assemblyTrackID.
- [var assemblyTrackID: CMPersistentTrackID](avplannedsegmentwritingrequest/assemblytrackid.md)
  The trackID identifies which track should be written to this segment file. This is the same track ID in the AVAssetTrackPlan object. This is also the trackID the AVAssetWritingPlanner uses to build the assembled AVComposition before it calls the completion handler.
### Managing client state
- [var clientStateToRestore: Data?](avplannedsegmentwritingrequest/clientstatetorestore.md)
  The client state persisted from the previous segment, if any. Specifically, this is the NSData provided to the previous segment’s finishWithClientState: method. The client is responsible to restore its client state before writing the current segment. For example, clients such as compositors with a temporal element may need some processing history of previous samples in order to generate an output sample at time N. This will be nil for algorithms that are stateless.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAssetTrackPlan](avassettrackplan.md)
  AVAssetTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.
- [class AVAssetVideoTrackPlan](avassetvideotrackplan.md)
  AVAssetVideoTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.
- [class AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md)
  AVPlannedSegmentConfiguration describes the requirements for a planned segment in an incremental writing session executed by the AVAssetWritingPlanner. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.
- [class AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md)
  AVPlannedVideoSegmentConfiguration describes the requirements for a planned video segment in an incremental writing session executed by the AVAssetWritingPlanner.
- [class AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md)
  AVPlannedVideoSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental video track segment with compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest)*