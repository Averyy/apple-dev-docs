# byteSource

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The byte source to use to read the data for the sample.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var byteSource: MEByteSource { get }
```

```objc
@property (nonatomic, retain, readonly) MEByteSource * byteSource;
```

## See Also

### Inspecting a chunk
- [var chunkStorageRange: AVSampleCursorStorageRange](./chunkstoragerange.md)
  The offset location and length of the sample’s chunk within the byte source.
- [var chunkInfo: AVSampleCursorChunkInfo](./chunkinfo.md)
  An object that provides details about the chunk in the media.
- [var sampleIndexWithinChunk: CFIndex](./sampleindexwithinchunk.md)
  The offset index of the sample within the chunk, in samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursorchunk/bytesource)*