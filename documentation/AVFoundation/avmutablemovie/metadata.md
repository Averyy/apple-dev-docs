# metadata

**Framework**: AVFoundation  
**Kind**: property

An array of metadata items for all metadata identifiers for which a value is available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var metadata: [AVMetadataItem] { get set }
```

#### Discussion

You can filter the metadata items by language using the [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md) method, or by identifier with the [`metadataItems(from:filteredByIdentifier:)`](avmetadataitem/metadataitems(from:filteredbyidentifier:).md) method.

## See Also

- [var commonMetadata: [AVMetadataItem]](avmutablemovie/commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avmutablemovie/availablemetadataformats.md)
  The metadata formats this asset contains.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avmutablemovie/metadata(forformat:).md)
  Returns an array of metadata items from the container with the specified format.
- [var creationDate: AVMetadataItem?](avmutablemovie/creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [var lyrics: String?](avmutablemovie/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/metadata)*