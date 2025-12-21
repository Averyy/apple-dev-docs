# EnvironmentBlendingComponent

**Framework**: RealityKit  
**Kind**: struct

A component that controls how an entity blends visually with objects in the local environment.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct EnvironmentBlendingComponent
```

#### Overview

Use this component in your visionOS apps to allow physical objects in the real world to occlude your virtual content.

To enable the surroundings to occlude an entity, you can set the [`preferredBlendingMode`](environmentblendingcomponent/preferredblendingmode.md) to [`occluded(by:)`](environmentblendingcomponent/blendingmode/occluded(by:).md), specifying the environment type as [`EnvironmentBlendingComponent.EnvironmentType.surroundings`](environmentblendingcomponent/environmenttype/surroundings.md):

```swift
let blendingComponent = EnvironmentBlendingComponent(
    preferredBlendingMode: .occluded(by: .surroundings)
)

let boxMesh = MeshResource.generateBox(width: 0.5, height: 0.5, depth: 0.5)
let boxModel = ModelComponent(mesh: boxMesh, materials: [PhysicallyBasedMaterial()])
let occludedBoxMesh = Entity(components: blendingComponent, boxModel)
```

Alternatively, you can also disable the occlusion for the same entity by setting the [`preferredBlendingMode`](environmentblendingcomponent/preferredblendingmode.md) to [`default`](environmentblendingcomponent/blendingmode/default.md). If you deactivate and reactivate an [`Entity`](entity.md) while it has an active `EnvironmentBlendingComponent`, it may take a few frames for visionOS to generate an occlusion map before it fades the entity in.

An entity with occlusion enabled behaves like a real-world passthrough object. It always renders behind other virtual contents that don’t have occlusion enabled. In addition, it doesn’t receive input events from the user if it’s behind a real-world object.

Occlusion only works in mixed or progressive immersive space. For progressive space, it works only for entities outside of the portal world. When the portal mask expands and overlaps with those entities by turning the Digital Crown, it fades those entities out gradually. Occlusion doesn’t work in full space, or in a window or volume in the Shared Space.

`EnvironmentBlendingComponent` applies occlusion recursively to the entity and its descendant entities. A sub-entity’s component set overrides the top-level component.

## Topics

### Structures
- [EnvironmentBlendingComponent.BlendingMode](environmentblendingcomponent/blendingmode.md)
  A struct that encapsulates the different environment-blending modes that can be applied to an entity.
### Initializers
- [init()](environmentblendingcomponent/init.md)
  Creates an instance of the component using the `default` blending mode.
- [init(preferredBlendingMode: EnvironmentBlendingComponent.BlendingMode)](environmentblendingcomponent/init(preferredblendingmode:).md)
  Creates an instance of the component.
### Instance Properties
- [var preferredBlendingMode: EnvironmentBlendingComponent.BlendingMode](environmentblendingcomponent/preferredblendingmode.md)
  Specifies how the entity and its descendants blend against environments which encompass them.
### Enumerations
- [EnvironmentBlendingComponent.EnvironmentType](environmentblendingcomponent/environmenttype.md)
  An enumeration of the environment types which support environment-blending.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct HoverEffectComponent](hovereffectcomponent.md)
  A component that applies a visual effect to a hierarchy of entities when a person looks at or selects an entity.
- [struct BillboardComponent](billboardcomponent.md)
  A component that orients an entity instance so that it continuously points toward the active camera.
- [struct LensDistortionData](lensdistortiondata.md)
  A description of estimated lens distortion that can be used to rectify images.
- [struct ImagePresentationComponent](imagepresentationcomponent.md)
  A component that supports general image presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentblendingcomponent)*