# chunkStorageRange

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The offset location and length of the sample’s chunk within the byte source.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var chunkStorageRange: AVSampleCursorStorageRange { get }
```

```objc
@property (nonatomic, readonly) AVSampleCursorStorageRange chunkStorageRange;
```

## See Also

### Inspecting a chunk
- [var byteSource: MEByteSource](./bytesource.md)
  The byte source to use to read the data for the sample.
- [var chunkInfo: AVSampleCursorChunkInfo](./chunkinfo.md)
  An object that provides details about the chunk in the media.
- [var sampleIndexWithinChunk: CFIndex](./sampleindexwithinchunk.md)
  The offset index of the sample within the chunk, in samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursorchunk/chunkstoragerange)*