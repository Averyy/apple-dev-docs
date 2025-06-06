# AVCompositionTrackSegment

**Framework**: AVFoundation  
**Kind**: class

A track segment that maps a time from the source media track to the composition track.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVCompositionTrackSegment
```

#### Overview

You typically use this class to save a low-level representation of a composition.

## Topics

### Creating a Segment
- [init(timeRange: CMTimeRange)](avcompositiontracksegment/init(timerange:).md)
  Creates an object that presents an empty composition track segment.
- [init(url: URL, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)](avcompositiontracksegment/init(url:trackid:sourcetimerange:targettimerange:).md)
  Creates an object that presents a segment of a media file that the specified URL references.
### Accessing Segment Properties
- [var sourceURL: URL?](avcompositiontracksegment/sourceurl.md)
  A URL of the container file whose media this track segment presents.
- [var sourceTrackID: CMPersistentTrackID](avcompositiontracksegment/sourcetrackid.md)
  An identifier of a track in the container file whose media this track segment presents.
- [var isEmpty: Bool](avcompositiontracksegment/isempty.md)
  A Boolean value that indicates whether the segment is empty.

## Relationships

### Inherits From
- [AVAssetTrackSegment](avassettracksegment.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVComposition](avcomposition.md)
  An object that combines and arranges media from multiple assets into a single composite asset that you can play or process.
- [class AVCompositionTrack](avcompositiontrack.md)
  A track in a composition that presents media of a uniform type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment)*