# MEEstimatedSampleLocation

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that provides information about the estimated sample location with the media.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MEEstimatedSampleLocation
```

```objc
@interface MEEstimatedSampleLocation : NSObject
```

## Topics

### Creating an estimated sample location
- [init(byteSource: MEByteSource, estimatedSampleLocation: AVSampleCursorStorageRange, refinementDataLocation: AVSampleCursorStorageRange)](./meestimatedsamplelocation/init%28bytesource,estimatedsamplelocation,refinementdatalocation%29.md)
  Creates an estimated sample location object with the byte source, sample location, and data location that you specify.
### Inspecting an estimated sample location
- [var byteSource: MEByteSource](./meestimatedsamplelocation/bytesource.md)
  The byte source to use to read the data for the sample.
- [var estimatedSampleLocation: AVSampleCursorStorageRange](./meestimatedsamplelocation/estimatedsamplelocation.md)
  The estimated starting file offset and size in bytes of the sample.
- [var refinementDataLocation: AVSampleCursorStorageRange](./meestimatedsamplelocation/refinementdatalocation.md)
  The starting file offset and size in bytes of the data necessary to provide an accurate sample location.

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
- [class MESampleCursorChunk](./mesamplecursorchunk.md)
  An object that provides information about the chunk of media at the location of a sample.
- [class MEHEVCDependencyInfo](./mehevcdependencyinfo.md)
  An object that provides information about the HEVC dependency attributes of a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meestimatedsamplelocation)*