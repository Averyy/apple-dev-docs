# metadataTrack(segmentDuration:end:)

**Framework**: Immersive Media Support  
**Kind**: method

Retrieves all metadata items, optionally segmented and filtered by end time. Should run on the same thread with PresentationDescriptorReader.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func metadataTrack(segmentDuration: CMTime? = nil, end: CMTime? = nil) throws -> [AVMetadataItem]
```

#### Return Value

An array of AVMetadataItem objects.

## Parameters

- `segmentDuration`: Optional duration for splitting metadata items into segments.
- `end`: Optional end time to limit the range of returned metadata items. Required when the one of metadata item has no defined end time and segmentDuration is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/metadatatrack(segmentduration:end:))*