# metadataItem(frameTimeRange:)

**Framework**: Immersive Media Support  
**Kind**: method

Builds a metadata item containing the presentation commands active at the start of the specified frame’s time range.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func metadataItem(frameTimeRange: CMTimeRange) throws -> AVMetadataItem?
```

#### Return Value

An `AVMetadataItem` whose value encodes the active presentation commands for that frame, or `nil` if none are active.

#### Discussion

This is intended to be called once per video frame. The returned item’s `time` and `duration` are set directly from `frameTimeRange`, so the caller can write it into a per-frame metadata track without further clipping or stamping. Returns `nil` if no presentation commands are active at `frameTimeRange.start`.

## Parameters

- `frameTimeRange`: The frame’s presentation time range. Its `start` is used to resolve which commands are active; the returned item is stamped with the full range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/metadataitem(frametimerange:))*