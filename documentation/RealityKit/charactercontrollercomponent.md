# CharacterControllerComponent

**Framework**: Realitykit  
**Kind**: struct

A component that manages character movement.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct CharacterControllerComponent
```

#### Overview

To use a character controller, add a `CharacterControllerComponent` to your entity to make it a character entity. Use [`moveCharacter(by:deltaTime:relativeTo:collisionHandler:)`](entity/movecharacter(by:deltatime:relativeto:collisionhandler:).md) to move your character and respond to collisions, or [`teleportCharacter(to:relativeTo:)`](entity/teleportcharacter(to:relativeto:).md) to place your character instantaneously in 3D space.

> **Note**: [`PhysicsBodyComponent`](physicsbodycomponent.md) and [`CollisionComponent`](collisioncomponent.md) are incompatible with `CharacterControllerComponent`, and RealityKit deactivates them if you add them to the same entity.

#### Handle Collision

Character entities are capsular, and you can specify their height and radius in the component’s initializer. A character’s capsule shape aligns with its [`upVector`](charactercontrollercomponent/upvector.md) so that the top and bottom of the capsule pass through that direction vector.

Although characters don’t have a `CollisionComponent`, they can still interact with colliders. The collision handler in `moveCharacter(by:deltaTime:relativeTo:collisionHandler:)` allows you to respond to collisions with solid colliders in your scene.

```swift
entity.moveCharacter(by: velocity * deltaTime, deltaTime: deltaTime, relativeTo: nil) {
    event in
    // Your character collided with `event.hitEntity`.
}
```

To handle collisions with colliders that have a [`mode`](collisioncomponent/mode-swift.property.md) of [`CollisionComponent.Mode.trigger`](collisioncomponent/mode-swift.enum/trigger.md), subscribe to the [`CollisionEvents.Began`](collisionevents/began.md) event for your [`RealityView`](realityview.md). This event doesn’t occur for solid collisions with your character, but RealityKit invokes it when your character enters a trigger. This is useful for collecting coins, claiming checkpoints, activating enemy behavior when your character enters an area, and many other interactions within games.

#### Update Your Character

A common use case for `CharacterControllerComponent` is to control a character in a video game. Video games have update loops where characters and game logic update once each frame, allowing them to respond to player input in real time. `CharacterControllerComponent` works well in such a setup.

To move your character in response to player input, subscribe to [`PhysicsSimulationEvents.WillSimulate`](physicssimulationevents/willsimulate.md) on [`RealityViewContent`](realityviewcontent.md) for your scene. The event object contains information like the time delta since the last update, and you can treat this callback as the update loop for your game.

> **Note**: You can also use [`SceneEvents.Update`](sceneevents/update.md) to run code for each frame, but avoid using it to control physics-based motion in your scene.

Read the values from [`CharacterControllerStateComponent`](charactercontrollerstatecomponent.md) to accumulate forces (such as gravity) and to check whether the character is on the ground. RealityKit calculates [`isOnGround`](charactercontrollerstatecomponent/isonground.md) and  [`velocity`](charactercontrollerstatecomponent/velocity.md) only after you call `moveCharacter(by:deltaTime:relativeTo:collisionHandler:)`, so it’s a good idea to call this function at each update.

```swift
let gravity: SIMD3<Float> = [0, -50, 0]
let jumpSpeed: Float = 10
content.subscribe(to: PhysicsSimulationEvents.WillSimulate.self, on: playerEntity) {
    event in
    let deltaTime: Float = event.deltaTime
    var velocity: SIMD3<Float> = .zero
    var isOnGround: Bool = false

    // RealityKit automatically adds `CharacterControllerStateComponent` after moving the character for the first time.
    if let ccState = playerEntity.components[CharacterControllerStateComponent.self] {
        velocity = ccState.velocity
        isOnGround = ccState.isOnGround
    }

    if !isOnGround {
        // Gravity is a force, so you need to accumulate it for each frame.
        velocity += gravity * deltaTime
    } else if myPlayerInput.jump {
        // Set the character's velocity directly to launch it in the air when the player jumps.
        velocity.y = jumpSpeed
    }

    playerEntity.moveCharacter(by: velocity * deltaTime, deltaTime: deltaTime, relativeTo: nil) {
        event in
        print("playerEntity collided with \(event.hitEntity.name)")
    }
}
```

The following video shows a character entity jumping in response to player input:

## Topics

### Creating a character controller component
- [init()](charactercontrollercomponent/init.md)
  Creates a character controller component using default values.
- [init(radius: Float, height: Float, skinWidth: Float, slopeLimit: Float, stepLimit: Float, upVector: SIMD3<Float>, collisionFilter: CollisionFilter)](charactercontrollercomponent/init(radius:height:skinwidth:slopelimit:steplimit:upvector:collisionfilter:).md)
  Creates a character controller component using specified values.
### Configuring a character
- [var height: Float](charactercontrollercomponent/height.md)
  The capsule height.
- [var radius: Float](charactercontrollercomponent/radius.md)
  The capsule radius.
- [var skinWidth: Float](charactercontrollercomponent/skinwidth.md)
  An added tolerance around the character capsule.
- [var slopeLimit: Float](charactercontrollercomponent/slopelimit.md)
  The slope limit expressed as a limit angle in radians.
- [var stepLimit: Float](charactercontrollercomponent/steplimit.md)
  The maximum obstacle height that the controller can move over.
- [var upVector: SIMD3<Float>](charactercontrollercomponent/upvector.md)
  The y-axis direction relative to the physics origin.
### Managing character collisions
- [var collisionFilter: CollisionFilter](charactercontrollercomponent/collisionfilter.md)
  The character’s collision filter.
### Reading default values
- [static let defaultHeight: Float](charactercontrollercomponent/defaultheight.md)
  The capsule height value RealityKit applies when you use the default initializer.
- [static let defaultRadius: Float](charactercontrollercomponent/defaultradius.md)
  The capsule default radius RealityKit applies when you use the default initializer.
- [static let defaultSkinWidth: Float](charactercontrollercomponent/defaultskinwidth.md)
  The skin width value RealityKit applies when you use the default initializer.
- [static let defaultSlopeLimit: Float](charactercontrollercomponent/defaultslopelimit.md)
  The slope limit value RealityKit applies when you use the default initializer.
- [static let defaultStepLimit: Float](charactercontrollercomponent/defaultsteplimit.md)
  The step limit value RealityKit applies when you use the default initializer.
- [static let defaultUpVector: SIMD3<Float>](charactercontrollercomponent/defaultupvector.md)
  The default up vector RealityKit applies when you use the default initializer.
### Animating a character
- [struct JointTransforms](jointtransforms.md)
  A set of animatable transform values for joints that collectively represent a single skeletal pose.
### Handling collisions
- [CharacterControllerComponent.Collision](charactercontrollercomponent/collision.md)
  A container that holds collision state for the character controller.
- [CharacterControllerComponent.CollisionFlags](charactercontrollercomponent/collisionflags.md)
  An option set that specifies which parts of the character capsule have collided with other objects.
### Default Implementations
- [Component Implementations](charactercontrollercomponent/component-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [CharacterControllerComponent.Collision](charactercontrollercomponent/collision.md)
  A container that holds collision state for the character controller.
- [CharacterControllerComponent.CollisionFlags](charactercontrollercomponent/collisionflags.md)
  An option set that specifies which parts of the character capsule have collided with other objects.
- [struct CharacterControllerStateComponent](charactercontrollerstatecomponent.md)
  A component that represents the state of a character controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RealityKit/charactercontrollercomponent)*