# groupID

**Framework**: RealityKit  
**Kind**: property

An optional group identifier for the hover effect.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var groupID: HoverEffectComponent.GroupID? { get set }
```

#### Discussion

The system activates the hover effect entities that have the same [`HoverEffectComponent.GroupID`](hovereffectcomponent/groupid.md) instance at the same time when a person looks at it or hovers over any entity in the group.

##### Activating Hover Effects

The system activates hover effect entities with a `groupID` independently from the hierarchical activation behavior.

```swift
let boxSize = SIMD3<Float>(0.3, 0.1, 0.05)
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
hoverEntityB.position.x = -0.2
hoverEntityB.position.y = -0.15

let hoverEntityBB = hoverEntityA.clone(recursive: true)
hoverEntityBB.position.y = -0.15

let hoverEntityC = hoverEntityA.clone(recursive: true)
hoverEntityC.position.x = 0.2
hoverEntityC.position.y = -0.15

content.add(hoverEntityA)
hoverEntityA.addChild(hoverEntityB)
hoverEntityB.addChild(hoverEntityBB)
hoverEntityA.addChild(hoverEntityC)

// Create hover effect component for the top entity in the scene.
let hoverA = HoverEffectComponent(
    .highlight(HoverEffectComponent.HighlightHoverEffectStyle(
        color: .green, strength: 2.0
        )))
hoverEntityA.components.set(hoverA)

// Create hover effect components for the two children on the left side.
var hoverB = HoverEffectComponent(
    .highlight(HoverEffectComponent.HighlightHoverEffectStyle(
        color: .yellow, strength: 2.0
        )))

var hoverBB = HoverEffectComponent(
    .highlight(HoverEffectComponent.HighlightHoverEffectStyle(
        color: .orange, strength: 2.0
        )))

// Create a `HoverEffectComponent.GroupID` instance for the children on the left side
let leftGroupId = HoverEffectComponent.GroupID()
hoverB.hoverEffect.groupID = leftGroupId
hoverBB.hoverEffect.groupID = leftGroupId
hoverEntityB.components.set(hoverB)
hoverEntityBB.components.set(hoverBB)

```

In this example, the top entity, `entityA`, doesn’t have a group identifier. However, the left side entities, `entityB` and `entityBB`, have the same [`HoverEffectComponent.GroupID`](hovereffectcomponent/groupid.md) instance. The top entity `entityA` and its right child `entityC` both glow when a person activates either one in the right side hierarchical branch. However, the left child `entityB` and its descendent `entityBB` glow only when a person activates either one of them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hovereffectcomponent/hovereffect-swift.struct/groupid)*