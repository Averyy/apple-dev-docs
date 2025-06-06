# AVSampleCursorAudioDependencyInfo

**Framework**: AVFoundation  
**Kind**: struct

A structure that describes the independent decodability of audio samples.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVSampleCursorAudioDependencyInfo
```

## Topics

### Querying Independent Decodability
- [var audioSampleIsIndependentlyDecodable: ObjCBool](avsamplecursoraudiodependencyinfo/audiosampleisindependentlydecodable.md)
  A Boolean value indicating whether the sample is independently decodable.
- [var audioSamplePacketRefreshCount: Int](avsamplecursoraudiodependencyinfo/audiosamplepacketrefreshcount.md)
  The number of samples, starting at the current sample, that must be fed to the decoder to achieve full decoder refresh.
### Initializers
- [init()](avsamplecursoraudiodependencyinfo/init.md)
  Creates an audio sample decodability information structure.
- [init(audioSampleIsIndependentlyDecodable: ObjCBool, audioSamplePacketRefreshCount: Int)](avsamplecursoraudiodependencyinfo/init(audiosampleisindependentlydecodable:audiosamplepacketrefreshcount:).md)
  Creates an audio sample decodability information structure with the specified values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVSampleCursor](avsamplecursor.md)
  An object that provides information about the media sample at the cursor’s current position.
- [struct AVSampleCursorSyncInfo](avsamplecursorsyncinfo.md)
  A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [struct AVSampleCursorDependencyInfo](avsamplecursordependencyinfo.md)
  A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [struct AVSampleCursorStorageRange](avsamplecursorstoragerange.md)
  A structure that indicates the offset and length of storage for a media sample or its chunk.
- [struct AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md)
  A value that provides information about a chunk of media samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursoraudiodependencyinfo)*