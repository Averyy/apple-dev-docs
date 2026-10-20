# sampleReferenceBaseURL

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) NSURL * sampleReferenceBaseURL;
```

#### Discussion

This property is only valid for file types that support writing sample references, such as QuickTime files. If the system resolves the value of this property to an absolute URL, the sample references it appends are relative to this URL. The URL must point to a location that’s in a directory that’s a parent of the sample reference location.

For example, setting the value of this property to `file:///User/johnappleseed/Movies/` and appending sample buffers with the [`kCMSampleBufferAttachmentKey_SampleReferenceURL`](../../CoreMedia/kcmsamplebufferattachmentkey_samplereferenceurl.md) attachment set to `file:///User/johnappleseed/Movies/data/movie1.mov` writes a sample reference of `data/movie1.mov` to the movie.

## See Also

### Configuring media data layout
- [var preferredMediaChunkAlignment: Int](./preferredmediachunkalignment.md)
  The boundary, in bytes, for aligning media chunks.
- [var preferredMediaChunkDuration: CMTime](./preferredmediachunkduration.md)
  The duration to use for each chunk of sample data in the output file.
- [var mediaDataLocation: AVAssetWriterInput.MediaDataLocation](./mediadatalocation-swift.property.md)
  Specifies how the input lays out and interleaves media data.
- [AVAssetWriterInput.MediaDataLocation](./mediadatalocation-swift.struct.md)
  A structure that indicates how to lay out and interleave media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplereferencebaseurl)*