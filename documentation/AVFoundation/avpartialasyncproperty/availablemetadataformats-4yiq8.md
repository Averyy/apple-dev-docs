# availableMetadataFormats

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The formats of metadata that an asset contains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]> { get }
```

Available when `Root` inherits `AVAsset`.

## Mentions

- [Retrieving media metadata](../retrieving-media-metadata.md)

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading metadata
- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](./metadata-16qej.md)
  The metadata items that an asset contains for all metadata identifiers.
- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](./commonmetadata-3j3n4.md)
  The metadata items that an asset contains for common metadata identifiers.
- [func loadMetadata(for: AVMetadataFormat, completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](../avasset/loadmetadata%28for,completionhandler%29.md)
  Loads an array of metadata items that the asset contains for the specified format.
- [static var creationDate: AVAsyncProperty<Root, AVMetadataItem?>](./creationdate.md)
  A metadata item that indicates the creation date of an asset.
- [static var lyrics: AVAsyncProperty<Root, String?>](./lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/availablemetadataformats-4yiq8)*