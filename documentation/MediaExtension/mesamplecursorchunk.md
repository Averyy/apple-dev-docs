# MESampleCursorChunk

**Framework**: MediaExtension  
**Kind**: class

An object that provides information about the chunk of media at the location of a sample.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MESampleCursorChunk
```

#### Overview

The [`chunkDetails()`](mesamplecursor/chunkdetails().md) method returns an instance of this class.

## Topics

### Creating a sample cursor chunk
- [init(byteSource: MEByteSource, chunkStorageRange: AVSampleCursorStorageRange, chunkInfo: AVSampleCursorChunkInfo, sampleIndexWithinChunk: CFIndex)](mesamplecursorchunk/init(bytesource:chunkstoragerange:chunkinfo:sampleindexwithinchunk:).md)
  Creates a new sample cursor chunk with byte source and chunk data that you provide.
### Inspecting a chunk
- [var byteSource: MEByteSource](mesamplecursorchunk/bytesource.md)
  The byte source to use to read the data for the sample.
- [var chunkStorageRange: AVSampleCursorStorageRange](mesamplecursorchunk/chunkstoragerange.md)
  The offset location and length of the sample’s chunk within the byte source.
- [var chunkInfo: AVSampleCursorChunkInfo](mesamplecursorchunk/chunkinfo.md)
  An object that provides details about the chunk in the media.
- [var sampleIndexWithinChunk: CFIndex](mesamplecursorchunk/sampleindexwithinchunk.md)
  The offset index of the sample within the chunk, in samples.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol MESampleCursor](mesamplecursor.md)
  A protocol that defines the information to provide about samples within a track of a media asset, and enables stepping through samples in the track in decode or presentation order.
- [class MESampleLocation](mesamplelocation.md)
  An object that provides information about the sample location with the media.
- [class MEEstimatedSampleLocation](meestimatedsamplelocation.md)
  An object that provides information about the estimated sample location with the media.
- [class MEHEVCDependencyInfo](mehevcdependencyinfo.md)
  An object that provides information about the HEVC dependency attributes of a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursorchunk)*