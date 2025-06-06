# metadata

**Framework**: AVFoundation  
**Kind**: property

An array of metadata items for all metadata identifiers that have a value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var metadata: [AVMetadataItem] { get }
```

#### Discussion

You can filter the array of metadata items according to language using the [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md) method. Filter the results by identifier using the [`metadataItems(from:filteredByIdentifier:)`](avmetadataitem/metadataitems(from:filteredbyidentifier:).md) method.

## See Also

- [var commonMetadata: [AVMetadataItem]](avcompositiontrack/commonmetadata.md)
  An array of metadata items for all common metadata keys that have a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avcompositiontrack/availablemetadataformats.md)
  An array of metadata formats available for the track.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avcompositiontrack/metadata(forformat:).md)
  Returns metadata items that a track contains for the specified format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/metadata)*