# commonMetadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The metadata items an asset contains for common metadata identifiers that provide a value.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`commonMetadata`](../avpartialasyncproperty/commonmetadata-3j3n4.md) asynchronously instead.

## Declaration

```swift
var commonMetadata: [AVMetadataItem] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVMetadataItem *> * commonMetadata;
```

#### Discussion

This property value is an array of metadata items, one for each metadata key from the common key space for which the asset has an available value. You can use the various class methods provided by [`AVMetadataItem`](../avmetadataitem.md), such as [`metadataItems(from:filteredByIdentifier:)`](../avmetadataitem/metadataitems%28from,filteredbyidentifier%29.md) or [`metadataItems(from:with:)`](../avmetadataitem/metadataitems%28from,with%29.md) to filter the array to the specific items of interest.

## See Also

### Accessing metadata
- [metadata](./metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [availableMetadataFormats](./availablemetadataformats.md)
  The metadata formats this asset contains.
- [- metadataForFormat:](./metadata%28forformat%29.md)
  Returns an array of metadata items from the container with the specified format.
- [creationDate](./creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [lyrics](./lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/commonmetadata)*