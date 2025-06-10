# segments

**Framework**: AVFoundation  
**Kind**: property

The time mappings from the track’s media samples to its timeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var segments: AVAsyncProperty<Root, [AVAssetTrackSegment]> { get }
```

#### Discussion

Use the `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the property value.

## See Also

- [func loadSegment(forTrackTime: CMTime, completionHandler: (AVAssetTrackSegment?, (any Error)?) -> Void)](avassettrack/loadsegment(fortracktime:completionhandler:).md)
  Loads a segment with a target time range that contains, or is closest to, the specified track time.
- [func loadSamplePresentationTime(forTrackTime: CMTime, completionHandler: (CMTime, (any Error)?) -> Void)](avassettrack/loadsamplepresentationtime(fortracktime:completionhandler:).md)
  Loads a sample presentation time that maps to the specified track time.
- [class AVAssetTrackSegment](avassettracksegment.md)
  An object that represents a time range segment of an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/segments)*