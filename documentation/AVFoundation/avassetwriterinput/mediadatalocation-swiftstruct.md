# AVAssetWriterInput.MediaDataLocation

**Framework**: AVFoundation  
**Kind**: struct

A structure that indicates how to lay out and interleave media data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct MediaDataLocation
```

## Topics

### Media Data Locations
- [static let interleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct/interleavedwithmainmediadata.md)
  A value that indicates to interleave the input’s media data with other media data.
- [static let beforeMainMediaDataNotInterleaved: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct/beforemainmediadatanotinterleaved.md)
  A value that indicates to use noninterleaved data, and write it before interleaved data.
### Initializers
- [init(rawValue: String)](avassetwriterinput/mediadatalocation-swift.struct/init(rawvalue:).md)
  Creates a location with a string value.
### Type Properties
- [static let sparselyInterleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct/sparselyinterleavedwithmainmediadata.md)
  Indicates that there may be large segments of time without any media data from this track. When mediaDataLocation is set to this value, AVAssetWriter will interleave the media data, but will not wait for media data from this track to achieve tight interleaving with other tracks.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var preferredMediaChunkAlignment: Int](avassetwriterinput/preferredmediachunkalignment.md)
  The boundary, in bytes, for aligning media chunks.
- [var preferredMediaChunkDuration: CMTime](avassetwriterinput/preferredmediachunkduration.md)
  The duration to use for each chunk of sample data in the output file.
- [var sampleReferenceBaseURL: URL?](avassetwriterinput/samplereferencebaseurl.md)
  The base URL sample references are relative to.
- [var mediaDataLocation: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.property.md)
  Specifies how the input lays out and interleaves media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct)*