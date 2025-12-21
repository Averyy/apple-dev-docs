# BindTarget.TextureCoordinateTransformPath

**Framework**: RealityKit  
**Kind**: struct

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

#### Overview

When `index` equals `0`, the structure refers to the primary texture coordinates. When `index` equals `1`, the structure refers to the secondary texture coordinates.

## Topics

### Instance Properties
- [var offset: BindTarget](bindtarget/texturecoordinatetransformpath/offset.md)

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
- [BindTarget.MaterialPath](bindtarget/materialpath.md)
  Material parameters that an animation can target.
- [BindTarget.IkSolverPath](bindtarget/iksolverpath.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/texturecoordinatetransformpath)*