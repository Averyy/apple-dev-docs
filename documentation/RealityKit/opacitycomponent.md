# OpacityComponent

**Framework**: RealityKit  
**Kind**: struct

A component that controls the opacity of an entity and its descendants.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct OpacityComponent
```

#### Overview

An opacity component multiplies its [`opacity`](opacitycomponent/opacity.md) property with all visual components the entity and its descendants own. Visual components include [`ModelComponent`](modelcomponent.md) and [`ParticleEmitterComponent`](particleemittercomponent.md). If a descendant also has its own opacity component, the system combines the two opacities by multiplying their values. The system repeats this pattern for the entity’s entire family tree.

For example, the following code sets a component’s opacity value to `0.5` for its entity:

```swift
// Load a USDZ model from a file, or create a model component.
let robot = try await Entity(named: "vintage_robot")

// Create an opacity component.
let opacityComponent = OpacityComponent(opacity: 0.5)

// Apply the opacity component to the robot entity.
robot.components.set(opacityComponent)
```

The following images show robot models with opacity values of `1.0` and `0.5`.

| `opacity: 1` | `opacity: 0.5` |
| --- | --- |
| ![An image of an opaque vintage-style toy robot in a living room scene. The robot is facing about 45 degrees to the left and down from the viewer’s perspective.](https://docs-assets.developer.apple.com/published/5a0d4c59785c56c39e5ef6e8b8b6e26a/opacitycomponent-full.jpg) | ![An image of a translucent vintage-style toy robot in a living room scene. The robot is facing about 45 degrees to the left and down from the viewer’s perspective.](https://docs-assets.developer.apple.com/published/75344498b9563f1b26fe1c2710602edd/opacitycomponent-half.jpg) |

## Topics

### Operators
- [static func == (OpacityComponent, OpacityComponent) -> Bool](opacitycomponent/==(_:_:).md)
  Returns a Boolean value that indicates whether two opacity components are equal.
### Initializers
- [init(opacity: Float)](opacitycomponent/init(opacity:).md)
  Creates a new opacity component.
### Instance Properties
- [var opacity: Float](opacitycomponent/opacity.md)
  The floating-point value the renderer applies to an entity and its descendants.

## Relationships

### Conforms To
- [Component](component.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct ModelSortGroupComponent](modelsortgroupcomponent.md)
  A component that configures the rendering order for an entity’s model.
- [struct ModelSortGroup](modelsortgroup.md)
  A group that you assign to multiple entities to tell the renderer what order and how to render the entities in the group.
- [struct AdaptiveResolutionComponent](adaptiveresolutioncomponent.md)
  A component that provides the suggested pixels per meter necessary to render an object.
- [struct ModelDebugOptionsComponent](modeldebugoptionscomponent.md)
  A component that changes how RealityKit renders its entity to help with debugging.
- [struct MeshInstancesComponent](meshinstancescomponent.md)
  A component that performs GPU instancing on the model of the same entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/opacitycomponent)*