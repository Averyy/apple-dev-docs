# EnvironmentProbeAnchor

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

An environment probe in the world.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct EnvironmentProbeAnchor
```

## Overview

Use environment probes to light virtual geometry by producing environment textures from the probe’s location in the world.

> **Note**:  The framework always positions the anchor at the location of the Vision Pro device.

## Topics

### Getting anchor information
- [var environmentTexture: (any MTLTexture)?](./environmentprobeanchor/environmenttexture.md)
  The environment texture of an anchor.
- [var cameraScaleReference: Float](./environmentprobeanchor/camerascalereference.md)
  The camera scale reference of this anchor.
- [var originFromAnchorTransform: simd_float4x4](./environmentprobeanchor/originfromanchortransform.md)
  The transform from the environment probe anchor to the origin coordinate system.
### Comparing environment probe anchors
- [var id: UUID](./environmentprobeanchor/id.md)
  The unique identifier of this anchor.
- [var description: String](./environmentprobeanchor/description.md)
  A textual representation of this anchor.
### Operators
- [static func == (EnvironmentProbeAnchor, EnvironmentProbeAnchor) -> Bool](./environmentprobeanchor/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two environment probe anchors are equal.
### Default Implementations
- [ARKitCoordinateSpaceProviding Implementations](./environmentprobeanchor/arkitcoordinatespaceproviding-implementations.md)

## Relationships

### Conforms To
- [ARKitCoordinateSpaceProviding](./arkitcoordinatespaceproviding.md)
- [Anchor](./anchor.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Lighting estimation
- [class EnvironmentLightEstimationProvider](./environmentlightestimationprovider.md)
  A source of live data about lighting information in the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/environmentprobeanchor)*