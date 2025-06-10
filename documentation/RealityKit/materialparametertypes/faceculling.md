# MaterialParameterTypes.FaceCulling

**Framework**: RealityKit  
**Kind**: enum

An object that defines how the system removes polygons before rendering a scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum FaceCulling
```

#### Overview

To improve performance, RealityKit culls polygons, or faces, that it determines won’t be visible. Discarding faces that aren’t part of the final render eliminates the need to do any calculations for those faces. Use this object to specify what kind of polygons RealityKit culls.

## Topics

### Face culling
- [MaterialParameterTypes.FaceCulling.front](materialparametertypes/faceculling/front.md)
  The system culls front-facing polygons.
- [MaterialParameterTypes.FaceCulling.back](materialparametertypes/faceculling/back.md)
  The system culls back-facing polygons.
- [MaterialParameterTypes.FaceCulling.none](materialparametertypes/faceculling/none.md)
  The system doesn’t cull polygons.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialparametertypes/faceculling)*