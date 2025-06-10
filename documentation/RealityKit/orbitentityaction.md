# OrbitEntityAction

**Framework**: RealityKit  
**Kind**: struct

An action which animates the transform of an entity to revolve around a specified pivot entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct OrbitEntityAction
```

#### Overview

This action moves an entity in a circular path by gradually adjusting its local transform. The animation starts from the entity’s initial transform, and rotates around the pivot entity. The [`orbitalAxis`](orbitentityaction/orbitalaxis.md) specifies which cartesian axis to rotate around in world space.. The axis is resolved when the action starts to produce an axis of rotation around the pivot entity. The full orbit completes after the action has ended.

The example below creates an animation that orbits an entity around the x-axis two times for five seconds.

```swift
// Create an action entity resolution to the pivot entity 
// that exists in the scene.
let pivotEntity: ActionEntityResolution = .entityNamed("pivotEntity")

// Create an action that performs an orbit around the 
// specified pivot entity.
let orbitEntityAction = OrbitEntityAction(pivotEntity: pivotEntity,
                                          revolutions: 2,
                                          orbitalAxis: [0, 1, 0],
                                          isOrientedToPath: true,
                                          isAdditive: false)

// A five second animation that plays an animation causing the entity to
// orbit around the pivot.
let orbitAnimation = try AnimationResource
    .makeActionAnimation(for: orbitEntityAction,
                         duration: 5.0,
                         bindTarget: .transform)

// Play the five second orbit animation.
entity.playAnimation(orbitAnimation)
```

> **Note**: Use the [`orbitalAxis`](orbitentityaction/orbitalaxis.md) to determine whether the entity orbits clockwise or counterclockwise.

> ❗ **Important**: This action directly animates the [`BindTarget.transform`](bindtarget/transform.md) on the bound entity. Ensure a correct bind target is supplied when creating the animation.

> ❗ **Important**: For a successful orbit, ensure the translational offset between the target and pivot entity are not parallel to the orbit axis.

## Topics

### Initializers
- [init(pivotEntity: ActionEntityResolution, revolutions: Float, orbitalAxis: SIMD3<Float>, isOrientedToPath: Bool, isAdditive: Bool)](orbitentityaction/init(pivotentity:revolutions:orbitalaxis:isorientedtopath:isadditive:).md)
  Creates a new orbit entity action.
### Instance Properties
- [var animatedValueType: (any AnimatableData.Type)?](orbitentityaction/animatedvaluetype.md)
  The type for the value that the action modifies over time.
- [var isAdditive: Bool](orbitentityaction/isadditive.md)
  A Boolean value that indicates whether the animation system additively blends the action’s output with the base value.
- [var isOrientedToPath: Bool](orbitentityaction/isorientedtopath.md)
  A Boolean value that indicates whether the orbiting object updates its orientation during the animation to orient itself along the rotation path.
- [var orbitalAxis: SIMD3<Float>](orbitentityaction/orbitalaxis.md)
  A vector that describes the axis of rotation (in world space).
- [var pivotEntity: ActionEntityResolution](orbitentityaction/pivotentity.md)
  The entity that the target entity orbits around.
- [var revolutions: Float](orbitentityaction/revolutions.md)
  The number of rotations to complete before stopping.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [EntityAction](entityaction.md)

## See Also

- [struct BillboardAction](billboardaction.md)
  An action that animates the blend factor of an entity’s billboard component.
- [struct EmphasizeAction](emphasizeaction.md)
  An action that performs an animation to call attention to an entity.
- [struct FromToByAction](fromtobyaction.md)
  An action that starts, stops, or increments by a specific value.
- [struct ImpulseAction](impulseaction.md)
  An action that applies an impulse to the physics body at its center of mass when played as an animation.
- [struct PlayAnimationAction](playanimationaction.md)
  An action that plays an animation on the given target entity with a range of playback options.
- [struct PlayAudioAction](playaudioaction.md)
  An action which plays an audio resource on the given target entity.
- [struct SetEntityEnabledAction](setentityenabledaction.md)
  An action that enables or disables the targeted entity and its descendants when played as an animation.
- [struct SpinAction](spinaction.md)
  An action which animates the transform of an entity to rotate around a specified local axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitentityaction)*