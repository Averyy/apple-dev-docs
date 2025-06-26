# creationDate

**Framework**: AVFoundation  
**Kind**: property

A metadata item that indicates the creation date of an asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var creationDate: AVAsyncProperty<Root, AVMetadataItem?> { get }
```

#### Discussion

Use the [`load(_:isolation:)`](avasynchronouskeyvalueloading/load(_:isolation:).md) method to retrieve the property value.

If the asset stores a creation date in a form the system can convert to an [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate), the metadata item’s [`dateValue`](avmetadataitem/datevalue.md) property contains a valid date. Otherwise, the creation date is available only as a string that you retrieve by calling the metadata item’s [`stringValue`](avmetadataitem/stringvalue.md) property.

This property may be `nil`.

## See Also

- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/metadata-16qej.md)
  The metadata items that an asset contains for all metadata identifiers.
- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/commonmetadata-3j3n4.md)
  The metadata items that an asset contains for common metadata identifiers.
- [static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]>](avpartialasyncproperty/availablemetadataformats-4yiq8.md)
  The formats of metadata that an asset contains.
- [func loadMetadata(for: AVMetadataFormat, completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](avasset/loadmetadata(for:completionhandler:).md)
  Loads an array of metadata items that the asset contains for the specified format.
- [static var lyrics: AVAsyncProperty<Root, String?>](avpartialasyncproperty/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/creationdate)*