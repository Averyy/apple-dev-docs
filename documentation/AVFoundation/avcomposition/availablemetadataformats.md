# availableMetadataFormats

**Framework**: AVFoundation  
**Kind**: property

The metadata formats this asset contains.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var availableMetadataFormats: [AVMetadataFormat] { get }
```

#### Discussion

Metadata formats may include ID3, iTunes metadata, and so on.

## See Also

- [var metadata: [AVMetadataItem]](avcomposition/metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [var commonMetadata: [AVMetadataItem]](avcomposition/commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avcomposition/metadata(forformat:).md)
  Returns an array of metadata items from the container with the specified format.
- [var creationDate: AVMetadataItem?](avcomposition/creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [var lyrics: String?](avcomposition/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/availablemetadataformats)*