# sampleIndexWithinChunk

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The offset index of the sample within the chunk, in samples.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var sampleIndexWithinChunk: CFIndex { get }
```

```objc
@property (nonatomic, readonly) CFIndex sampleIndexWithinChunk;
```

## See Also

### Inspecting a chunk
- [var byteSource: MEByteSource](./bytesource.md)
  The byte source to use to read the data for the sample.
- [var chunkStorageRange: AVSampleCursorStorageRange](./chunkstoragerange.md)
  The offset location and length of the sample’s chunk within the byte source.
- [var chunkInfo: AVSampleCursorChunkInfo](./chunkinfo.md)
  An object that provides details about the chunk in the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursorchunk/sampleindexwithinchunk)*