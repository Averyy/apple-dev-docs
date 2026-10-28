# segment(forTrackTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Retrieves a segment with a target time range that contains, or is closest to, the specified track time.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadSegment(forTrackTime:completionHandler:)`](./loadsegment%28fortracktime,completionhandler%29.md) instead.

## Declaration

```swift
func segment(forTrackTime trackTime: CMTime) -> AVAssetTrackSegment?
```

```objc
- (AVAssetTrackSegment *) segmentForTrackTime:(CMTime) trackTime;
```

## Return Value

The track segment matching, or closest to, the specied time.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a segment asynchronously using [`loadSegment(forTrackTime:completionHandler:)`](./loadsegment%28fortracktime,completionhandler%29.md) instead.

## Parameters

- `trackTime`: The track time for which you want the segment.

## See Also

### Accessing track segments
- [segments](./segments.md)
  The time mappings from the track’s media samples to its timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/segment(fortracktime:))*