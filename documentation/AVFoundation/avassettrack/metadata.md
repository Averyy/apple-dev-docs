# metadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of metadata items for all metadata identifiers that have a value.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.10+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`metadata`](../avpartialasyncproperty/metadata-6e14c.md) asynchronously instead.

## Declaration

```swift
var metadata: [AVMetadataItem] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVMetadataItem *> * metadata;
```

## Discussion

You can filter the array of metadata items according to language using the [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](../avmetadataitem/metadataitems%28from,filteredandsortedaccordingtopreferredlanguages%29.md) method. Filter the results by identifier using the [`metadataItems(from:filteredByIdentifier:)`](../avmetadataitem/metadataitems%28from,filteredbyidentifier%29.md) method.

## See Also

### Accessing metadata
- [commonMetadata](./commonmetadata.md)
  An array of metadata items for all common metadata keys that have a value.
- [availableMetadataFormats](./availablemetadataformats.md)
  An array of metadata formats available for the track.
- [- metadataForFormat:](./metadata%28forformat%29.md)
  Returns metadata items that a track contains for the specified format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/metadata)*