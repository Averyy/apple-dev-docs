# availableMetadataFormats

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

An array of metadata formats available for the track.

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

Available when `Root` inherits `AVAssetTrack`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading metadata
- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](./metadata-6e14c.md)
  An array of metadata items for all metadata identifiers that have a value.
- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](./commonmetadata-73m58.md)
  An array of metadata items for all common metadata keys that have a value.
- [func loadMetadata(for: AVMetadataFormat, completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](../avassettrack/loadmetadata%28for,completionhandler%29.md)
  Loads metadata items that a track contains for the specified format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/availablemetadataformats-5p9xg)*