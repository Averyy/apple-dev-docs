# AVAssetVideoTrackPlan

**Framework**: AVFoundation  
**Kind**: class

AVAssetVideoTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class AVAssetVideoTrackPlan
```

#### Overview

Call AVAssetWritingPlanner’s “planTrack:withSegmentsGeneratedBy:” method to add an AVAssetTrackPlan to the planner’s plan to include it in the incremental writing session. Use this class instead of the base class AVAssetTrackPlan if you are setting up AVAssetWriter with video compression. This configuration hints to the planner that it must coordinate segment boundaries transitions between segments. This is abstracted from the client via using either the resumableAssetWriterInputWithMediaType or createResumableCompressionSessionWithAllocator helper functions within the AVPlannedVideoSegmentWritingRequest.

## Topics

### Creating a video track plan
- [convenience init(videoCodecType: AVVideoCodecType, encoderSpecification: [String : any Sendable]?, mediaType: AVMediaType, segmentConfigurations: [AVPlannedVideoSegmentConfiguration], assemblyTrackID: CMPersistentTrackID)](avassetvideotrackplan/init(videocodectype:encoderspecification:mediatype:segmentconfigurations:assemblytrackid:).md)
  Creates an instance of AVAssetVideoTrackPlan.
### Inspecting the video track plan
- [var videoCodecType: AVVideoCodecType](avassetvideotrackplan/videocodectype.md)
  Video codec type of this track

## Relationships

### Inherits From
- [AVAssetTrackPlan](avassettrackplan.md)
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
- [class AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md)
  AVPlannedSegmentConfiguration describes the requirements for a planned segment in an incremental writing session executed by the AVAssetWritingPlanner. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.
- [class AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md)
  AVPlannedVideoSegmentConfiguration describes the requirements for a planned video segment in an incremental writing session executed by the AVAssetWritingPlanner.
- [class AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md)
  AVPlannedSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental track segment.
- [class AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md)
  AVPlannedVideoSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental video track segment with compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvideotrackplan)*