# metadata

**Framework**: AVFoundation  
**Kind**: property

The metadata items that an asset contains for all metadata identifiers.

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
static var metadata: AVAsyncProperty<Root, [AVMetadataItem]> { get }
```

## Mentions

- [Retrieving media metadata](retrieving-media-metadata.md)
- [Loading media data asynchronously](loading-media-data-asynchronously.md)

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

You can filter items in the array according to language by calling [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md), or by identifier by calling [`metadataItems(from:filteredByIdentifier:)`](avmetadataitem/metadataitems(from:filteredbyidentifier:).md).

## See Also

- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/commonmetadata-3j3n4.md)
  The metadata items that an asset contains for common metadata identifiers.
- [static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]>](avpartialasyncproperty/availablemetadataformats-4yiq8.md)
  The formats of metadata that an asset contains.
- [func loadMetadata(for: AVMetadataFormat, completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](avasset/loadmetadata(for:completionhandler:).md)
  Loads an array of metadata items that the asset contains for the specified format.
- [static var creationDate: AVAsyncProperty<Root, AVMetadataItem?>](avpartialasyncproperty/creationdate.md)
  A metadata item that indicates the creation date of an asset.
- [static var lyrics: AVAsyncProperty<Root, String?>](avpartialasyncproperty/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/metadata-16qej)*