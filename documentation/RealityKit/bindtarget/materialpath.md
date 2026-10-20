# BindTarget.MaterialPath

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

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
- [var anisotropyAngleScale: BindTarget](./materialpath/anisotropyanglescale.md)
  This BindTarget references a Float type
- [var anisotropyLevelScale: BindTarget](./materialpath/anisotropylevelscale.md)
  This BindTarget references a Float type
- [var baseColorTint: BindTarget](./materialpath/basecolortint.md)
  This BindTarget references a SIMD4 type
- [var clearcoatRoughnessScale: BindTarget](./materialpath/clearcoatroughnessscale.md)
  This BindTarget references a Float type
- [var clearcoatScale: BindTarget](./materialpath/clearcoatscale.md)
  This BindTarget references a Float type
- [var customValue: BindTarget](./materialpath/customvalue.md)
- [var emissiveColor: BindTarget](./materialpath/emissivecolor.md)
  This BindTarget references a SIMD4 type
- [var emissiveIntensity: BindTarget](./materialpath/emissiveintensity.md)
  This BindTarget references a Float type
- [var metallicScale: BindTarget](./materialpath/metallicscale.md)
  This BindTarget references a Float type
- [var opacityThreshold: BindTarget](./materialpath/opacitythreshold.md)
  This BindTarget references a Float type
- [var roughnessScale: BindTarget](./materialpath/roughnessscale.md)
  This BindTarget references a Float type
- [var secondaryTextureCoordinate: BindTarget.TextureCoordinateTransformPath](./materialpath/secondarytexturecoordinate.md)
  This BindTarget references a SIMD2 type
- [var sheenTint: BindTarget](./materialpath/sheentint.md)
  This BindTarget references a SIMD4 type
- [var specularScale: BindTarget](./materialpath/specularscale.md)
  This BindTarget references a Float type
- [var textureCoordinate: BindTarget.TextureCoordinateTransformPath](./materialpath/texturecoordinate.md)
  This BindTarget references a SIMD2 type

## See Also

### Animatable properties
- [BindTarget.opacity](./opacity.md)
  An option that specifies that the entity’s opacity to animate. Requires that the entity has an OpacityComponent
- [BindTarget.billboardBlendFactor](./billboardblendfactor.md)
- [BindTarget.blendShapeWeights](./blendshapeweights.md)
  An option the entity’s blend shape weights animate. Requires that the entity has a BlendShapeWeightsComponent.
- [BindTarget.skeletalPose(_:)](./skeletalpose%28_%29.md)
  An option that specifies one of the entity’s skeletal poses to animate.
- [BindTarget.blendShapeWeightsAtIndex(_:)](./blendshapeweightsatindex%28_%29.md)
- [case blendShapeWeightsWithID(BlendShapeWeightsData.ID)](./blendshapeweightswithid%28_%29.md)
- [static func material(Int) -> BindTarget.MaterialPath](./material%28_%29.md)
  Generates a complex bind path from one of an entity’s materials.
- [BindTarget.TextureCoordinateTransformPath](./texturecoordinatetransformpath.md)
  The texture coordinate parameters for a given texture layer that an animation can target.
- [BindTarget.IkSolverPath](./iksolverpath.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/materialpath)*