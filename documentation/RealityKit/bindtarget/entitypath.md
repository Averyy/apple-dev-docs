# BindTarget.EntityPath

**Framework**: RealityKit  
**Kind**: struct

A bind path context for a particular entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct EntityPath
```

#### Overview

This structure references all the animated properties of an entity.

To access the animated properties of one of the entity’s children, call [`entity(_:)`](bindtarget/entitypath/entity(_:).md) and pass in the child’s name.

## Topics

### Accessing a bind target
- [var jointTransforms: BindTarget](bindtarget/entitypath/jointtransforms.md)
  A bind target for the entity’s joint transforms.
- [var transform: BindTarget](bindtarget/entitypath/transform.md)
  A bind target for the entity’s transform.
- [var `self`: BindTarget](bindtarget/entitypath/self.md)
  A bind target for the entity.
- [func parameter(String) -> BindTarget](bindtarget/entitypath/parameter(_:).md)
  Provides a bind target for a particular animated property.
### Accessing child-entity paths
- [func entity(String) -> BindTarget.EntityPath](bindtarget/entitypath/entity(_:).md)
  Provides a child entity’s path.
### Instance Properties
- [var billboardBlendFactor: BindTarget](bindtarget/entitypath/billboardblendfactor.md)
- [var opacity: BindTarget](bindtarget/entitypath/opacity.md)
  A bind target for the entity’s opacity.. Requires that the entity has an OpacityComponent
### Instance Methods
- [func blendShapeWeights() -> BindTarget](bindtarget/entitypath/blendshapeweights.md)
  A bind target for the entity’s blend shape weights.
- [func blendShapeWeightsAtIndex(Int) -> BindTarget](bindtarget/entitypath/blendshapeweightsatindex(_:).md)
- [func blendShapeWeightsWithID(BlendShapeWeightsData.ID) -> BindTarget](bindtarget/entitypath/blendshapeweightswithid(_:).md)
- [func ikSolver(IKComponent.Solver.ID?) -> BindTarget.IkSolverPath](bindtarget/entitypath/iksolver(_:).md)
- [func material(Int) -> BindTarget.MaterialPath](bindtarget/entitypath/material(_:).md)
  Provides a specified material’s path.
- [func skeletalPose(SkeletalPose.ID) -> BindTarget](bindtarget/entitypath/skeletalpose(_:).md)

## See Also

- [static func scene(String) -> BindTarget.ScenePath](bindtarget/scene(_:).md)
  Generates a bind path from a particular scene.
- [BindTarget.ScenePath](bindtarget/scenepath.md)
  A bind path for a particular scene.
- [static func anchorEntity(String) -> BindTarget.EntityPath](bindtarget/anchorentity(_:).md)
  Generates a complex bind path from a particular anchor entity in the scene.
- [static func entity(String) -> BindTarget.EntityPath](bindtarget/entity(_:).md)
  Generates a complex bind path from a particular child entity of the current entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/entitypath)*