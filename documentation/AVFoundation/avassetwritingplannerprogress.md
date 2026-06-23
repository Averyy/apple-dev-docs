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

### Instance Properties
- [var overallProgress: Float](avassetwritingplannerprogress/overallprogress.md)
  The overall progress across all tracks.
### Instance Methods
- [func progress(forTrack: CMPersistentTrackID) -> Float](avassetwritingplannerprogress/progress(fortrack:).md)
  Returns the progress for a specific track identified by its assemblyTrackID.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplannerprogress)*