# init(timeRange:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates an object that presents an empty composition track segment.

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
init(timeRange: CMTimeRange)
```

```objc
- (instancetype) initWithTimeRange:(CMTimeRange) timeRange;
```

## Parameters

- `timeRange`: The time range of the empty track segment.

## See Also

### Creating a segment
- [init(url: URL, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)](./init%28url,trackid,sourcetimerange,targettimerange%29-4rc2g.md)
  Creates an object that presents a segment of a media file that the specified URL references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/init(timerange:))*