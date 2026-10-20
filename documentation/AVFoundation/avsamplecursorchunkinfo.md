# AVSampleCursorChunkInfo

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A value that provides information about a chunk of media samples.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct AVSampleCursorChunkInfo
```

```c
typedef struct { ... } AVSampleCursorChunkInfo;
```

## Topics

### Chunk information
- [var chunkSampleCount: Int64](./avsamplecursorchunkinfo/chunksamplecount.md)
  The count of media samples in the chunk.
- [var chunkHasUniformSampleSizes: ObjCBool](./avsamplecursorchunkinfo/chunkhasuniformsamplesizes.md)
  The samples in the chunk occupy the same number of bytes in storage.
- [var chunkHasUniformSampleDurations: ObjCBool](./avsamplecursorchunkinfo/chunkhasuniformsampledurations.md)
  The samples in the chunk have the same duration.
- [var chunkHasUniformFormatDescriptions: ObjCBool](./avsamplecursorchunkinfo/chunkhasuniformformatdescriptions.md)
  The samples in the chunk have the same format description.
### Initializers
- [init()](./avsamplecursorchunkinfo/init%28%29.md)
  Creates a chunk information structure.
- [init(chunkSampleCount: Int64, chunkHasUniformSampleSizes: ObjCBool, chunkHasUniformSampleDurations: ObjCBool, chunkHasUniformFormatDescriptions: ObjCBool)](./avsamplecursorchunkinfo/init%28chunksamplecount,chunkhasuniformsamplesizes,chunkhasuniformsampledurations,chunkhasuniformformatdescriptions%29.md)
  Creates a chunk information structure with the specified values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Sample cursors
- [class AVSampleCursor](./avsamplecursor.md)
  An object that provides information about the media sample at the cursor’s current position.
- [struct AVSampleCursorSyncInfo](./avsamplecursorsyncinfo.md)
  A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [struct AVSampleCursorDependencyInfo](./avsamplecursordependencyinfo.md)
  A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [struct AVSampleCursorAudioDependencyInfo](./avsamplecursoraudiodependencyinfo.md)
  A structure that describes the independent decodability of audio samples.
- [struct AVSampleCursorStorageRange](./avsamplecursorstoragerange.md)
  A structure that indicates the offset and length of storage for a media sample or its chunk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursorchunkinfo)*