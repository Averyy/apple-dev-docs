# BindTarget.TextureCoordinateTransformPath

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The texture coordinate parameters for a given texture layer that an animation can target.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct TextureCoordinateTransformPath
```

## Overview

When `index` equals `0`, the structure refers to the primary texture coordinates. When `index` equals `1`, the structure refers to the secondary texture coordinates.

## Topics

### Instance Properties
- [var offset: BindTarget](./texturecoordinatetransformpath/offset.md)

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
- [BindTarget.MaterialPath](./materialpath.md)
  Material parameters that an animation can target.
- [BindTarget.IkSolverPath](./iksolverpath.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/texturecoordinatetransformpath)*