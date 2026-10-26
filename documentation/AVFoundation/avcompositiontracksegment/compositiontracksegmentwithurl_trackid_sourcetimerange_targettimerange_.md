# compositionTrackSegmentWithURL:trackID:sourceTimeRange:targetTimeRange:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new an object that presents a segment of a media file that the specified URL references.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
+ (instancetype) compositionTrackSegmentWithURL:(NSURL *) URL trackID:(CMPersistentTrackID) trackID sourceTimeRange:(CMTimeRange) sourceTimeRange targetTimeRange:(CMTimeRange) targetTimeRange;
```

#### Return Value

A new composition track segment.

## Parameters

- `URL`: A URL of the source media file.
- `trackID`: The identifier of the track whose media this segment presents.
- `sourceTimeRange`: The time range of the track whose media this segment presents.
- `targetTimeRange`: The time range of the composition track to present the segment’s media.

## See Also

### Creating a segment
- [+ compositionTrackSegmentWithTimeRange:](./compositiontracksegmentwithtimerange_.md)
  Returns a new object that presents an empty composition track segment.
- [init(timeRange: CMTimeRange)](./init%28timerange%29.md)
  Creates an object that presents an empty composition track segment.
- [init(url: URL, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)](./init%28url,trackid,sourcetimerange,targettimerange%29-4rc2g.md)
  Creates an object that presents a segment of a media file that the specified URL references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/compositiontracksegmentwithurl:trackid:sourcetimerange:targettimerange:)*