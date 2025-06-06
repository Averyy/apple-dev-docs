# AVSampleCursorChunkInfo

**Framework**: AVFoundation  
**Kind**: struct

A value that provides information about a chunk of media samples.

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
struct AVSampleCursorChunkInfo
```

## Topics

### Chunk Information
- [var chunkSampleCount: Int64](avsamplecursorchunkinfo/chunksamplecount.md)
  The count of media samples in the chunk.
- [var chunkHasUniformSampleSizes: ObjCBool](avsamplecursorchunkinfo/chunkhasuniformsamplesizes.md)
  The samples in the chunk occupy the same number of bytes in storage.
- [var chunkHasUniformSampleDurations: ObjCBool](avsamplecursorchunkinfo/chunkhasuniformsampledurations.md)
  The samples in the chunk have the same duration.
- [var chunkHasUniformFormatDescriptions: ObjCBool](avsamplecursorchunkinfo/chunkhasuniformformatdescriptions.md)
  The samples in the chunk have the same format description.
### Initializers
- [init()](avsamplecursorchunkinfo/init.md)
  Creates a chunk information structure.
- [init(chunkSampleCount: Int64, chunkHasUniformSampleSizes: ObjCBool, chunkHasUniformSampleDurations: ObjCBool, chunkHasUniformFormatDescriptions: ObjCBool)](avsamplecursorchunkinfo/init(chunksamplecount:chunkhasuniformsamplesizes:chunkhasuniformsampledurations:chunkhasuniformformatdescriptions:).md)
  Creates a chunk information structure with the specified values.

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
- [struct AVSampleCursorAudioDependencyInfo](avsamplecursoraudiodependencyinfo.md)
  A structure that describes the independent decodability of audio samples.
- [struct AVSampleCursorStorageRange](avsamplecursorstoragerange.md)
  A structure that indicates the offset and length of storage for a media sample or its chunk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursorchunkinfo)*