# init(url:trackID:sourceTimeRange:targetTimeRange:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates an object that presents a segment of a media file that the specified URL references.

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
init(url URL: URL, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL trackID:(CMPersistentTrackID) trackID sourceTimeRange:(CMTimeRange) sourceTimeRange targetTimeRange:(CMTimeRange) targetTimeRange;
```

## Parameters

- `URL`: A URL of the source media file.
- `trackID`: The identifier of the track whose media this segment presents.
- `sourceTimeRange`: The time range of the track whose media this segment presents.
- `targetTimeRange`: The time range of the composition track to present the segment’s media.

## See Also

### Creating a segment
- [init(timeRange: CMTimeRange)](./init%28timerange%29.md)
  Creates an object that presents an empty composition track segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/init(url:trackid:sourcetimerange:targettimerange:)-4rc2g)*