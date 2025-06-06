# preferredMediaChunkAlignment

**Framework**: AVFoundation  
**Kind**: property

The boundary, in bytes, for aligning media chunks.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preferredMediaChunkAlignment: Int { get set }
```

#### Discussion

This property supports file types that support media chunk alignment, such as QuickTime Movie files. The default value is `0`, which means that the input chooses an appropriate default value. A value of `1` indicates not to use padding to achieve a particular chunk alignment. It’s an error to set a negative value for chunk alignment.

You can’t set this value after writing starts.

## See Also

- [var preferredMediaChunkDuration: CMTime](avassetwriterinput/preferredmediachunkduration.md)
  The duration to use for each chunk of sample data in the output file.
- [var sampleReferenceBaseURL: URL?](avassetwriterinput/samplereferencebaseurl.md)
  The base URL sample references are relative to.
- [var mediaDataLocation: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.property.md)
  Specifies how the input lays out and interleaves media data.
- [AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct.md)
  A structure that indicates how to lay out and interleave media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/preferredmediachunkalignment)*