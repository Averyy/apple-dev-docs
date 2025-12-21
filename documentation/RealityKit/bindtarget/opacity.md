# BindTarget.opacity

**Framework**: RealityKit  
**Kind**: case

An option that specifies that the entity’s opacity to animate. Requires that the entity has an OpacityComponent

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
case opacity
```

## See Also

- [BindTarget.billboardBlendFactor](bindtarget/billboardblendfactor.md)
- [BindTarget.blendShapeWeights](bindtarget/blendshapeweights.md)
  An option the entity’s blend shape weights animate. Requires that the entity has a BlendShapeWeightsComponent.
- [BindTarget.blendShapeWeightsAtIndex(_:)](bindtarget/blendshapeweightsatindex(_:).md)
- [case blendShapeWeightsWithID(BlendShapeWeightsData.ID)](bindtarget/blendshapeweightswithid(_:).md)
- [static func material(Int) -> BindTarget.MaterialPath](bindtarget/material(_:).md)
  Generates a complex bind path from one of an entity’s materials.
- [BindTarget.MaterialPath](bindtarget/materialpath.md)
  Material parameters that an animation can target.
- [BindTarget.TextureCoordinateTransformPath](bindtarget/texturecoordinatetransformpath.md)
  The texture coordinate parameters for a given texture layer that an animation can target.
- [BindTarget.IkSolverPath](bindtarget/iksolverpath.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/opacity)*