# copyCurrentSampleFormatDescription()

**Framework**: AVFoundation  
**Kind**: method

Returns the format description of the sample at the cursor’s current position.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.10+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func copyCurrentSampleFormatDescription() -> CMFormatDescription
```

#### Return Value

The current sample’s format description.

## See Also

- [var currentChunkInfo: AVSampleCursorChunkInfo](avsamplecursor/currentchunkinfo.md)
  A value that provides information about the chunk of samples to which the current sample belongs.
- [struct AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md)
  A value that provides information about a chunk of media samples.
- [var currentChunkStorageRange: AVSampleCursorStorageRange](avsamplecursor/currentchunkstoragerange.md)
  The sample range in the storage container to load together with the current sample as a chunk.
- [struct AVSampleCursorStorageRange](avsamplecursorstoragerange.md)
  A structure that indicates the offset and length of storage for a media sample or its chunk.
- [var currentChunkStorageURL: URL?](avsamplecursor/currentchunkstorageurl.md)
  The URL of the storage container of the current sample and other samples to load in the same operation as a chunk.
- [var currentSampleDependencyInfo: AVSampleCursorDependencyInfo](avsamplecursor/currentsampledependencyinfo.md)
  The dependency information that describes relationships between a media sample and other media samples in the same sample sequence.
- [struct AVSampleCursorDependencyInfo](avsamplecursordependencyinfo.md)
  A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [var currentSampleDuration: CMTime](avsamplecursor/currentsampleduration.md)
  The decode duration of the sample at the cursor’s current position.
- [var currentSampleIndexInChunk: Int64](avsamplecursor/currentsampleindexinchunk.md)
  The index of the current sample within the chunk to which it belongs.
- [var currentSampleStorageRange: AVSampleCursorStorageRange](avsamplecursor/currentsamplestoragerange.md)
  The offset and length of the current sample in the current chunk storage URL.
- [var currentSampleSyncInfo: AVSampleCursorSyncInfo](avsamplecursor/currentsamplesyncinfo.md)
  The synchronization information for the current sample for consideration when resynchronizing a decoder.
- [struct AVSampleCursorSyncInfo](avsamplecursorsyncinfo.md)
  A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [var currentSampleAudioDependencyInfo: AVSampleCursorAudioDependencyInfo](avsamplecursor/currentsampleaudiodependencyinfo.md)
  The independent decodability information for the audio sample.
- [var currentSampleDependencyAttachments: [AnyHashable : Any]?](avsamplecursor/currentsampledependencyattachments.md)
  A dictionary of dependency-related sample buffer attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursor/copycurrentsampleformatdescription())*