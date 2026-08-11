# geometry

**Framework**: RealityKit  
**Kind**: property

The compiled vertex-stage geometry modifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var geometry: LowLevelMaterialResource.GeometryModifier { get }
```

## See Also

- [var surface: LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surface.md)
  The compiled fragment-stage surface shader.
- [LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surfaceshader.md)
  A compiled Metal function that implements the surface shader function.
- [LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometrymodifier.md)
  A compiled Metal function that implements the geometry modifier function.
- [LowLevelMaterialResource.LightingFunction](lowlevelmaterialresource/lightingfunction.md)
  A compiled Metal function that evaluates lighting.
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
  A compiled shader function that can receive per-draw parameters via an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/geometry)*