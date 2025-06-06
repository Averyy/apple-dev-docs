# commonMetadata

**Framework**: AVFoundation  
**Kind**: property

The metadata items an asset contains for common metadata identifiers that provide a value.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var commonMetadata: [AVMetadataItem] { get }
```

#### Discussion

This property value is an array of metadata items, one for each metadata key from the common key space for which the asset has an available value. You can use the various class methods provided by [`AVMetadataItem`](avmetadataitem.md), such as [`metadataItems(from:filteredByIdentifier:)`](avmetadataitem/metadataitems(from:filteredbyidentifier:).md) or [`metadataItems(from:with:)`](avmetadataitem/metadataitems(from:with:).md) to filter the array to the specific items of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/commonmetadata)*