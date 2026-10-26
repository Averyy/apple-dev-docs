# AVCompositionTrackSegment

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCompositionTrackSegment : AVAssetTrackSegment
```

#### Overview

You typically use this class to save a low-level representation of a composition.

## Topics

### Creating a segment
- [init(timeRange: CMTimeRange)](./avcompositiontracksegment/init%28timerange%29.md)
  Creates an object that presents an empty composition track segment.
- [init(url: URL, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)](./avcompositiontracksegment/init%28url,trackid,sourcetimerange,targettimerange%29-4rc2g.md)
  Creates an object that presents a segment of a media file that the specified URL references.
- [+ compositionTrackSegmentWithTimeRange:](./avcompositiontracksegment/compositiontracksegmentwithtimerange_.md)
  Returns a new object that presents an empty composition track segment.
- [+ compositionTrackSegmentWithURL:trackID:sourceTimeRange:targetTimeRange:](./avcompositiontracksegment/compositiontracksegmentwithurl_trackid_sourcetimerange_targettimerange_.md)
  Returns a new an object that presents a segment of a media file that the specified URL references.
### Accessing segment properties
- [var sourceURL: URL?](./avcompositiontracksegment/sourceurl.md)
  A URL of the container file whose media this track segment presents.
- [var sourceTrackID: CMPersistentTrackID](./avcompositiontracksegment/sourcetrackid.md)
  An identifier of a track in the container file whose media this track segment presents.
- [var isEmpty: Bool](./avcompositiontracksegment/isempty.md)
  A Boolean value that indicates whether the segment is empty.
### Initializers
- [init(URL: URL, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)](./avcompositiontracksegment/init%28url,trackid,sourcetimerange,targettimerange%29-9shbx.md)
- [convenience init(URL: URL, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)](./avcompositiontracksegment/init%28url,trackid,sourcetimerange,targettimerange%29-qoz.md)

## Relationships

### Inherits From
- [AVAssetTrackSegment](./avassettracksegment.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Compositions
- [class AVComposition](./avcomposition.md)
  An object that combines and arranges media from multiple assets into a single composite asset that you can play or process.
- [class AVCompositionTrack](./avcompositiontrack.md)
  A track in a composition that presents media of a uniform type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment)*