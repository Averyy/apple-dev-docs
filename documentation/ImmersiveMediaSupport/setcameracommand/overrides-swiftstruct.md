# SetCameraCommand.Overrides

**Framework**: Immersive Media Support  
**Kind**: struct

Override camera/venue params

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Overrides
```

#### Overview

> **Note**: The renderer only honors these overrides on visionOS 27, macOS 27, or later. Earlier runtimes ignore them during playback.

## Topics

### Initializers
- [init(rotation: Rotation3DFloat?, lensDefinitionData: ImmersiveCameraLensDefinition?, maskData: ImmersiveDynamicMask?)](setcameracommand/overrides-swift.struct/init(rotation:lensdefinitiondata:maskdata:).md)
### Instance Properties
- [var lensDefinitionData: ImmersiveCameraLensDefinition?](setcameracommand/overrides-swift.struct/lensdefinitiondata.md)
  Inline lens definition (ILPD) data to override lens calibration
- [var maskData: ImmersiveDynamicMask?](setcameracommand/overrides-swift.struct/maskdata.md)
  Dynamic mask data to override camera mask
- [var rotation: Rotation3DFloat?](setcameracommand/overrides-swift.struct/rotation.md)
  Camera rotation to override the rotation in [`pose`](immersivecamera/pose.md).

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand/overrides-swift.struct)*