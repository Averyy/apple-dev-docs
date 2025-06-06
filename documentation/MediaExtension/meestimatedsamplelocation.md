# MEEstimatedSampleLocation

**Framework**: MediaExtension  
**Kind**: class

An object that provides information about the estimated sample location with the media.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MEEstimatedSampleLocation
```

## Topics

### Creating an estimated sample location
- [init(byteSource: MEByteSource, estimatedSampleLocation: AVSampleCursorStorageRange, refinementDataLocation: AVSampleCursorStorageRange)](meestimatedsamplelocation/init(bytesource:estimatedsamplelocation:refinementdatalocation:).md)
  Creates an estimated sample location object with the byte source, sample location, and data location that you specify.
### Inspecting an estimated sample location
- [var byteSource: MEByteSource](meestimatedsamplelocation/bytesource.md)
  The byte source to use to read the data for the sample.
- [var estimatedSampleLocation: AVSampleCursorStorageRange](meestimatedsamplelocation/estimatedsamplelocation.md)
  The estimated starting file offset and size in bytes of the sample.
- [var refinementDataLocation: AVSampleCursorStorageRange](meestimatedsamplelocation/refinementdatalocation.md)
  The starting file offset and size in bytes of the data necessary to provide an accurate sample location.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MESampleCursor](mesamplecursor.md)
  A protocol that defines the information to provide about samples within a track of a media asset, and enables stepping through samples in the track in decode or presentation order.
- [class MESampleLocation](mesamplelocation.md)
  An object that provides information about the sample location with the media.
- [class MESampleCursorChunk](mesamplecursorchunk.md)
  An object that provides information about the chunk of media at the location of a sample.
- [class MEHEVCDependencyInfo](mehevcdependencyinfo.md)
  An object that provides information about the HEVC dependency attributes of a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meestimatedsamplelocation)*