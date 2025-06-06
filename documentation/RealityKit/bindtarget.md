# BindTarget

**Framework**: RealityKit  
**Kind**: enum

A reference to a particular scene, entity, or property that animates.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
enum BindTarget
```

#### Overview

This structure describes a reference to an animated property. The property may be a transform, collection of joint transforms, an arbitrary named property of an entity, or the property of a nested entity.

For nested entities, the [`BindTarget.path(_:)`](bindtarget/path(_:).md) case returns a [`BindPath`](bindpath.md) instance that contains an array of  ([`BindPath.Part`](bindpath/part.md)). Each part identifies one or more nested, named entities or scenes, followed by the property to animate.

## Topics

### Choosing a bind target
- [case `internal`(InternalBindPath)](bindtarget/internal(_:).md)
  A bind target that refers to a framework-provided property.
- [BindTarget.jointTransforms](bindtarget/jointtransforms.md)
  An option that specifies that the entity’s joint transforms animate.
- [BindTarget.parameter(_:)](bindtarget/parameter(_:).md)
  Provides a property that animates from the given textual name.
- [BindTarget.path(_:)](bindtarget/path(_:).md)
  Provides a complex bind path capable of animating additional entities other than the current entity.
- [BindTarget.transform](bindtarget/transform.md)
  A option that specifies that the target entity’s transform animates.
### Comparing bind targets
- [static func == (BindTarget, BindTarget) -> Bool](bindtarget/==(_:_:).md)
  Returns a Boolean value that indicates whether two bind targets are equal.
- [static func != (Self, Self) -> Bool](bindtarget/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Targeting entities and scenes
- [static func scene(String) -> BindTarget.ScenePath](bindtarget/scene(_:).md)
  Generates a bind path from a particular scene.
- [BindTarget.ScenePath](bindtarget/scenepath.md)
  A bind path for a particular scene.
- [static func anchorEntity(String) -> BindTarget.EntityPath](bindtarget/anchorentity(_:).md)
  Generates a complex bind path from a particular anchor entity in the scene.
- [static func entity(String) -> BindTarget.EntityPath](bindtarget/entity(_:).md)
  Generates a complex bind path from a particular child entity of the current entity.
- [BindTarget.EntityPath](bindtarget/entitypath.md)
  A bind path context for a particular entity.
### Structures
- [BindTarget.IkSolverPath](bindtarget/iksolverpath.md)
- [BindTarget.MaterialPath](bindtarget/materialpath.md)
  Material parameters that an animation can target.
- [BindTarget.TextureCoordinateTransformPath](bindtarget/texturecoordinatetransformpath.md)
  The texture coordinate parameters for a given texture layer that an animation can target.
### Enumeration Cases
- [BindTarget.billboardBlendFactor](bindtarget/billboardblendfactor.md)
- [BindTarget.blendShapeWeights](bindtarget/blendshapeweights.md)
  An option the entity’s blend shape weights animate. Requires that the entity has a BlendShapeWeightsComponent.
- [BindTarget.blendShapeWeightsAtIndex(_:)](bindtarget/blendshapeweightsatindex(_:).md)
- [case blendShapeWeightsWithID(BlendShapeWeightsData.ID)](bindtarget/blendshapeweightswithid(_:).md)
- [BindTarget.opacity](bindtarget/opacity.md)
  An option that specifies that the entity’s opacity to animate. Requires that the entity has an OpacityComponent
- [BindTarget.skeletalPose(_:)](bindtarget/skeletalpose(_:).md)
  An option that specifies one of the entity’s skeletal poses to animate.
### Type Methods
- [static func material(Int) -> BindTarget.MaterialPath](bindtarget/material(_:).md)
  Generates a complex bind path from one of an entity’s materials.
### Default Implementations
- [Equatable Implementations](bindtarget/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct BindPath](bindpath.md)
  The components of a target’s path that refer to the animation properties of a nested scene or entity.
- [struct BindableValue](bindablevalue.md)
  The value of a bindable target.
- [struct BindableValuesReference](bindablevaluesreference.md)
  A reference to a bindable value of an animation.
- [struct ParameterSet](parameterset.md)
  A reference to general-purpose entity parameters for animations.
- [struct InternalBindPath](internalbindpath.md)
  A bind target for framework-provided properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget)*