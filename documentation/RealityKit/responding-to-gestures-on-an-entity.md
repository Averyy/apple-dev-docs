# Responding to gestures on an entity

**Framework**: RealityKit

Respond to gestures performed on RealityKit entities using input target and collision components.

**Availability**:
- visionOS 2.0+
- Xcode 16.3+

#### Overview

Your app responds to [`RealityView`](RealityView.md) gesture events received from SwiftUI by adding an [`InputTargetComponent`](InputTargetComponent.md) and a [`CollisionComponent`](CollisionComponent.md) to your entities. Add a [`HoverEffectComponent`](HoverEffectComponent.md) to the entity so it highlights as the gaze intersects the collision shape. The input target component marks the entity as participating in the event system. The system uses the collision component to test if the gaze vector intersects the entity. With both components attached, entities receive events. With the hover effect attached the entity visually appears ready to receive events.

##### Attach Components to an Entity to Process Events

The sample defines the `ActiveComponent`, which keeps track of the `active` state of the entity.

```swift
public class ActiveComponent: Component {
    public var active: Bool = false
}
```

This sample has one entity, a cube that’s `0.1` units in each direction. The sample creates the entity then adds the components.

```swift
var cube = ModelEntity(mesh: .generateBox(size: 0.1),
                       materials: [SimpleMaterial(color: .orange, isMetallic: false)])

cube.components.set(InputTargetComponent())
cube.components.set(CollisionComponent(shapes: [ShapeResource.generateBox(size: SIMD3<Float>(0.1, 0.1, 0.1))]))
cube.components.set(HoverEffectComponent())
cube.components.set(ActiveComponent())
```

The sample has a [`SpatialEventGesture`](https://developer.apple.com/documentation/SwiftUI/SpatialEventGesture) attached to the `RealityView`. As the person interacting with the app looks around and pinches, the system uses the input target component and the collision component to determine intent. The system considers all entities in the scene because the sample calls [`targetedToAnyEntity()`](https://developer.apple.com/documentation/SwiftUI/Gesture/targetedToAnyEntity()). When the person pinches on the cube the system invokes the gesture’s `onEnded` block, which toggles the `active` flag.

```swift
.gesture(SpatialEventGesture()
    .targetedToAnyEntity()
    .onEnded { value in
        value.entity.components[ActiveComponent.self]?.active.toggle()
    })
```

The `attachments:` block creates an attachment with the name of the `cube` entity.

```swift
attachments: {
    Attachment(id: cube.id) {
        Text("\(cube.name)")
            .padding()
            .glassBackgroundEffect(in: RoundedRectangle(cornerRadius: 5.0))
            .tag(cube.id)
    }
}
```

The attachment’s `id` is set to the ID of the `cube` so that it’s easy to find in the `update:` block of `RealityView`. In the `update:` block, the sample finds the `ActiveComponent` from the cube and then finds the attachment using the ID of the cube. If the active value is `true` the code adds a [`BillboardComponent`](BillboardComponent.md) to the attachment. The system ensures entities with a `BillboardComponent` always face the person. The `RealityView` `update` block adds the attachment entity as a subentity of the cube and sets the position to `[0.0, 0.1, 0.0]`.

```swift
update: { content, attachments in
    guard let component = cube.components[ActiveComponent.self] else { return }
    guard let attachmentEntity = attachments.entity(for: cube.id) else { return }
    if component.active {
        attachmentEntity.components.set(BillboardComponent())
        cube.addChild(attachmentEntity)
        attachmentEntity.setPosition(SIMD3<Float>(0.0, 0.1, 0.0),
                                     relativeTo: cube)
    } else {
        cube.removeChild(attachmentEntity)
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/responding-to-gestures-on-an-entity)*