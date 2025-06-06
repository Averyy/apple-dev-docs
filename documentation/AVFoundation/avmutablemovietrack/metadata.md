# metadata

**Framework**: AVFoundation  
**Kind**: property

An array of metadata stored by the track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var metadata: [AVMetadataItem] { get set }
```

## See Also

- [var commonMetadata: [AVMetadataItem]](avmutablemovietrack/commonmetadata.md)
  An array of metadata items for all common metadata keys that have a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avmutablemovietrack/availablemetadataformats.md)
  An array of metadata formats available for the track.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avmutablemovietrack/metadata(forformat:).md)
  Returns metadata items that a track contains for the specified format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/metadata)*