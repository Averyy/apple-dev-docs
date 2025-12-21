# BillboardComponent

**Framework**: RealityKit  
**Kind**: struct

A component that orients an entity instance so that it continuously points toward the active camera.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct BillboardComponent
```

#### Overview

The `BillboardComponent` automatically adjusts an entity’s orientation so that its z-axis keeps pointing in the direction of the main camera in a RealityKit scene.

Add a `BillboardComponent` to any entity by passing it to an entity’s [`set(_:)`](entity/componentset/set(_:)-8sii2.md) method.

```swift
entity.components.set(BillboardComponent())
```

The entity immediately reorients itself so that it faces the scene’s active camera.

| Without `BillboardComponent` | With `BillboardComponent` |
| --- | --- |
| ![An image of a vintage-style toy robot in a living room scene. The robot is facing about 45 degrees to the left and down from the viewer’s perspective.](https://docs-assets.developer.apple.com/published/eeff1917f6f47d0a52a049afc17fc1b4/billboardcomponent-robot-side-above-without.jpg) | ![An image of a vintage-style toy robot in a living room scene. The robot is facing directly towards the viewer.](https://docs-assets.developer.apple.com/published/83e2c31b61c7e99ba2df03efd08d302b/billboardcomponent-robot-side-above-with.jpg) |

> ❗ **Important**: An entity with `BillboardComponent` doesn’t provide access to its end orientation. Requesting the entity’s orientation through its transform returns only the unaltered orientation.

For an example of how to animate [`blendFactor`](billboardcomponent/blendfactor.md), see [`BillboardAction`](billboardaction.md).

## Topics

### Initializers
- [init()](billboardcomponent/init.md)
  Creates a billboard component that points an entity’s positive z-axis directly toward the active camera.
### Instance Properties
- [var blendFactor: Float](billboardcomponent/blendfactor.md)
  The degree at which the entity rotates toward the camera.

## Relationships

### Conforms To
- [Component](component.md)
- [Copyable](../Swift/Copyable.md)

## See Also

- [struct HoverEffectComponent](hovereffectcomponent.md)
  A component that applies a visual effect to a hierarchy of entities when a person looks at or selects an entity.
- [struct EnvironmentBlendingComponent](environmentblendingcomponent.md)
  A component that controls how an entity blends visually with objects in the local environment.
- [struct LensDistortionData](lensdistortiondata.md)
  A description of estimated lens distortion that can be used to rectify images.
- [struct ImagePresentationComponent](imagepresentationcomponent.md)
  A component that supports general image presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/billboardcomponent)*