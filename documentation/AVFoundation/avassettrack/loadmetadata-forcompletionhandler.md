# loadMetadata(for:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Loads metadata items that a track contains for the specified format.

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
func loadMetadata(for format: AVMetadataFormat) async throws -> [AVMetadataItem]
```

## Parameters

- `format`: The format of the metadata items to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

## See Also

- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/metadata-6e14c.md)
  An array of metadata items for all metadata identifiers that have a value.
- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/commonmetadata-73m58.md)
  An array of metadata items for all common metadata keys that have a value.
- [static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]>](avpartialasyncproperty/availablemetadataformats-5p9xg.md)
  An array of metadata formats available for the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/loadmetadata(for:completionhandler:))*