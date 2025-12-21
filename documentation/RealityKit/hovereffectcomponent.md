# HoverEffectComponent

**Framework**: RealityKit  
**Kind**: struct

A component that applies a visual effect to a hierarchy of entities when a person looks at or selects an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct HoverEffectComponent
```

#### Overview

Add a HoverEffectComponent to an entity to convey the entity can receive gestures or to separate parts that can be interacted with independently.

> **Note**: On visionOS, you hover over an entity by looking at or directly touching it. On other platforms, you hover over an entity by moving your mouse cursor over it.

> ❗ **Important**: Entities also need to have an [`InputTargetComponent`](inputtargetcomponent.md) and [`CollisionComponent`](collisioncomponent.md) to receive hover effects.

```swift
let boxSize = SIMD3<Float>(0.5, 0.1, 0.05)

let modelComponent = ModelComponent(
    mesh: MeshResource.generateBox(size: boxSize),
    materials: [SimpleMaterial(color: .black, roughness: 0.5, isMetallic: false)]
)
let collisionComponent = CollisionComponent(
    shapes: [ShapeResource.generateBox(size: boxSize)]
)
let inputTargetComponent = InputTargetComponent()
let hoverEffectComponent = HoverEffectComponent()

let entityA = Entity()
entityA.components.set([modelComponent, collisionComponent, inputTargetComponent, hoverEffectComponent])
```

The example code above produces the following scene.

##### Hierarchical Behavior

The `HoverEffectComponent` applies its effect to an entity’s entire hierarchy, which means that all the entity’s descendent entities inherit the effect when a person looks at (or selects) an entity.

```swift
let boxSize = SIMD3<Float>(0.5, 0.1, 0.05)

// Create a black box model, a matching collision component, and an input target component.
let modelComponent = ModelComponent(
    mesh: MeshResource.generateBox(size: boxSize),
    materials: [SimpleMaterial(color: .black, roughness: 0.5, isMetallic: false)]
)
let collisionComponent = CollisionComponent(
    shapes: [ShapeResource.generateBox(size: boxSize)]
)
let inputTargetComponent = InputTargetComponent()

// Create a default hover effect component.
let hoverEffectComponent = HoverEffectComponent()

let entityA = Entity()
entityA.components.set([modelComponent, collisionComponent, inputTargetComponent])

let entityB = entityA.clone(recursive: true)
let entityC = entityB.clone(recursive: true)

// B is a child of A.
entityA.addChild(entityB)
// C is a child of B.
entityB.addChild(entityC)

// Place B above its parent, A.
entityB.position.y = 0.1
// Place C above its parent, B.
entityC.position.y = 0.1

entityA.components.set(hoverEffectComponent)
```

In this example only the highest entity in the hierarchy has a `HoverEffectComponent`. Activating this hover effect causes all of its children to display the same effect.

##### Grouping Multiple Hover Effects

The optional [`groupID`](hovereffectcomponent/hovereffect-swift.struct/groupid.md) connects entities so that they activate their hover effects together, which is independent from the entities’ hierarchy. When someone hovers over any entity in the group, all entities with the same [`HoverEffectComponent.GroupID`](hovereffectcomponent/groupid.md) instance start their hover effects together.

```swift
let boxSize = SIMD3<Float>(0.5, 0.1, 0.05)
let modelComponent = ModelComponent(
    mesh: MeshResource.generateBox(size: boxSize, cornerRadius: 0.2),
    materials: [SimpleMaterial(color: .black, roughness: 0.5, isMetallic: false)]
)
let collisionComponent = CollisionComponent(
    shapes: [ShapeResource.generateBox(size: boxSize)]
)
let inputTargetComponent = InputTargetComponent()

let hoverEntityA = Entity(components:
    modelComponent, collisionComponent, inputTargetComponent
)
let hoverEntityB = hoverEntityA.clone(recursive: true)
hoverEntityB.position.y = -0.1
let hoverEntityC = hoverEntityA.clone(recursive: true)
hoverEntityC.position.y = -0.2

content.add(hoverEntityA)
content.add(hoverEntityB)
content.add(hoverEntityC)

// Create hover effect components for the two topmost entities in the scene.
var hoverA = HoverEffectComponent(
    .highlight(HoverEffectComponent.HighlightHoverEffectStyle(
            color: .green, strength: 2.0
        )))

var hoverB = HoverEffectComponent(
    .highlight(HoverEffectComponent.HighlightHoverEffectStyle(
            color: .yellow, strength: 2.0
        )))

// Create a `HoverEffectComponent.GroupID` instance and assign it to the hover effect components for both `entityA` and `entityB`.
let topGroupID = HoverEffectComponent.GroupID()
hoverA.hoverEffect.groupID = topGroupID
hoverB.hoverEffect.groupID = topGroupID
hoverEntityA.components.set(hoverA)
hoverEntityB.components.set(hoverB)

// Create hover effect component for the bottommost entity in the scnee.
var hoverC = HoverEffectComponent(
    .highlight(HoverEffectComponent.HighlightHoverEffectStyle(
            color: .blue, strength: 2.0
        )))

// Create a `HoverEffectComponent.GroupID` instance and assign it to the hover effect component for `entityC`
let bottomGroupID = HoverEffectComponent.GroupID()
hoverC.hoverEffect.groupID = bottomGroupID
hoverEntityC.components.set(hoverC)

```

In this example, the top and middle entities, `entityA` and `entityB`, have a [`HoverEffectComponent`](hovereffectcomponent.md) with the same group identifier. However, the bottom entity, `entityC`, has a different group ID. The top amd middle entity both glow when a person activates either one. The bottom entity glows separately and only when someone activates it directly.

##### Styles

You can customize the visual effect of the `HoverEffectComponent` through the use of styles.

The [`HoverEffectComponent.SpotlightHoverEffectStyle`](hovereffectcomponent/spotlighthovereffectstyle.md) represents a feathered effect that follows the hover location on the entity. This is the default effect RealityKit uses if you create a `HoverEffectComponent` with the default initializer, [`init()`](hovereffectcomponent/init().md). You can customize the color and strength of this effect by passing values into the [`HoverEffectComponent.SpotlightHoverEffectStyle`](hovereffectcomponent/spotlighthovereffectstyle.md) constructor.

```swift
let hoverComponent = HoverEffectComponent(.spotlight(
    HoverEffectComponent.SpotlightHoverEffectStyle(
        color: .green, strength: 2.0
    )
))
```

The [`HoverEffectComponent.HighlightHoverEffectStyle`](hovereffectcomponent/highlighthovereffectstyle.md) applies a uniform glow to the entity in addition to the feathered effect from the [`HoverEffectComponent.SpotlightHoverEffectStyle`](hovereffectcomponent/spotlighthovereffectstyle.md). You can customize the color and strength of this effect by passing values into the [`HoverEffectComponent.HighlightHoverEffectStyle`](hovereffectcomponent/highlighthovereffectstyle.md) constructor.

```swift
let hoverComponent = HoverEffectComponent(.highlight(
    HoverEffectComponent.HighlightHoverEffectStyle(
        color: .green, strength: 2.0
    )
))
```

##### Opacity Functions

Customize how a `HoverEffectComponent` presents on a partially or fully transparent material with the following opacity functions:

> **Note**: Opacity functions can’t be applied to `HoverEffectComponents` that use [`HoverEffectComponent.ShaderHoverEffectInputs`](hovereffectcomponent/shaderhovereffectinputs.md).

##### Shader Inputs

Pass [`HoverEffectComponent.ShaderHoverEffectInputs`](hovereffectcomponent/shaderhovereffectinputs.md) to the `HoverEffectComponent` constructor with [`shader(_:)`](hovereffectcomponent/hovereffect-swift.struct/shader(_:).md) to activate the `Hover State` Shader Graph node in a [`ShaderGraphMaterial`](shadergraphmaterial.md). Apply the [`ShaderGraphMaterial`](shadergraphmaterial.md) to the entity’s [`ModelComponent`](modelcomponent.md) when using this effect.

```swift
let boxSize = SIMD3<Float>(0.5, 0.1, 0.05)

let customMaterial = try! await ShaderGraphMaterial(
   named: "/Root/HoverEffectComponentDemo",
   from: Bundle.main.url(forResource: "DemoScene", withExtension: "usda")!
)

let entity = ModelEntity(
    mesh: MeshResource.generateBox(size: boxSize),
    materials: [customMaterial]
)

// ...

let hoverComponent = HoverEffectComponent(.shader(
    HoverEffectComponent.ShaderHoverEffectInputs(
        fadeInDuration: 1.0, fadeOutDuration: 1.0
    )
))
entity.components.set(hoverComponent)
```

This shader graph represents a red and blue effect that interpolates between each color using a sine wave.

![A screenshot of an app window with a shader graph visible. The shader graph represents a red and blue effect that interpolates between each color using a sine wave. On the bottom right is a purple cube representing the effect halfway between red and blue.](https://docs-assets.developer.apple.com/published/87a01f2abcf75f901637dca380b007c7/hovereffectcomponent-shader-graph.jpg)

Hovering over the entity displays the following effect.

## Topics

### Structures
- [HoverEffectComponent.GroupID](hovereffectcomponent/groupid.md)
  A struct for grouping hover effects together.
- [HoverEffectComponent.HighlightHoverEffectStyle](hovereffectcomponent/highlighthovereffectstyle.md)
  A type that configures the visual aspects of a highlight hover effect for an entity
- [HoverEffectComponent.HoverEffect](hovereffectcomponent/hovereffect-swift.struct.md)
  An effect that applies when a person looks at or directly touches the entity.
- [HoverEffectComponent.ShaderHoverEffectInputs](hovereffectcomponent/shaderhovereffectinputs.md)
  A type that configures the visual aspects of a hover effect that applies a custom material
- [HoverEffectComponent.SpotlightHoverEffectStyle](hovereffectcomponent/spotlighthovereffectstyle.md)
  A type that configures the visual aspects of a spotlight hover effect for an entity.
### Initializers
- [init()](hovereffectcomponent/init.md)
  Creates a hover effect component with a default spotlight effect.
- [init(HoverEffectComponent.HoverEffect)](hovereffectcomponent/init(_:).md)
  Creates a hover effect component with a particular visualization effect.
### Instance Properties
- [var hoverEffect: HoverEffectComponent.HoverEffect](hovereffectcomponent/hovereffect-swift.property.md)
  The current hover effect of the hover effect component.
### Enumerations
- [HoverEffectComponent.OpacityFunction](hovereffectcomponent/opacityfunction.md)
  The blending technique options a hover effect applies to its entity’s base material.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct BillboardComponent](billboardcomponent.md)
  A component that orients an entity instance so that it continuously points toward the active camera.
- [struct EnvironmentBlendingComponent](environmentblendingcomponent.md)
  A component that controls how an entity blends visually with objects in the local environment.
- [struct LensDistortionData](lensdistortiondata.md)
  A description of estimated lens distortion that can be used to rectify images.
- [struct ImagePresentationComponent](imagepresentationcomponent.md)
  A component that supports general image presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hovereffectcomponent)*