# CMSampleBuffer.HEVCTemporalInfo

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

The temporal layer information for all samples in a temporal layer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct HEVCTemporalInfo
```

#### Overview

The members of this struct represents the `tscl` sample group as defined in ISO/IEC 14496‐15 section 8.4.5 Temporal scalability sample grouping..

## Topics

### Initializers
- [init(temporalLayerID: Int, profileSpace: Int, tierFlag: Int, profileIndex: Int, profileCompatibilityFlags: Data?, constraintIndicatorFlags: Data?, levelIndex: Int)](./hevctemporalinfo/init%28temporallayerid,profilespace,tierflag,profileindex,profilecompatibilityflags,constraintindicatorflags,levelindex%29.md)
### Instance Properties
- [var constraintIndicatorFlags: Data?](./hevctemporalinfo/constraintindicatorflags.md)
- [var levelIndex: Int](./hevctemporalinfo/levelindex.md)
- [var profileCompatibilityFlags: Data?](./hevctemporalinfo/profilecompatibilityflags.md)
- [var profileIndex: Int](./hevctemporalinfo/profileindex.md)
- [var profileSpace: Int](./hevctemporalinfo/profilespace.md)
- [var temporalLayerID: Int](./hevctemporalinfo/temporallayerid.md)
- [var tierFlag: Int](./hevctemporalinfo/tierflag.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/hevctemporalinfo)*