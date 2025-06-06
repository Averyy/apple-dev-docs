# chunkInfo

**Framework**: MediaExtension  
**Kind**: property

An object that provides details about the chunk in the media.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var chunkInfo: AVSampleCursorChunkInfo { get }
```

## See Also

- [var byteSource: MEByteSource](mesamplecursorchunk/bytesource.md)
  The byte source to use to read the data for the sample.
- [var chunkStorageRange: AVSampleCursorStorageRange](mesamplecursorchunk/chunkstoragerange.md)
  The offset location and length of the sample’s chunk within the byte source.
- [var sampleIndexWithinChunk: CFIndex](mesamplecursorchunk/sampleindexwithinchunk.md)
  The offset index of the sample within the chunk, in samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursorchunk/chunkinfo)*