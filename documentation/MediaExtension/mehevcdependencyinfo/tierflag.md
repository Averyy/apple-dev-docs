# tierFlag

**Framework**: MediaExtension  
**Kind**: property

The HEVC tier level flag, if available.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var tierFlag: Int16 { get set }
```

#### Discussion

This value maps to the [`kCMHEVCTemporalLevelInfoKey_TierFlag`](https://developer.apple.com/documentation/CoreMedia/kCMHEVCTemporalLevelInfoKey_TierFlag) sample buffer attachment, and is `-1` if this information isn’t available.

## See Also

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
- [var profileIndex: Int16](mehevcdependencyinfo/profileindex.md)
  The HEVC profile index, if available.
- [var profileCompatibilityFlags: Data?](mehevcdependencyinfo/profilecompatibilityflags.md)
  The HEVC profile compatibility flags (4 bytes), if available.
- [var constraintIndicatorFlags: Data?](mehevcdependencyinfo/constraintindicatorflags.md)
  The HEVC constraint indicator flags (6 bytes), if available.
- [var levelIndex: Int16](mehevcdependencyinfo/levelindex.md)
  The HEVC level index, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mehevcdependencyinfo/tierflag)*