# availableMetadataFormats

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The metadata formats this asset contains.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var availableMetadataFormats: [AVMetadataFormat] { get }
```

## Discussion

Metadata formats may include ID3, iTunes metadata, and so on.

## See Also

### Accessing metadata
- [var metadata: [AVMetadataItem]](./metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [var commonMetadata: [AVMetadataItem]](./commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](./metadata%28forformat%29.md)
  Returns an array of metadata items from the container with the specified format.
- [var creationDate: AVMetadataItem?](./creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [var lyrics: String?](./lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/availablemetadataformats)*