# sampleReferenceBaseURL

**Framework**: AVFoundation  
**Kind**: property

The base URL sample references are relative to.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sampleReferenceBaseURL: URL? { get set }
```

#### Discussion

This property is only valid for file types that support writing sample references, such as QuickTime files. If the system resolves the value of this property to an absolute URL, the sample references it appends are relative to this URL. The URL must point to a location that’s in a directory that’s a parent of the sample reference location.

For example, setting the value of this property to `file:///User/johnappleseed/Movies/` and appending sample buffers with the [`kCMSampleBufferAttachmentKey_SampleReferenceURL`](https://developer.apple.com/documentation/CoreMedia/kCMSampleBufferAttachmentKey_SampleReferenceURL) attachment set to `file:///User/johnappleseed/Movies/data/movie1.mov` writes a sample reference of `data/movie1.mov` to the movie.

## See Also

- [var preferredMediaChunkAlignment: Int](avassetwriterinput/preferredmediachunkalignment.md)
  The boundary, in bytes, for aligning media chunks.
- [var preferredMediaChunkDuration: CMTime](avassetwriterinput/preferredmediachunkduration.md)
  The duration to use for each chunk of sample data in the output file.
- [var mediaDataLocation: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.property.md)
  Specifies how the input lays out and interleaves media data.
- [AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct.md)
  A structure that indicates how to lay out and interleave media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplereferencebaseurl)*