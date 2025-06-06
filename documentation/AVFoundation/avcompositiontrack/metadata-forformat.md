# metadata(forFormat:)

**Framework**: AVFoundation  
**Kind**: method

Returns metadata items that a track contains for the specified format.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func metadata(forFormat format: AVMetadataFormat) -> [AVMetadataItem]
```

#### Return Value

An array of metadata items matching the specified format, or an empty array if none are found.

## Parameters

- `format`: The format of the metadata items to retrieve.

## See Also

- [var metadata: [AVMetadataItem]](avcompositiontrack/metadata.md)
  An array of metadata items for all metadata identifiers that have a value.
- [var commonMetadata: [AVMetadataItem]](avcompositiontrack/commonmetadata.md)
  An array of metadata items for all common metadata keys that have a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avcompositiontrack/availablemetadataformats.md)
  An array of metadata formats available for the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/metadata(forformat:))*