# MESampleLocation

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that provides information about the sample location with the media.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MESampleLocation
```

```objc
@interface MESampleLocation : NSObject
```

## Topics

### Creating a sample location
- [init(byteSource: MEByteSource, sampleLocation: AVSampleCursorStorageRange)](./mesamplelocation/init%28bytesource,samplelocation%29.md)
  Creates a sample location object with the byte source and sample location that you specify.
### Inspecting a sample location
- [var byteSource: MEByteSource](./mesamplelocation/bytesource.md)
  The byte source to use to read the data for the sample.
- [var sampleLocation: AVSampleCursorStorageRange](./mesamplelocation/samplelocation.md)
  The starting file offset and size in bytes of the sample.

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
- [class MESampleCursorChunk](./mesamplecursorchunk.md)
  An object that provides information about the chunk of media at the location of a sample.
- [class MEEstimatedSampleLocation](./meestimatedsamplelocation.md)
  An object that provides information about the estimated sample location with the media.
- [class MEHEVCDependencyInfo](./mehevcdependencyinfo.md)
  An object that provides information about the HEVC dependency attributes of a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplelocation)*