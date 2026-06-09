# DiffuseProbeResource

**Framework**: RealityKit  
**Kind**: class

A resource containing baked diffuse lighting data organized as a tetrahedral probe mesh.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class DiffuseProbeResource
```

#### Overview

Diffuse probe resources store spherical harmonic coefficients at discrete 3D positions, connected via a tetrahedral mesh for efficient runtime interpolation. This compact representation enables high probe density throughout a scene, allowing dynamic objects to receive accurate diffuse lighting as they move through different lighting conditions.

#### Probe Data Format

Each probe stores first-order (L0 + L1) spherical harmonics: 4 coefficients per RGB channel, for a total of 12 floats (48 bytes) per probe. The tetrahedral mesh adds minimal per-tetrahedron overhead. This compact representation enables high probe density within typical memory budgets.

## Topics

### Initializers
- [convenience init(positions: [SIMD3<Float>], coefficients: [InlineArray<3, SIMD4<Float>>], tetrahedronIndices: [SIMD4<UInt16>]) throws](diffuseproberesource/init(positions:coefficients:tetrahedronindices:).md)
  Creates a diffuse probe resource from arrays of probe data.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DiffuseLightProbeGroupComponent](diffuselightprobegroupcomponent.md)
  A component that stores diffuse probe data for a spatial region.
- [struct DiffuseLightProbeReceiverComponent](diffuselightprobereceivercomponent.md)
  A component that receives diffuse lighting from a referenced probe group.
- [class LightmapResource](lightmapresource.md)
  A resource containing references to lightmap texture atlases and descriptions of how parts of the atlases map to meshes in the scene. At a high level, this resource comprises two parts:
- [struct LightmapComponent](lightmapcomponent.md)
- [struct DiffuseLightProbeGroupComponent](diffuselightprobegroupcomponent.md)
  A component that stores diffuse probe data for a spatial region.
- [struct DiffuseLightProbeReceiverComponent](diffuselightprobereceivercomponent.md)
  A component that receives diffuse lighting from a referenced probe group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/diffuseproberesource)*