# segment(forTrackTime:)

**Framework**: AVFoundation  
**Kind**: method

Retrieves a segment with a target time range that contains, or is closest to, the specified track time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func segment(forTrackTime trackTime: CMTime) -> AVAssetTrackSegment?
```

#### Return Value

The track segment matching, or closest to, the specied time.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a segment asynchronously using [`loadSegment(forTrackTime:completionHandler:)`](avassettrack/loadsegment(fortracktime:completionhandler:).md) instead.

## Parameters

- `trackTime`: The track time for which you want the segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/segment(fortracktime:))*