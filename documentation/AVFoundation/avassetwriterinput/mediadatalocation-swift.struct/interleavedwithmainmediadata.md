# interleavedWithMainMediaData

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A value that indicates to interleave the input’s media data with other media data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let interleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation
```

```c
extern AVAssetWriterInputMediaDataLocation const AVAssetWriterInputMediaDataLocationInterleavedWithMainMediaData;
```

## See Also

### Media data locations
- [static let beforeMainMediaDataNotInterleaved: AVAssetWriterInput.MediaDataLocation](./beforemainmediadatanotinterleaved.md)
  A value that indicates to use noninterleaved data, and write it before interleaved data.
- [static let sparselyInterleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation](./sparselyinterleavedwithmainmediadata.md)
  Indicates that there may be large segments of time without any media data from this track. When mediaDataLocation is set to this value, AVAssetWriter will interleave the media data, but will not wait for media data from this track to achieve tight interleaving with other tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct/interleavedwithmainmediadata)*