# creationDate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A metadata item that indicates the creation date of an asset.

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
static var creationDate: AVAsyncProperty<Root, AVMetadataItem?> { get }
```

Available when `Root` inherits `AVAsset`.

#### Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

If the asset stores a creation date in a form the system can convert to an [`NSDate`](../../Foundation/nsdate.md), the metadata item’s [`dateValue`](../avmetadataitem/datevalue.md) property contains a valid date. Otherwise, the creation date is available only as a string that you retrieve by calling the metadata item’s [`stringValue`](../avmetadataitem/stringvalue.md) property.

This property may be `nil`.

## See Also

### Loading metadata
- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](./metadata-16qej.md)
  The metadata items that an asset contains for all metadata identifiers.
- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](./commonmetadata-3j3n4.md)
  The metadata items that an asset contains for common metadata identifiers.
- [static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]>](./availablemetadataformats-4yiq8.md)
  The formats of metadata that an asset contains.
- [func loadMetadata(for: AVMetadataFormat, completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](../avasset/loadmetadata%28for,completionhandler%29.md)
  Loads an array of metadata items that the asset contains for the specified format.
- [static var lyrics: AVAsyncProperty<Root, String?>](./lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/creationdate)*