# init(url:trackID:sourceTimeRange:targetTimeRange:)

**Framework**: AVFoundation  
**Kind**: init

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

## Parameters

- `URL`: A URL of the source media file.
- `trackID`: The identifier of the track whose media this segment presents.
- `sourceTimeRange`: The time range of the track whose media this segment presents.
- `targetTimeRange`: The time range of the composition track to present the segment’s media.

## See Also

- [init(timeRange: CMTimeRange)](avcompositiontracksegment/init(timerange:).md)
  Creates an object that presents an empty composition track segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/init(url:trackid:sourcetimerange:targettimerange:))*