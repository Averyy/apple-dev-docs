# mediaDataLocation

**Framework**: AVFoundation  
**Kind**: property

Specifies how the input lays out and interleaves media data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var mediaDataLocation: AVAssetWriterInput.MediaDataLocation { get set }
```

#### Discussion

Use this property to optimize tracks that contain a small amount of data that you need all at once, such as chapter tracks. Setting the value to [`beforeMainMediaDataNotInterleaved`](avassetwriterinput/mediadatalocation-swift.struct/beforemainmediadatanotinterleaved.md) causes the asset writer to try to write the media data for this track before interleaved inputs. For file types that support preloading media data, such as QuickTime files, setting this value also writes an indicator to the file to preload its media data.

Set the value to [`interleavedWithMainMediaData`](avassetwriterinput/mediadatalocation-swift.struct/interleavedwithmainmediadata.md) for tracks whose media data you need only as it approaches its presentation time, or when multiple inputs exist that supply media data that plays concurrently.

You can’t set this value after writing starts.

## See Also

- [var preferredMediaChunkAlignment: Int](avassetwriterinput/preferredmediachunkalignment.md)
  The boundary, in bytes, for aligning media chunks.
- [var preferredMediaChunkDuration: CMTime](avassetwriterinput/preferredmediachunkduration.md)
  The duration to use for each chunk of sample data in the output file.
- [var sampleReferenceBaseURL: URL?](avassetwriterinput/samplereferencebaseurl.md)
  The base URL sample references are relative to.
- [AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct.md)
  A structure that indicates how to lay out and interleave media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.property)*