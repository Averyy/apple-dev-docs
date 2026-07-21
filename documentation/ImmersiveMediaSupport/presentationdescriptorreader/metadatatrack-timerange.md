# metadataTrack(timeRange:)

**Framework**: Immersive Media Support  
**Kind**: method

Retrieves all metadata items to write to an output metadata track, optionally clipped to a segment time range. Pass a `timeRange` to produce one item per segment (e.g. per IDR group or per fixed-length interval).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func metadataTrack(timeRange: CMTimeRange? = nil) throws -> [AVMetadataItem]
```

#### Return Value

An array of `AVMetadataItem` objects sorted by start time.

#### Discussion

Note: the last item’s `duration` may be invalid, since the descriptor itself doesn’t know where the video ends. If you need a concrete duration (e.g. to extend the final segment to the end of the video), copy the returned item and overwrite `duration` with the valid value. Also, use the same timescale for `timeRange` as the [`PresentationCommand`](presentationcommand.md) values to avoid timescale mismatches.

## Parameters

- `timeRange`: The segment range to filter to, or `nil` to return all items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/metadatatrack(timerange:))*