# metadata(forFormat:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns metadata items that a track contains for the specified format.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadMetadata(for:completionHandler:)`](./loadmetadata%28for,completionhandler%29.md) instead.

## Declaration

```swift
func metadata(forFormat format: AVMetadataFormat) -> [AVMetadataItem]
```

```objc
- (NSArray<AVMetadataItem *> *) metadataForFormat:(AVMetadataFormat) format;
```

#### Return Value

An array of metadata items matching the specified format, or an empty array if none are found.

#### Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load track metadata asynchronously using [`loadMetadata(for:completionHandler:)`](./loadmetadata%28for,completionhandler%29.md) instead.

You can call this method without blocking the current thread after you’ve loaded the [`availableMetadataFormats`](./availablemetadataformats.md) property.

## Parameters

- `format`: The format of the metadata items to retrieve.

## See Also

### Accessing metadata
- [metadata](./metadata.md)
  An array of metadata items for all metadata identifiers that have a value.
- [commonMetadata](./commonmetadata.md)
  An array of metadata items for all common metadata keys that have a value.
- [availableMetadataFormats](./availablemetadataformats.md)
  An array of metadata formats available for the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/metadata(forformat:))*