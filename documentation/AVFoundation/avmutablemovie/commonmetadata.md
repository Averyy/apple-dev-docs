# commonMetadata

**Framework**: AVFoundation  
**Kind**: property

The metadata items an asset contains for common metadata identifiers that provide a value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var commonMetadata: [AVMetadataItem] { get }
```

#### Discussion

This property value is an array of metadata items, one for each metadata key from the common key space for which the asset has an available value. You can use the various class methods provided by [`AVMetadataItem`](avmetadataitem.md), such as [`metadataItems(from:filteredByIdentifier:)`](avmetadataitem/metadataitems(from:filteredbyidentifier:).md) or [`metadataItems(from:with:)`](avmetadataitem/metadataitems(from:with:).md) to filter the array to the specific items of interest.

## See Also

- [var metadata: [AVMetadataItem]](avmutablemovie/metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [var availableMetadataFormats: [AVMetadataFormat]](avmutablemovie/availablemetadataformats.md)
  The metadata formats this asset contains.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avmutablemovie/metadata(forformat:).md)
  Returns an array of metadata items from the container with the specified format.
- [var creationDate: AVMetadataItem?](avmutablemovie/creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [var lyrics: String?](avmutablemovie/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/commonmetadata)*