# AVAssetTrackPlan

**Framework**: AVFoundation  
**Kind**: class

AVAssetTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class AVAssetTrackPlan
```

#### Overview

Call AVAssetWritingPlanner’s “planTrack:withSegmentsGeneratedBy:” method to add an AVAssetTrackPlan to the planner to include it in the incremental writing session.

## Topics

### Creating a track plan
- [init(mediaType: AVMediaType, segmentConfigurations: [AVPlannedSegmentConfiguration], assemblyTrackID: CMPersistentTrackID)](avassettrackplan/init(mediatype:segmentconfigurations:assemblytrackid:).md)
  Returns an instance of AVAssetTrackPlan
### Inspecting the track plan
- [var mediaType: AVMediaType](avassettrackplan/mediatype.md)
  The media type of this track.
- [var segmentConfigurations: [AVPlannedSegmentConfiguration]](avassettrackplan/segmentconfigurations.md)
  Array of AVPlannedSegmentConfigurations, each element specifying the configuration of a planned segment, ordered in output PTS order.
- [var assemblyTrackID: CMPersistentTrackID](avassettrackplan/assemblytrackid.md)
  This is the track ID of this track when it is included in the assemblyComposition the planner passes to the completion handler to assemble all planned segments of all tracks into a single AVComposition.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVAssetVideoTrackPlan](avassetvideotrackplan.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAssetWritingPlanner](avassetwritingplanner.md)
  AVAssetWritingPlanner orchestrates incremental writing of media files.
- [class AVAssetWritingPlannerProgress](avassetwritingplannerprogress.md)
  AVAssetWritingPlannerProgress tracks the progress of incremental writing for each track in an AVAssetWritingPlanner session.
- [class AVAssetVideoTrackPlan](avassetvideotrackplan.md)
  AVAssetVideoTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.
- [class AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md)
  AVPlannedSegmentConfiguration describes the requirements for a planned segment in an incremental writing session executed by the AVAssetWritingPlanner. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.
- [class AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md)
  AVPlannedVideoSegmentConfiguration describes the requirements for a planned video segment in an incremental writing session executed by the AVAssetWritingPlanner.
- [class AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md)
  AVPlannedSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental track segment.
- [class AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md)
  AVPlannedVideoSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental video track segment with compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackplan)*