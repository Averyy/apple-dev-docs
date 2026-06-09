# AVPlannedSegmentConfiguration

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
class AVPlannedSegmentConfiguration
```

#### Overview

AVPlannedSegmentConfiguration describes the requirements for a planned segment in an incremental writing session executed by the AVAssetWritingPlanner.   Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Topics

### Creating a segment configuration
- [init(duration: CMTime)](avplannedsegmentconfiguration/init(duration:).md)
### Inspecting the configuration
- [var duration: CMTime](avplannedsegmentconfiguration/duration.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md)
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
- [class AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md)
- [class AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md)
- [class AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentconfiguration)*