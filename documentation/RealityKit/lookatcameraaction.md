# LookAtCameraAction

**Framework**: RealityKit

An action that reorients an object to face the user’s camera.

#### Overview

By default, the [`duration`](duration.md) specifies the amount of time the prim looks at the camera. To look at the camera indefinitely, place this action in a `GroupAction` that repeats infinitely.

##### Declaration

```other
class Preliminary_Action "LookAtCameraAction"
```

## Topics

### Properties
- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [duration](duration.md)
  The amount of time that the objects face the camera.
- [front](front.md)
  A vector that’s perpendicular to, and points outward from, the object’s face.
- [upVector](upvector.md)
  A vector around which the runtime rotates the object.

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
- [OrbitAction](orbitaction.md)
  An action that orbits a set of prims around another.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lookatcameraaction)*