# loadSegment(forTrackTime:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Loads a segment with a target time range that contains, or is closest to, the specified track time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func loadSegment(forTrackTime trackTime: CMTime) async throws -> AVAssetTrackSegment?
```

#### Discussion

If the specified track time doesn’t map to a sample presentation time, the system returns the segment with the closest matching time.

## Parameters

- `trackTime`: The track time of the segment to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

## See Also

- [static var segments: AVAsyncProperty<Root, [AVAssetTrackSegment]>](avpartialasyncproperty/segments.md)
  The time mappings from the track’s media samples to its timeline.
- [func loadSamplePresentationTime(forTrackTime: CMTime, completionHandler: (CMTime, (any Error)?) -> Void)](avassettrack/loadsamplepresentationtime(fortracktime:completionhandler:).md)
  Loads a sample presentation time that maps to the specified track time.
- [class AVAssetTrackSegment](avassettracksegment.md)
  An object that represents a time range segment of an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/loadsegment(fortracktime:completionhandler:))*