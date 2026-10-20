# BindTarget.EntityPath

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A bind path context for a particular entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct EntityPath
```

#### Overview

This structure references all the animated properties of an entity.

To access the animated properties of one of the entity’s children, call [`entity(_:)`](./entitypath/entity%28_%29.md) and pass in the child’s name.

## Topics

### Accessing a bind target
- [var jointTransforms: BindTarget](./entitypath/jointtransforms.md)
  A bind target for the entity’s joint transforms.
- [var transform: BindTarget](./entitypath/transform.md)
  A bind target for the entity’s transform.
- [var `self`: BindTarget](./entitypath/self.md)
  A bind target for the entity.
- [func parameter(String) -> BindTarget](./entitypath/parameter%28_%29.md)
  Provides a bind target for a particular animated property.
### Accessing child-entity paths
- [func entity(String) -> BindTarget.EntityPath](./entitypath/entity%28_%29.md)
  Provides a child entity’s path.
### Accessing root motion
- [var rootMotion: BindTarget](./entitypath/rootmotion.md)
  The root motion bind target for this entity.
### Instance Properties
- [var billboardBlendFactor: BindTarget](./entitypath/billboardblendfactor.md)
- [var opacity: BindTarget](./entitypath/opacity.md)
  A bind target for the entity’s opacity.. Requires that the entity has an OpacityComponent
### Instance Methods
- [func blendShapeWeights() -> BindTarget](./entitypath/blendshapeweights%28%29.md)
  A bind target for the entity’s blend shape weights.
- [func blendShapeWeightsAtIndex(Int) -> BindTarget](./entitypath/blendshapeweightsatindex%28_%29.md)
- [func blendShapeWeightsWithID(BlendShapeWeightsData.ID) -> BindTarget](./entitypath/blendshapeweightswithid%28_%29.md)
- [func ikSolver(IKComponent.Solver.ID?) -> BindTarget.IkSolverPath](./entitypath/iksolver%28_%29.md)
- [func material(Int) -> BindTarget.MaterialPath](./entitypath/material%28_%29.md)
  Provides a specified material’s path.
- [func skeletalPose(SkeletalPose.ID) -> BindTarget](./entitypath/skeletalpose%28_%29.md)

## See Also

### Targeting entities and scenes
- [static func scene(String) -> BindTarget.ScenePath](./scene%28_%29.md)
  Generates a bind path from a particular scene.
- [BindTarget.ScenePath](./scenepath.md)
  A bind path for a particular scene.
- [static func anchorEntity(String) -> BindTarget.EntityPath](./anchorentity%28_%29.md)
  Generates a complex bind path from a particular anchor entity in the scene.
- [static func entity(String) -> BindTarget.EntityPath](./entity%28_%29.md)
  Generates a complex bind path from a particular child entity of the current entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/entitypath)*