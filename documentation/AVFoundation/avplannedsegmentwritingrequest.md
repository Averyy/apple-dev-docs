# AVPlannedSegmentWritingRequest

**Framework**: AVFoundation  
**Kind**: class

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

AVPlannedSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental track segment.

The client should respond to this request by writing the specified time range of data to a movie file at the specified segmentFileOutputURL, with start PTS zero.  The client’s writing work may be completed asynchronously.  If it completes successfully, clients must call the `-finish` or `-finishWithClientState` method on the request object.  If writing the segment fails, clients must call the `-finishWithError:` method on the request object.  If segment writing needs to be stopped before reaching the end of the segment, clients must call `-cancel`.

## Topics

### Inspecting the request
- [var timeRange: CMTimeRange](avplannedsegmentwritingrequest/timerange.md)
- [var segmentFileOutputURL: URL](avplannedsegmentwritingrequest/segmentfileoutputurl.md)
- [var progress: Float](avplannedsegmentwritingrequest/progress.md)
- [var assemblyTrackID: CMPersistentTrackID](avplannedsegmentwritingrequest/assemblytrackid.md)
### Managing client state
- [var clientStateToRestore: Data?](avplannedsegmentwritingrequest/clientstatetorestore.md)

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
- [class AVAssetVideoTrackPlan](avassetvideotrackplan.md)
- [class AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md)
- [class AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md)
- [class AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest)*