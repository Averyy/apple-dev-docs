# sparselyInterleavedWithMainMediaData

**Framework**: AVFoundation  
**Kind**: property

Indicates that there may be large segments of time without any media data from this track. When mediaDataLocation is set to this value, AVAssetWriter will interleave the media data, but will not wait for media data from this track to achieve tight interleaving with other tracks.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let sparselyInterleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation
```

## See Also

- [static let interleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct/interleavedwithmainmediadata.md)
  A value that indicates to interleave the input’s media data with other media data.
- [static let beforeMainMediaDataNotInterleaved: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct/beforemainmediadatanotinterleaved.md)
  A value that indicates to use noninterleaved data, and write it before interleaved data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct/sparselyinterleavedwithmainmediadata)*