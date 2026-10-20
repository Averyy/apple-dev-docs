# MEHEVCDependencyInfo

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that provides information about the HEVC dependency attributes of a sample.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MEHEVCDependencyInfo
```

```objc
@interface MEHEVCDependencyInfo : NSObject
```

## Topics

### Inspecting the HEVC dependency attributes of a sample
- [var hasTemporalSubLayerAccess: Bool](./mehevcdependencyinfo/hastemporalsublayeraccess.md)
  A Boolean value that indicates if the sample has an HEVC temporal sublayer access (TSA) picture.
- [var hasStepwiseTemporalSubLayerAccess: Bool](./mehevcdependencyinfo/hasstepwisetemporalsublayeraccess.md)
  A Boolean value that indicates if the sample has an HEVC stepwise temporal sublayer access (STSA) picture.
- [var syncSampleNALUnitType: Int16](./mehevcdependencyinfo/syncsamplenalunittype.md)
  The NAL unit type for HEVC sync sample groups.
- [var temporalLevel: Int16](./mehevcdependencyinfo/temporallevel.md)
  The HEVC temporal level, if available.
- [var profileSpace: Int16](./mehevcdependencyinfo/profilespace.md)
  The HEVC profile space, if available.
- [var tierFlag: Int16](./mehevcdependencyinfo/tierflag.md)
  The HEVC tier level flag, if available.
- [var profileIndex: Int16](./mehevcdependencyinfo/profileindex.md)
  The HEVC profile index, if available.
- [var profileCompatibilityFlags: Data?](./mehevcdependencyinfo/profilecompatibilityflags.md)
  The HEVC profile compatibility flags (4 bytes), if available.
- [var constraintIndicatorFlags: Data?](./mehevcdependencyinfo/constraintindicatorflags.md)
  The HEVC constraint indicator flags (6 bytes), if available.
- [var levelIndex: Int16](./mehevcdependencyinfo/levelindex.md)
  The HEVC level index, if available.

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
- [class MEEstimatedSampleLocation](./meestimatedsamplelocation.md)
  An object that provides information about the estimated sample location with the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mehevcdependencyinfo)*