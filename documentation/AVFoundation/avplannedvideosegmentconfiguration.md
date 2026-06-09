# AVPlannedVideoSegmentConfiguration

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
class AVPlannedVideoSegmentConfiguration
```

#### Overview

AVPlannedVideoSegmentConfiguration describes the requirements for a planned video segment in an incremental writing session executed by the AVAssetWritingPlanner.

Use this class instead of the base class AVPlannedSegmentConfiguration if you are setting up AVAssetWriterInput to do video compression. AVAssetWritingPlanner will provide required video compression properties in its AVPlannedSegmentWritingRequest that are needed to prevent visual artifacts on segment boundaries.

## Topics

### Creating a video segment configuration
- [init(numberOfFrames: Int, duration: CMTime)](avplannedvideosegmentconfiguration/init(numberofframes:duration:).md)
### Inspecting the configuration
- [var frameCount: Int](avplannedvideosegmentconfiguration/framecount.md)

## Relationships

### Inherits From
- [AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md)
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
- [class AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md)
- [class AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedvideosegmentconfiguration)*