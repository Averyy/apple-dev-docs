# AVAssetWritingPlannerProgress

**Framework**: AVFoundation  
**Kind**: class

AVAssetWritingPlannerProgress tracks the progress of incremental writing for each track in an AVAssetWritingPlanner session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class AVAssetWritingPlannerProgress
```

#### Overview

This class provides per-track progress information as a percentage of the total duration completed. Progress can be queried by assemblyTrackID.

## Topics

### Getting progress
- [var overallProgress: Float](avassetwritingplannerprogress/overallprogress.md)
  The overall progress across all tracks.
- [func progress(forTrack: CMPersistentTrackID) -> Float](avassetwritingplannerprogress/progress(fortrack:).md)
  Returns the progress for a specific track identified by its assemblyTrackID.
- [func progress(forTrack: CMPersistentTrackID) -> Float](avassetwritingplannerprogress/progress(fortrack:).md)
  Returns the progress for a specific track identified by its assemblyTrackID.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AVAssetWritingPlanner](avassetwritingplanner.md)
  AVAssetWritingPlanner orchestrates incremental writing of media files.
- [class AVAssetTrackPlan](avassettrackplan.md)
  AVAssetTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplannerprogress)*