# metadata(forFormat:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an array of metadata items from the container with the specified format.

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

An array of [`AVMetadataItem`](../avmetadataitem.md) objects, one for each metadata item in the container of the specified format, or an empty array if there is no metadata for the specified format.

#### Discussion

You can filter the array to the specific items of interest using the class methods provided by [`AVMetadataItem`](../avmetadataitem.md), like [`metadataItems(from:filteredByIdentifier:)`](../avmetadataitem/metadataitems%28from,filteredbyidentifier%29.md) or [`metadataItems(from:with:)`](../avmetadataitem/metadataitems%28from,with%29.md).

You can call this method without blocking the current thread after you’ve asynchronously loaded the [`availableMetadataFormats`](./availablemetadataformats.md) property.

## Parameters

- `format`: The metadata format for which you want items.

## See Also

### Accessing metadata
- [metadata](./metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [commonMetadata](./commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [availableMetadataFormats](./availablemetadataformats.md)
  The metadata formats this asset contains.
- [creationDate](./creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [lyrics](./lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/metadata(forformat:))*