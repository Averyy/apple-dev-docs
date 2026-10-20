# creationDate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A metadata item that indicates the asset’s creation date.

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
var creationDate: AVMetadataItem? { get }
```

#### Discussion

If the asset contains metadata that the framework can convert to an [`NSDate`](../../Foundation/nsdate.md), you can retrieve it from the metadata item using its [`dateValue`](../avmetadataitem/datevalue.md) property. Otherwise, you retrieve it as a string by using the metadata item’s [`stringValue`](../avmetadataitem/stringvalue.md) property.

This property value is `nil` if no creation date metadata exists.

## See Also

### Accessing metadata
- [var metadata: [AVMetadataItem]](./metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [var commonMetadata: [AVMetadataItem]](./commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [var availableMetadataFormats: [AVMetadataFormat]](./availablemetadataformats.md)
  The metadata formats this asset contains.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](./metadata%28forformat%29.md)
  Returns an array of metadata items from the container with the specified format.
- [var lyrics: String?](./lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/creationdate)*