# constraintIndicatorFlags

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The HEVC constraint indicator flags (6 bytes), if available.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var constraintIndicatorFlags: Data? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSData * constraintIndicatorFlags;
```

#### Discussion

This value maps to the [`kCMHEVCTemporalLevelInfoKey_ConstraintIndicatorFlags`](../../CoreMedia/kcmhevctemporallevelinfokey_constraintindicatorflags.md) sample buffer attachment, and is `nil` if this information isn’t available.

## See Also

### Inspecting the HEVC dependency attributes of a sample
- [var hasTemporalSubLayerAccess: Bool](./hastemporalsublayeraccess.md)
  A Boolean value that indicates if the sample has an HEVC temporal sublayer access (TSA) picture.
- [var hasStepwiseTemporalSubLayerAccess: Bool](./hasstepwisetemporalsublayeraccess.md)
  A Boolean value that indicates if the sample has an HEVC stepwise temporal sublayer access (STSA) picture.
- [var syncSampleNALUnitType: Int16](./syncsamplenalunittype.md)
  The NAL unit type for HEVC sync sample groups.
- [var temporalLevel: Int16](./temporallevel.md)
  The HEVC temporal level, if available.
- [var profileSpace: Int16](./profilespace.md)
  The HEVC profile space, if available.
- [var tierFlag: Int16](./tierflag.md)
  The HEVC tier level flag, if available.
- [var profileIndex: Int16](./profileindex.md)
  The HEVC profile index, if available.
- [var profileCompatibilityFlags: Data?](./profilecompatibilityflags.md)
  The HEVC profile compatibility flags (4 bytes), if available.
- [var levelIndex: Int16](./levelindex.md)
  The HEVC level index, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mehevcdependencyinfo/constraintindicatorflags)*