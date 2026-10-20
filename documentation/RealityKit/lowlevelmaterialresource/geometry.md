# geometry

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The compiled vertex-stage geometry modifier.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var geometry: LowLevelMaterialResource.GeometryModifier { get }
```

## See Also

### Configuring the shaders
- [var surface: LowLevelMaterialResource.SurfaceShader](./surface.md)
  The compiled fragment-stage surface shader.
- [LowLevelMaterialResource.SurfaceShader](./surfaceshader.md)
  A compiled Metal function that implements the surface shader function.
- [LowLevelMaterialResource.GeometryModifier](./geometrymodifier.md)
  A compiled Metal function that implements the geometry modifier function.
- [LowLevelMaterialResource.LightingFunction](./lightingfunction.md)
  A compiled Metal function that evaluates lighting.
- [LowLevelMaterialResource.Function](./function.md)
  A compiled shader function that can receive per-draw parameters via an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/geometry)*