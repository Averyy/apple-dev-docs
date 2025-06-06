# OrbitAction

**Framework**: RealityKit

An action that orbits a set of prims around another.

#### Overview

This action sends the list of prims defined by [`affectedObjects`](affectedobjects.md) into orbit at a fixed distance around its [`center`](center.md) prim, on a plane perpendicular to the axis of rotation. The runtime caculates the fixed distance as a straight line between the respective origins of the [`affectedObjects`](affectedobjects.md) and the [`center`](center.md).

##### Declaration

```other
class Preliminary_Action "OrbitAction"
```

## Topics

### Properties
- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [center](center.md)
  A prim around which the affected objects orbit.
- [duration](duration.md)
  The amount of time that the objects face the camera.
- [revolutions](revolutions.md)
  The number of rotations to complete.
- [axis](axis.md)
  A vector that describes the axis of rotation.
- [alignToPath](aligntopath.md)
  An option that controls the prim’s orientation as it revolves.

## See Also

- [Preliminary_Action](preliminary-action.md)
  A specific task that a trigger performs.
- [AudioAction](audioaction.md)
  An action that plays audio.
- [ChangeSceneAction](changesceneaction.md)
  An action that transitions from one scene to another.
- [EmphasizeAction](emphasizeaction.md)
  An action that performs an animation to call attention to an object.
- [GroupAction](groupaction.md)
  An action that runs a list of other actions.
- [ImpulseAction](impulseaction.md)
  An action that adds velocity to an prim.
- [LookAtCameraAction](lookatcameraaction.md)
  An action that reorients an object to face the user’s camera.
- [SpinAction](spinaction.md)
  An action that spins a prim.
- [StartAnimationAction](startanimationaction.md)
  An action that plays an asset’s animation.
- [TransformAction](transformaction.md)
  An action that animates from one transform to another.
- [TransformAnimationAction](transformanimationaction.md)
  An action that plays a transform animation.
- [VisibilityAction](visibilityaction.md)
  An action that displays or hides objects over a period of time.
- [WaitAction](waitaction.md)
  An action that performs a delay.
- [NotificationAction](notificationaction.md)
  An action that sends a custom notification to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitaction)*