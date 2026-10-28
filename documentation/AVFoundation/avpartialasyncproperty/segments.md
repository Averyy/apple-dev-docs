# segments

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The time mappings from the track’s media samples to its timeline.

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
static var segments: AVAsyncProperty<Root, [AVAssetTrackSegment]> { get }
```

Available when `Root` inherits `AVAssetTrack`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading track segments
- [func loadSegment(forTrackTime: CMTime, completionHandler: (AVAssetTrackSegment?, (any Error)?) -> Void)](../avassettrack/loadsegment%28fortracktime,completionhandler%29.md)
  Loads a segment with a target time range that contains, or is closest to, the specified track time.
- [func loadSamplePresentationTime(forTrackTime: CMTime, completionHandler: (CMTime, (any Error)?) -> Void)](../avassettrack/loadsamplepresentationtime%28fortracktime,completionhandler%29.md)
  Loads a sample presentation time that maps to the specified track time.
- [class AVAssetTrackSegment](../avassettracksegment.md)
  An object that represents a time range segment of an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/segments)*