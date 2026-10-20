# MESampleCursorChunk

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that provides information about the chunk of media at the location of a sample.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MESampleCursorChunk
```

```objc
@interface MESampleCursorChunk : NSObject
```

#### Overview

The [`chunkDetails()`](./mesamplecursor/chunkdetails%28%29.md) method returns an instance of this class.

## Topics

### Creating a sample cursor chunk
- [init(byteSource: MEByteSource, chunkStorageRange: AVSampleCursorStorageRange, chunkInfo: AVSampleCursorChunkInfo, sampleIndexWithinChunk: CFIndex)](./mesamplecursorchunk/init%28bytesource,chunkstoragerange,chunkinfo,sampleindexwithinchunk%29.md)
  Creates a new sample cursor chunk with byte source and chunk data that you provide.
### Inspecting a chunk
- [var byteSource: MEByteSource](./mesamplecursorchunk/bytesource.md)
  The byte source to use to read the data for the sample.
- [var chunkStorageRange: AVSampleCursorStorageRange](./mesamplecursorchunk/chunkstoragerange.md)
  The offset location and length of the sample’s chunk within the byte source.
- [var chunkInfo: AVSampleCursorChunkInfo](./mesamplecursorchunk/chunkinfo.md)
  An object that provides details about the chunk in the media.
- [var sampleIndexWithinChunk: CFIndex](./mesamplecursorchunk/sampleindexwithinchunk.md)
  The offset index of the sample within the chunk, in samples.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sample cursors
- [protocol MESampleCursor](./mesamplecursor.md)
  A protocol that defines the information to provide about samples within a track of a media asset, and enables stepping through samples in the track in decode or presentation order.
- [class MESampleLocation](./mesamplelocation.md)
  An object that provides information about the sample location with the media.
- [class MEEstimatedSampleLocation](./meestimatedsamplelocation.md)
  An object that provides information about the estimated sample location with the media.
- [class MEHEVCDependencyInfo](./mehevcdependencyinfo.md)
  An object that provides information about the HEVC dependency attributes of a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursorchunk)*