# absolute(dBSPL:)

**Framework**: RealityKit  
**Kind**: method

The reference level (-12dBLUFS) of the audio source material will be reproduced at the given `dBSPL` level on known audio output hardware.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
static func absolute(dBSPL: Audio.Decibel) -> AudioResource.Calibration
```

#### Discussion

> **Note**: The -12dBLUFS reference level is achieved automatically by using `Normalization.dynamic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioresource/calibration-89r8s/absolute(dbspl:))*