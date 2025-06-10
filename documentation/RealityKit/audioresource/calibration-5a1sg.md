# AudioResource.Calibration

**Framework**: RealityKit  
**Kind**: struct

A container for different calibration modes that can be applied for playback.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct Calibration
```

## Topics

### Type Methods
- [static absolute(dBSPL:)](audioresource/calibration-5a1sg/absolute(dbspl:).md)
  The reference level (-12dBLUFS) of the audio source material will be reproduced at the given `dBSPL` level on known audio output hardware.
- [static relative(dBSPL:)](audioresource/calibration-5a1sg/relative(dbspl:).md)
  Relative adjustment of the resource from the default level of the audio output hardware.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioresource/calibration-5a1sg)*