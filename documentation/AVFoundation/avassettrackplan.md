# AVAssetTrackPlan

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
class AVAssetTrackPlan
```

#### Overview

AVAssetTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.

Call AVAssetWritingPlanner’s “planTrack:withSegmentsGeneratedBy:” method to add an AVAssetTrackPlan to the planner to include it in the incremental writing session.

## Topics

### Creating a track plan
- [init(mediaType: AVMediaType, segmentConfigurations: [AVPlannedSegmentConfiguration], assemblyTrackID: CMPersistentTrackID)](avassettrackplan/init(mediatype:segmentconfigurations:assemblytrackid:).md)
### Inspecting the track plan
- [var mediaType: AVMediaType](avassettrackplan/mediatype.md)
- [var segmentConfigurations: [AVPlannedSegmentConfiguration]](avassettrackplan/segmentconfigurations.md)
- [var assemblyTrackID: CMPersistentTrackID](avassettrackplan/assemblytrackid.md)

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

- [class AVAssetVideoTrackPlan](avassetvideotrackplan.md)
- [class AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md)
- [class AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md)
- [class AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md)
- [class AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackplan)*