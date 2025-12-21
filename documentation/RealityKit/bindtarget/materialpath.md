# BindTarget.MaterialPath

**Framework**: RealityKit  
**Kind**: struct

Material parameters that an animation can target.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct MaterialPath
```

#### Overview

Each property is a `BindTarget` which defines a parameter an animation can target.

## Topics

### Instance Properties
- [var anisotropyAngleScale: BindTarget](bindtarget/materialpath/anisotropyanglescale.md)
  This BindTarget references a Float type
- [var anisotropyLevelScale: BindTarget](bindtarget/materialpath/anisotropylevelscale.md)
  This BindTarget references a Float type
- [var baseColorTint: BindTarget](bindtarget/materialpath/basecolortint.md)
  This BindTarget references a SIMD4 type
- [var clearcoatRoughnessScale: BindTarget](bindtarget/materialpath/clearcoatroughnessscale.md)
  This BindTarget references a Float type
- [var clearcoatScale: BindTarget](bindtarget/materialpath/clearcoatscale.md)
  This BindTarget references a Float type
- [var customValue: BindTarget](bindtarget/materialpath/customvalue.md)
- [var emissiveColor: BindTarget](bindtarget/materialpath/emissivecolor.md)
  This BindTarget references a SIMD4 type
- [var emissiveIntensity: BindTarget](bindtarget/materialpath/emissiveintensity.md)
  This BindTarget references a Float type
- [var metallicScale: BindTarget](bindtarget/materialpath/metallicscale.md)
  This BindTarget references a Float type
- [var opacityThreshold: BindTarget](bindtarget/materialpath/opacitythreshold.md)
  This BindTarget references a Float type
- [var roughnessScale: BindTarget](bindtarget/materialpath/roughnessscale.md)
  This BindTarget references a Float type
- [var secondaryTextureCoordinate: BindTarget.TextureCoordinateTransformPath](bindtarget/materialpath/secondarytexturecoordinate.md)
  This BindTarget references a SIMD2 type
- [var sheenTint: BindTarget](bindtarget/materialpath/sheentint.md)
  This BindTarget references a SIMD4 type
- [var specularScale: BindTarget](bindtarget/materialpath/specularscale.md)
  This BindTarget references a Float type
- [var textureCoordinate: BindTarget.TextureCoordinateTransformPath](bindtarget/materialpath/texturecoordinate.md)
  This BindTarget references a SIMD2 type

## See Also

- [BindTarget.opacity](bindtarget/opacity.md)
  An option that specifies that the entity’s opacity to animate. Requires that the entity has an OpacityComponent
- [BindTarget.billboardBlendFactor](bindtarget/billboardblendfactor.md)
- [BindTarget.blendShapeWeights](bindtarget/blendshapeweights.md)
  An option the entity’s blend shape weights animate. Requires that the entity has a BlendShapeWeightsComponent.
- [BindTarget.blendShapeWeightsAtIndex(_:)](bindtarget/blendshapeweightsatindex(_:).md)
- [case blendShapeWeightsWithID(BlendShapeWeightsData.ID)](bindtarget/blendshapeweightswithid(_:).md)
- [static func material(Int) -> BindTarget.MaterialPath](bindtarget/material(_:).md)
  Generates a complex bind path from one of an entity’s materials.
- [BindTarget.TextureCoordinateTransformPath](bindtarget/texturecoordinatetransformpath.md)
  The texture coordinate parameters for a given texture layer that an animation can target.
- [BindTarget.IkSolverPath](bindtarget/iksolverpath.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/materialpath)*