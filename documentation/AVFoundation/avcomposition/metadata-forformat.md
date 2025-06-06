# metadata(forFormat:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array of metadata items from the container with the specified format.

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

An array of [`AVMetadataItem`](avmetadataitem.md) objects, one for each metadata item in the container of the specified format, or an empty array if there is no metadata for the specified format.

#### Discussion

You can filter the array to the specific items of interest using the class methods provided by [`AVMetadataItem`](avmetadataitem.md), like [`metadataItems(from:filteredByIdentifier:)`](avmetadataitem/metadataitems(from:filteredbyidentifier:).md) or [`metadataItems(from:with:)`](avmetadataitem/metadataitems(from:with:).md).

You can call this method without blocking the current thread after you’ve asynchronously loaded the [`availableMetadataFormats`](avasset/availablemetadataformats.md) property.

## Parameters

- `format`: The metadata format for which you want items.

## See Also

- [var metadata: [AVMetadataItem]](avcomposition/metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [var commonMetadata: [AVMetadataItem]](avcomposition/commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avcomposition/availablemetadataformats.md)
  The metadata formats this asset contains.
- [var creationDate: AVMetadataItem?](avcomposition/creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [var lyrics: String?](avcomposition/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/metadata(forformat:))*