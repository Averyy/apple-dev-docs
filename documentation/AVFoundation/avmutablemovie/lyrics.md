# lyrics

**Framework**: AVFoundation  
**Kind**: property

The lyrics of the asset in a language suitable for the current locale.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var lyrics: String? { get }
```

## See Also

- [var metadata: [AVMetadataItem]](avmutablemovie/metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [var commonMetadata: [AVMetadataItem]](avmutablemovie/commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avmutablemovie/availablemetadataformats.md)
  The metadata formats this asset contains.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avmutablemovie/metadata(forformat:).md)
  Returns an array of metadata items from the container with the specified format.
- [var creationDate: AVMetadataItem?](avmutablemovie/creationdate.md)
  A metadata item that indicates the asset’s creation date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/lyrics)*