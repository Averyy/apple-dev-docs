# metadata(forFormat:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array of metadata items from the container with the specified format.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func metadata(forFormat format: AVMetadataFormat) -> [AVMetadataItem]
```

#### Return Value

An array of [`AVMetadataItem`](avmetadataitem.md) objects, one for each metadata item in the container of the specified format, or an empty array if there is no metadata for the specified format.

#### Discussion

You can filter the array to the specific items of interest using the class methods provided by [`AVMetadataItem`](avmetadataitem.md), like [`metadataItems(from:filteredByIdentifier:)`](avmetadataitem/metadataitems(from:filteredbyidentifier:).md) or [`metadataItems(from:with:)`](avmetadataitem/metadataitems(from:with:).md).

You can call this method without blocking the current thread after you’ve asynchronously loaded the [`availableMetadataFormats`](avasset/availablemetadataformats.md) property.

## Parameters

- `format`: The metadata format for which you want items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/metadata(forformat:))*