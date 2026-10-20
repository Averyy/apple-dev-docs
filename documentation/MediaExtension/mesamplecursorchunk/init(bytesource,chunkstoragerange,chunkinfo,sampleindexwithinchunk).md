# init(byteSource:chunkStorageRange:chunkInfo:sampleIndexWithinChunk:)

**Framework**: MediaExtension  
**Kind**: init  
**Role**: Initializer

Creates a new sample cursor chunk with byte source and chunk data that you provide.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(byteSource: MEByteSource, chunkStorageRange: AVSampleCursorStorageRange, chunkInfo: AVSampleCursorChunkInfo, sampleIndexWithinChunk: CFIndex)
```

```objc
- (instancetype) initWithByteSource:(MEByteSource *) byteSource chunkStorageRange:(AVSampleCursorStorageRange) chunkStorageRange chunkInfo:(AVSampleCursorChunkInfo) chunkInfo sampleIndexWithinChunk:(CFIndex) sampleIndexWithinChunk;
```

## Parameters

- `byteSource`: The byte source to use to read the data for the sample.
- `chunkStorageRange`: The offset location and length of the sample’s chunk within the byte source.
- `chunkInfo`: An object that provides details about the chunk in the media.
- `sampleIndexWithinChunk`: The offset index of the sample within the chunk, in samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursorchunk/init(bytesource:chunkstoragerange:chunkinfo:sampleindexwithinchunk:))*