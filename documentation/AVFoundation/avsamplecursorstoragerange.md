# AVSampleCursorStorageRange

**Framework**: AVFoundation  
**Kind**: struct

A structure that indicates the offset and length of storage for a media sample or its chunk.

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
struct AVSampleCursorStorageRange
```

## Topics

### Storage Range
- [var offset: Int64](avsamplecursorstoragerange/offset.md)
  The offset of the first byte of storage that a media sample or its chunk occupies.
- [var length: Int64](avsamplecursorstoragerange/length.md)
  The count of bytes of storage that a media sample or its chunk occupies.
### Initializers
- [init()](avsamplecursorstoragerange/init.md)
  Creates a storage range structure.
- [init(offset: Int64, length: Int64)](avsamplecursorstoragerange/init(offset:length:).md)
  Creates a storage range structure with offset and length values.

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
- [struct AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md)
  A value that provides information about a chunk of media samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursorstoragerange)*