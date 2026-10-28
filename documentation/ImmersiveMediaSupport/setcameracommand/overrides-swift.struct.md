# SetCameraCommand.Overrides

**Framework**: Immersive Media Support  
**Kind**: struct  
**Role**: Structure

Override camera/venue params

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Overrides
```

## Overview

> **Note**: The renderer only honors these overrides on visionOS 27, macOS 27, or later. Earlier runtimes ignore them during playback.

## Topics

### Initializers
- [init(rotation: Rotation3DFloat?, lensDefinitionData: ImmersiveCameraLensDefinition?, maskData: ImmersiveDynamicMask?)](./overrides-swift.struct/init%28rotation,lensdefinitiondata,maskdata%29.md)
### Instance Properties
- [var lensDefinitionData: ImmersiveCameraLensDefinition?](./overrides-swift.struct/lensdefinitiondata.md)
  Inline lens definition (ILPD) data to override lens calibration
- [var maskData: ImmersiveDynamicMask?](./overrides-swift.struct/maskdata.md)
  Dynamic mask data to override camera mask
- [var rotation: Rotation3DFloat?](./overrides-swift.struct/rotation.md)
  Camera rotation to override the rotation in [`pose`](../immersivecamera/pose.md).

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand/overrides-swift.struct)*