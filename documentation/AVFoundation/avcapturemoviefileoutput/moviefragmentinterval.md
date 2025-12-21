# movieFragmentInterval

**Framework**: AVFoundation  
**Kind**: property

The number of seconds of output that are written per fragment.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var movieFragmentInterval: CMTime { get set }
```

#### Discussion

The default is 10 seconds. To disable movie fragment writing (not typically recommended), set to [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid).

A QuickTime movie contains media samples and a table identifying their location in the file. A movie file without a sample table is unreadable.

In a processed file, the sample table typically appears at the beginning of the file. It may also appear at the end of the file, in which case the header contains a pointer to the sample table at the end. When a new movie file is being recorded, it is not possible to write the sample table since the size of the file is not yet known. Instead, the table is must be written when recording is complete. If no other action is taken, this means that if the recording does not complete successfully (for example, in the event of a crash), the file data is unusable (because there is no sample table). By periodically inserting “movie fragments” into the movie file, the sample table can be built up incrementally. This means that if the file is not written completely, the movie file is still usable (up to the point where the last fragment was written).

## See Also

- [var metadata: [AVMetadataItem]?](avcapturemoviefileoutput/metadata.md)
  The metadata for the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/moviefragmentinterval)*