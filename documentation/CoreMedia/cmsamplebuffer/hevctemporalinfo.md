# CMSampleBuffer.HEVCTemporalInfo

**Framework**: Core Media  
**Kind**: struct

The temporal layer information for all samples in a temporal layer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
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
- [init(temporalLayerID: Int, profileSpace: Int, tierFlag: Int, profileIndex: Int, profileCompatibilityFlags: Data?, constraintIndicatorFlags: Data?, levelIndex: Int)](cmsamplebuffer/hevctemporalinfo/init(temporallayerid:profilespace:tierflag:profileindex:profilecompatibilityflags:constraintindicatorflags:levelindex:).md)
### Instance Properties
- [var constraintIndicatorFlags: Data?](cmsamplebuffer/hevctemporalinfo/constraintindicatorflags.md)
- [var levelIndex: Int](cmsamplebuffer/hevctemporalinfo/levelindex.md)
- [var profileCompatibilityFlags: Data?](cmsamplebuffer/hevctemporalinfo/profilecompatibilityflags.md)
- [var profileIndex: Int](cmsamplebuffer/hevctemporalinfo/profileindex.md)
- [var profileSpace: Int](cmsamplebuffer/hevctemporalinfo/profilespace.md)
- [var temporalLayerID: Int](cmsamplebuffer/hevctemporalinfo/temporallayerid.md)
- [var tierFlag: Int](cmsamplebuffer/hevctemporalinfo/tierflag.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/hevctemporalinfo)*