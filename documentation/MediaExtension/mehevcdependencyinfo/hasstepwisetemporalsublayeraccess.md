# hasStepwiseTemporalSubLayerAccess

**Framework**: MediaExtension  
**Kind**: property

A Boolean value that indicates if the sample has an HEVC stepwise temporal sublayer access (STSA) picture.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var hasStepwiseTemporalSubLayerAccess: Bool { get set }
```

#### Discussion

This value maps to the [`kCMSampleAttachmentKey_HEVCStepwiseTemporalSubLayerAccess`](https://developer.apple.com/documentation/CoreMedia/kCMSampleAttachmentKey_HEVCStepwiseTemporalSubLayerAccess) sample buffer attachment.

## See Also

- [var hasTemporalSubLayerAccess: Bool](mehevcdependencyinfo/hastemporalsublayeraccess.md)
  A Boolean value that indicates if the sample has an HEVC temporal sublayer access (TSA) picture.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mehevcdependencyinfo/hasstepwisetemporalsublayeraccess)*