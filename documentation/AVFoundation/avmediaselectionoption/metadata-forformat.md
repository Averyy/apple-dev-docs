# metadata(forFormat:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array of metadata items—one for each metadata item in the container of a given format.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func metadata(forFormat format: String) -> [AVMetadataItem]
```

#### Return Value

An array of `AVMetadataItem` objects, one for each metadata item in the container of format, or `nil` if there is no metadata of the specified format.

## Parameters

- `format`: The metadata format for which items are requested.

## See Also

- [var commonMetadata: [AVMetadataItem]](avmediaselectionoption/commonmetadata.md)
  An array of metadata items for each common metadata key for which a value is available.
- [var availableMetadataFormats: [String]](avmediaselectionoption/availablemetadataformats.md)
  The metadata formats that contain metadata associated with the option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/metadata(forformat:))*