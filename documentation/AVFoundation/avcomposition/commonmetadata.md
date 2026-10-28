# commonMetadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The metadata items an asset contains for common metadata identifiers that provide a value.

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
var commonMetadata: [AVMetadataItem] { get }
```

## Discussion

This property value is an array of metadata items, one for each metadata key from the common key space for which the asset has an available value. You can use the various class methods provided by [`AVMetadataItem`](../avmetadataitem.md), such as [`metadataItems(from:filteredByIdentifier:)`](../avmetadataitem/metadataitems%28from,filteredbyidentifier%29.md) or [`metadataItems(from:with:)`](../avmetadataitem/metadataitems%28from,with%29.md) to filter the array to the specific items of interest.

## See Also

### Accessing metadata
- [var metadata: [AVMetadataItem]](./metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [var availableMetadataFormats: [AVMetadataFormat]](./availablemetadataformats.md)
  The metadata formats this asset contains.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](./metadata%28forformat%29.md)
  Returns an array of metadata items from the container with the specified format.
- [var creationDate: AVMetadataItem?](./creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [var lyrics: String?](./lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/commonmetadata)*