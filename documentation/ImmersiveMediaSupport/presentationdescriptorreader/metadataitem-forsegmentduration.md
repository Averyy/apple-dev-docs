# metadataItem(for:segmentDuration:)

**Framework**: Immersive Media Support  
**Kind**: method

Retrieves the metadata item that starts at the specified presentation timestamp. Should run on the same thread with PresentationDescriptorReader.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func metadataItem(for time: CMTime, segmentDuration: CMTime? = nil) throws -> AVMetadataItem?
```

#### Return Value

The AVMetadataItem at the given timestamp, or nil if none exists.

## Parameters

- `time`: The presentation timestamp of the desired metadata.
- `segmentDuration`: Optional duration for splitting metadata items into segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/metadataitem(for:segmentduration:))*