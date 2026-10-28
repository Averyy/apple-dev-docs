# metadata(forFormat:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns metadata items that a track contains for the specified format.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func metadata(forFormat format: AVMetadataFormat) -> [AVMetadataItem]
```

```objc
- (NSArray<AVMetadataItem *> *) metadataForFormat:(AVMetadataFormat) format;
```

## Return Value

An array of metadata items matching the specified format, or an empty array if none are found.

## Parameters

- `format`: The format of the metadata items to retrieve.

## See Also

### Accessing metadata
- [var metadata: [AVMetadataItem]](./metadata.md)
  An array of metadata items for all metadata identifiers that have a value.
- [var commonMetadata: [AVMetadataItem]](./commonmetadata.md)
  An array of metadata items for all common metadata keys that have a value.
- [var availableMetadataFormats: [AVMetadataFormat]](./availablemetadataformats.md)
  An array of metadata formats available for the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/metadata(forformat:))*