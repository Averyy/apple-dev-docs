# ModelSortGroupComponent

**Framework**: RealityKit  
**Kind**: struct

A component that configures the rendering order for an entity’s model.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct ModelSortGroupComponent
```

#### Overview

Tell the renderer to draw a model on top of another by adding a `ModelSortGroupComponent` instance to both entities.

A model sort group component gives you control over the rendering order for entities within the same [`ModelSortGroup`](modelsortgroup.md). You can configure the group to render models in a specific order, even if that order contradicts their relative positions to each other in the scene.

The scenario below shows a living room scene that has two rectangular cuboids which overlap and form the shape of a plus symbol. The blue cuboid is opaque and taller than it is wide. The red cuboid is transparent and wider than it is tall.

The sections below demonstrate how to change the default behavior by configuring the properties of the model sort group component.

##### Set the Draw Order

To tell the renderer to draw the red cuboid before the blue one, add a `ModelSortGroupComponent` instance to both cuboids. Then set both component’s [`order`](modelsortgroupcomponent/order.md) property so that the red cuboid’s component has a smaller value than the blue cuboid’s component.

```swift
let redCuboid = Entity()
let blueCuboid = Entity()

// ...

// Create a group for both cuboids.
let group = ModelSortGroup(depthPass: nil)

let redSortComponent = ModelSortGroupComponent(
    group: group,
    order: 1
)

redCuboid.components.set(redSortComponent)

let blueSortComponent = ModelSortGroupComponent(
    group: group,
    order: 2
)
blueCuboid.components.set(blueSortComponent)
```

The renderer draws the red cuboid first and then doesn’t draw the part of the blue cuboid where the two cuboids overlap because the nearest face of the red cuboid in the overlapping area is closer to the camera.

If the renderer instead draws the blue cuboid first, and the translucent red cuboid second, the blue cuboid is once again visible in the overlapping area.

Rendering the blue cuboid produces the same result as if the two cuboids weren’t in a sort group.

##### Set the Depth Pass

In the examples in the previous section, the renderer draws each model’s depth and color together, at the same time.

To draw each entity’s color and depth separately, set the [`depthPass`](modelsortgroup/depthpass-swift.property.md) property of a [`ModelSortGroup`](modelsortgroup.md) instance, which changes the rendering sequence for each model in the group that either draws their colors first or their depths first.

> 💡 **Tip**: You can also set the property with the [`init(depthPass:)`](modelsortgroup/init(depthpass:).md) initializer.

To draw each model’s color on the first pass and then the depth, set the property to [`ModelSortGroup.DepthPass.postPass`](modelsortgroup/depthpass-swift.enum/postpass.md).

```swift
// Draw the color first, depth second.
let group = ModelSortGroup(depthPass: .postPass)
```

| **Red First** | **Blue First** |
| --- | --- |
| ![A screenshot of a living room scene with two rectangular cuboids that overlap. The vertical cuboid is an opaque blue, and the horizontal cuboid is a translucent red. The red cuboid appears behind the blue one.](/images/com.apple.RealityKit/modelsortgroupcomponent-postpass-redfirst.jpg) | ![A screenshot of a living room scene with two rectangular cuboids that overlap. The vertical cuboid is an opaque blue, and the horizontal cuboid is a translucent red. The red cuboid appears in front of the blue one, which gives the area where they overlap a purple hue.](/images/com.apple.RealityKit/modelsortgroupcomponent-postpass-bluefirst.jpg) |

The [`ModelSortGroup.DepthPass.postPass`](modelsortgroup/depthpass-swift.enum/postpass.md) option tells the renderer to draw entities in reverse order, which gives the effect that the last model it draws appears in front.

The depth pass [`ModelSortGroup.DepthPass.prePass`](modelsortgroup/depthpass-swift.enum/prepass.md) draws each entity’s depth on the first pass, then their color.

```swift
// Draw the depth first, color second.
let group = ModelSortGroup(depthPass: .prePass)
```

| **Red First** | **Blue First** |
| --- | --- |
| ![A screenshot of a living room scene with two rectangular cuboids that overlap. The vertical cuboid is an opaque blue, and the horizontal cuboid is a translucent red. The red cuboid appears in front of the blue one, and in the area where they overlap, the blue cuboid isn’t visible, which reveals the scene’s background through the red one.](/images/com.apple.RealityKit/modelsortgroupcomponent-prepass-redfirst.jpg) | ![A screenshot of a living room scene with two rectangular cuboids that overlap. The vertical cuboid is an opaque blue, and the horizontal cuboid is a translucent red. The red cuboid appears in front of the blue one, and in the area where they overlap, the blue cuboid isn’t visible, which reveals the scene’s background through the red one.](/images/com.apple.RealityKit/modelsortgroupcomponent-prepass-bluefirst.jpg) |

The [`ModelSortGroup.DepthPass.prePass`](modelsortgroup/depthpass-swift.enum/prepass.md) option tells the renderer to write the depth buffer for the group’s entities first. The renderer doesn’t draw the blue cuboid in the overlapping area, regardless of order, because the red cuboid has a shallower depth in all parts of the overlapping area.

> 💡 **Tip**: Check out [`Swift Splash`](https://developer.apple.com/documentation/visionos/swift-splash) which has an implementation that leverages `ModelSortGroupComponent`.

## Topics

### Initializers
- [init(group: ModelSortGroup, order: Int32)](modelsortgroupcomponent/init(group:order:).md)
  Creates a model sort group component.
### Instance Properties
- [var group: ModelSortGroup](modelsortgroupcomponent/group.md)
  The group that the component’s entity belongs to.
- [var order: Int32](modelsortgroupcomponent/order.md)
  An integer value that represents when the renderer draws the model relative to other the models in its group.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct ModelSortGroup](modelsortgroup.md)
  A group that you assign to multiple entities to tell the renderer what order and how to render the entities in the group.
- [struct OpacityComponent](opacitycomponent.md)
  A component that controls the opacity of an entity and its descendants.
- [struct AdaptiveResolutionComponent](adaptiveresolutioncomponent.md)
  A component that provides the suggested pixels per meter necessary to render an object.
- [struct ModelDebugOptionsComponent](modeldebugoptionscomponent.md)
  A component that changes how RealityKit renders its entity to help with debugging.
- [struct MeshInstancesComponent](meshinstancescomponent.md)
  A component that performs GPU instancing on the model of the same entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelsortgroupcomponent)*