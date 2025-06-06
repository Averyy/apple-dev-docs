# MEHEVCDependencyInfo

**Framework**: MediaExtension  
**Kind**: class

An object that provides information about the HEVC dependency attributes of a sample.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MEHEVCDependencyInfo
```

## Topics

### Inspecting the HEVC dependency attributes of a sample
- [var hasTemporalSubLayerAccess: Bool](mehevcdependencyinfo/hastemporalsublayeraccess.md)
  A Boolean value that indicates if the sample has an HEVC temporal sublayer access (TSA) picture.
- [var hasStepwiseTemporalSubLayerAccess: Bool](mehevcdependencyinfo/hasstepwisetemporalsublayeraccess.md)
  A Boolean value that indicates if the sample has an HEVC stepwise temporal sublayer access (STSA) picture.
- [var syncSampleNALUnitType: Int16](mehevcdependencyinfo/syncsamplenalunittype.md)
  The NAL unit type for HEVC sync sample groups.
- [var temporalLevel: Int16](mehevcdependencyinfo/temporallevel.md)
  The HEVC temporal level, if available.
- [var profileSpace: Int16](mehevcdependencyinfo/profilespace.md)
  The HEVC profile space, if available.
- [var tierFlag: Int16](mehevcdependencyinfo/tierflag.md)
  The HEVC tier level flag, if available.
- [var profileIndex: Int16](mehevcdependencyinfo/profileindex.md)
  The HEVC profile index, if available.
- [var profileCompatibilityFlags: Data?](mehevcdependencyinfo/profilecompatibilityflags.md)
  The HEVC profile compatibility flags (4 bytes), if available.
- [var constraintIndicatorFlags: Data?](mehevcdependencyinfo/constraintindicatorflags.md)
  The HEVC constraint indicator flags (6 bytes), if available.
- [var levelIndex: Int16](mehevcdependencyinfo/levelindex.md)
  The HEVC level index, if available.

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
- [class MEEstimatedSampleLocation](meestimatedsamplelocation.md)
  An object that provides information about the estimated sample location with the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mehevcdependencyinfo)*