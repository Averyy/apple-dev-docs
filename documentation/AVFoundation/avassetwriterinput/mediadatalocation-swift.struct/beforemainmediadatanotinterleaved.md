# beforeMainMediaDataNotInterleaved

**Framework**: AVFoundation  
**Kind**: property

A value that indicates to use noninterleaved data, and write it before interleaved data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let beforeMainMediaDataNotInterleaved: AVAssetWriterInput.MediaDataLocation
```

## See Also

- [static let interleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct/interleavedwithmainmediadata.md)
  A value that indicates to interleave the input’s media data with other media data.
- [static let sparselyInterleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct/sparselyinterleavedwithmainmediadata.md)
  Indicates that there may be large segments of time without any media data from this track. When mediaDataLocation is set to this value, AVAssetWriter will interleave the media data, but will not wait for media data from this track to achieve tight interleaving with other tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct/beforemainmediadatanotinterleaved)*