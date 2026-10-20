# BindPath.Part

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

An individual piece of a larger path that refers to the target of an animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
enum Part
```

#### Overview

Path-based instances of [`bindTarget`](../animationdefinition/bindtarget.md), or those identified by the [`BindTarget.path(_:)`](../bindtarget/path%28_%29.md) call, consist of one or more components identified by these enumeration options.

For example, the succession of [`BindPath.Part`](./part.md) calls in the following code results in a path with a [`parts`](./parts.md) array that contains three components: `entityA`, `entityB`, and `myInt`.

```swift
let target3: BindTarget = .entity("entityA").entity("entityB").parameter("myInt")
```

## Topics

### Choosing the path component
- [BindPath.Part.anchorEntity(_:)](./part/anchorentity%28_%29.md)
  A path component for the scene’s anchor entity.
- [BindPath.Part.entity(_:)](./part/entity%28_%29.md)
  A path component for a nested entity.
- [BindPath.Part.jointTransforms](./part/jointtransforms.md)
  A path component to animate joint transforms.
- [BindPath.Part.parameter(_:)](./part/parameter%28_%29.md)
  A path component to animate a named parameter.
- [BindPath.Part.scene(_:)](./part/scene%28_%29.md)
  A path component for a nested scene.
- [BindPath.Part.transform](./part/transform.md)
  A path component to animate a transform.
### Accessing path parts
- [BindPath.Part.rootMotion](./part/rootmotion.md)
  Identifies a sampled transform animation as root motion for its target entity.
### Operators
- [static func == (BindPath.Part, BindPath.Part) -> Bool](./part/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two components of a bind path are equal.
### Enumeration Cases
- [BindPath.Part.billboardBlendFactor](./part/billboardblendfactor.md)
- [BindPath.Part.blendShapeWeights](./part/blendshapeweights.md)
  An option the entity’s blend shape weights animate. Requires that the entity has a BlendShapeWeightsComponent. Can be indexed by blend shape index or by blend shape name.  Default is by index 0.
- [BindPath.Part.blendShapeWeightsAtIndex(_:)](./part/blendshapeweightsatindex%28_%29.md)
- [case blendShapeWeightsWithID(BlendShapeWeightsData.ID)](./part/blendshapeweightswithid%28_%29.md)
- [case ikConstraintLookAtTarget(IKComponent.Constraint.ID)](./part/ikconstraintlookattarget%28_%29.md)
  A path component to an IK solver’s constraint target look at position.
- [case ikConstraintTarget(IKComponent.Constraint.ID)](./part/ikconstrainttarget%28_%29.md)
  A path component to an IK solver’s constraint target transform.
- [case ikSolver(IKComponent.Solver.ID?)](./part/iksolver%28_%29.md)
  A path component to an IK solver instance.
- [BindPath.Part.material(_:)](./part/material%28_%29.md)
  A path component to animate a material property.
- [BindPath.Part.materialParameter(_:)](./part/materialparameter%28_%29.md)
  A path component to name a material parameter to animate
- [BindPath.Part.opacity](./part/opacity.md)
  An path component to animate an opacity. Requires that the entity has an OpacityComponent
- [case skeletalPose(SkeletalPose.ID)](./part/skeletalpose%28_%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)

## See Also

### Composing a property identifier
- [var parts: [BindPath.Part]](./parts.md)
  An array of the individual components of a complete bind path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindpath/part)*