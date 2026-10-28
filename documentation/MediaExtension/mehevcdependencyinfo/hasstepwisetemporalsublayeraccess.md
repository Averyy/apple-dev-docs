# hasStepwiseTemporalSubLayerAccess

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the sample has an HEVC stepwise temporal sublayer access (STSA) picture.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var hasStepwiseTemporalSubLayerAccess: Bool { get set }
```

```objc
@property (nonatomic, getter=hasStepwiseTemporalSubLayerAccess) BOOL stepwiseTemporalSubLayerAccess;
```

## Discussion

This value maps to the [`kCMSampleAttachmentKey_HEVCStepwiseTemporalSubLayerAccess`](../../CoreMedia/kcmsampleattachmentkey_hevcstepwisetemporalsublayeraccess.md) sample buffer attachment.

## See Also

### Inspecting the HEVC dependency attributes of a sample
- [var hasTemporalSubLayerAccess: Bool](./hastemporalsublayeraccess.md)
  A Boolean value that indicates if the sample has an HEVC temporal sublayer access (TSA) picture.
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
- [var constraintIndicatorFlags: Data?](./constraintindicatorflags.md)
  The HEVC constraint indicator flags (6 bytes), if available.
- [var levelIndex: Int16](./levelindex.md)
  The HEVC level index, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mehevcdependencyinfo/hasstepwisetemporalsublayeraccess)*