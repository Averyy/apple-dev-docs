# commonMetadata

**Framework**: AVFoundation  
**Kind**: property

The metadata items that an asset contains for common metadata identifiers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]> { get }
```

## Mentions

- [Retrieving media metadata](retrieving-media-metadata.md)

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

The value contains an array of metadata items that contain an [`identifier`](avmetadataitem/identifier.md) value from the set of Common Metadata Identifiers.

You can filter items in this array according to language by calling [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md), or by identifier by calling [`metadataItems(from:filteredByIdentifier:)`](avmetadataitem/metadataitems(from:filteredbyidentifier:).md).

## See Also

- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/metadata-16qej.md)
  The metadata items that an asset contains for all metadata identifiers.
- [static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]>](avpartialasyncproperty/availablemetadataformats-4yiq8.md)
  The formats of metadata that an asset contains.
- [func loadMetadata(for: AVMetadataFormat, completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](avasset/loadmetadata(for:completionhandler:).md)
  Loads an array of metadata items that the asset contains for the specified format.
- [static var creationDate: AVAsyncProperty<Root, AVMetadataItem?>](avpartialasyncproperty/creationdate.md)
  A metadata item that indicates the creation date of an asset.
- [static var lyrics: AVAsyncProperty<Root, String?>](avpartialasyncproperty/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/commonmetadata-3j3n4)*