# lyrics

**Framework**: AVFoundation  
**Kind**: property

The lyrics of the asset in a language suitable for the current locale.

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
static var lyrics: AVAsyncProperty<Root, String?> { get }
```

#### Discussion

Use the `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the property value.

## See Also

- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/metadata-16qej.md)
  The metadata items that an asset contains for all metadata identifiers.
- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/commonmetadata-3j3n4.md)
  The metadata items that an asset contains for common metadata identifiers.
- [static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]>](avpartialasyncproperty/availablemetadataformats-4yiq8.md)
  The formats of metadata that an asset contains.
- [func loadMetadata(for: AVMetadataFormat, completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](avasset/loadmetadata(for:completionhandler:).md)
  Loads an array of metadata items that the asset contains for the specified format.
- [static var creationDate: AVAsyncProperty<Root, AVMetadataItem?>](avpartialasyncproperty/creationdate.md)
  A metadata item that indicates the creation date of an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/lyrics)*