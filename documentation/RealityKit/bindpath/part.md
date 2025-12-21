# BindPath.Part

**Framework**: RealityKit  
**Kind**: enum

An individual piece of a larger path that refers to the target of an animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
enum Part
```

#### Overview

Path-based instances of [`bindTarget`](animationdefinition/bindtarget.md), or those identified by the [`BindTarget.path(_:)`](bindtarget/path(_:).md) call, consist of one or more components identified by these enumeration options.

For example, the succession of [`BindPath.Part`](bindpath/part.md) calls in the following code results in a path with a [`parts`](bindpath/parts.md) array that contains three components: `entityA`, `entityB`, and `myInt`.

```swift
let target3: BindTarget = .entity("entityA").entity("entityB").parameter("myInt")
```

## Topics

### Choosing the path component
- [BindPath.Part.anchorEntity(_:)](bindpath/part/anchorentity(_:).md)
  A path component for the scene’s anchor entity.
- [BindPath.Part.entity(_:)](bindpath/part/entity(_:).md)
  A path component for a nested entity.
- [BindPath.Part.jointTransforms](bindpath/part/jointtransforms.md)
  A path component to animate joint transforms.
- [BindPath.Part.parameter(_:)](bindpath/part/parameter(_:).md)
  A path component to animate a named parameter.
- [BindPath.Part.scene(_:)](bindpath/part/scene(_:).md)
  A path component for a nested scene.
- [BindPath.Part.transform](bindpath/part/transform.md)
  A path component to animate a transform.
### Comparing bind parts
- [static func == (BindPath.Part, BindPath.Part) -> Bool](bindpath/part/==(_:_:).md)
  Returns a Boolean value that indicates whether two components of a bind path are equal.
### Enumeration Cases
- [BindPath.Part.billboardBlendFactor](bindpath/part/billboardblendfactor.md)
- [BindPath.Part.blendShapeWeights](bindpath/part/blendshapeweights.md)
  An option the entity’s blend shape weights animate. Requires that the entity has a BlendShapeWeightsComponent. Can be indexed by blend shape index or by blend shape name.  Default is by index 0.
- [BindPath.Part.blendShapeWeightsAtIndex(_:)](bindpath/part/blendshapeweightsatindex(_:).md)
- [case blendShapeWeightsWithID(BlendShapeWeightsData.ID)](bindpath/part/blendshapeweightswithid(_:).md)
- [case ikConstraintLookAtTarget(IKComponent.Constraint.ID)](bindpath/part/ikconstraintlookattarget(_:).md)
  A path component to an IK solver’s constraint target look at position.
- [case ikConstraintTarget(IKComponent.Constraint.ID)](bindpath/part/ikconstrainttarget(_:).md)
  A path component to an IK solver’s constraint target transform.
- [case ikSolver(IKComponent.Solver.ID?)](bindpath/part/iksolver(_:).md)
  A path component to an IK solver instance.
- [BindPath.Part.material(_:)](bindpath/part/material(_:).md)
  A path component to animate a material property.
- [BindPath.Part.materialParameter(_:)](bindpath/part/materialparameter(_:).md)
  A path component to name a material parameter to animate
- [BindPath.Part.opacity](bindpath/part/opacity.md)
  An path component to animate an opacity. Requires that the entity has an OpacityComponent
- [case skeletalPose(SkeletalPose.ID)](bindpath/part/skeletalpose(_:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [var parts: [BindPath.Part]](bindpath/parts.md)
  An array of the individual components of a complete bind path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindpath/part)*