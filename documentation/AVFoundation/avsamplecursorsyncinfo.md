# AVSampleCursorSyncInfo

**Framework**: AVFoundation  
**Kind**: struct

A structure that describes the attributes of media samples to consider when resynchronizing a decoder.

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
struct AVSampleCursorSyncInfo
```

## Topics

### Sync Information
- [var sampleIsFullSync: ObjCBool](avsamplecursorsyncinfo/sampleisfullsync.md)
  A Boolean value that indicates whether a sample is a full sync sample.
- [var sampleIsPartialSync: ObjCBool](avsamplecursorsyncinfo/sampleispartialsync.md)
  A Boolean value that indicates whether a sample is a partial sync sample.
- [var sampleIsDroppable: ObjCBool](avsamplecursorsyncinfo/sampleisdroppable.md)
  A Boolean value that indicates whether a sample is droppable.
### Initializers
- [init()](avsamplecursorsyncinfo/init.md)
  Creates a sample cursor sync information structure.
- [init(sampleIsFullSync: ObjCBool, sampleIsPartialSync: ObjCBool, sampleIsDroppable: ObjCBool)](avsamplecursorsyncinfo/init(sampleisfullsync:sampleispartialsync:sampleisdroppable:).md)
  Creates a sample cursor sync information structure with media sample information.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVSampleCursor](avsamplecursor.md)
  An object that provides information about the media sample at the cursor’s current position.
- [struct AVSampleCursorDependencyInfo](avsamplecursordependencyinfo.md)
  A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [struct AVSampleCursorAudioDependencyInfo](avsamplecursoraudiodependencyinfo.md)
  A structure that describes the independent decodability of audio samples.
- [struct AVSampleCursorStorageRange](avsamplecursorstoragerange.md)
  A structure that indicates the offset and length of storage for a media sample or its chunk.
- [struct AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md)
  A value that provides information about a chunk of media samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursorsyncinfo)*