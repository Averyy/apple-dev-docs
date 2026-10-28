# metadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of metadata items for all metadata identifiers for which a value is available.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.10+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`metadata`](../avpartialasyncproperty/metadata-16qej.md) asynchronously instead.

## Declaration

```swift
var metadata: [AVMetadataItem] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVMetadataItem *> * metadata;
```

## Discussion

You can filter the metadata items by language using the [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](../avmetadataitem/metadataitems%28from,filteredandsortedaccordingtopreferredlanguages%29.md) method, or by identifier with the [`metadataItems(from:filteredByIdentifier:)`](../avmetadataitem/metadataitems%28from,filteredbyidentifier%29.md) method.

## See Also

### Accessing metadata
- [commonMetadata](./commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [availableMetadataFormats](./availablemetadataformats.md)
  The metadata formats this asset contains.
- [- metadataForFormat:](./metadata%28forformat%29.md)
  Returns an array of metadata items from the container with the specified format.
- [creationDate](./creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [lyrics](./lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/metadata)*