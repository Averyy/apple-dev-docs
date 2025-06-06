# StartAnimationAction

**Framework**: RealityKit

An action that plays an asset’s animation.

#### Overview

If the asset defines an animation, this action runs it on every prim in [`affectedObjects`](affectedobjects.md).

##### Declaration

```other
class Preliminary_Action "StartAnimationAction"
```

## Topics

### Properties
- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [start](start.md)
  The moment to begin an animation.
- [duration](duration.md)
  The amount of time that the objects face the camera.
- [reversed](reversed.md)
  A Boolean value that determines the clip playback direction.
- [animationSpeed](animationspeed.md)
  A factor to apply to the animation speed.
- [reverses](reverses.md)
  A Boolean value that indicates whether the animation plays from beginning to end, then again from end to beginning.

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
- [OrbitAction](orbitaction.md)
  An action that orbits a set of prims around another.
- [SpinAction](spinaction.md)
  An action that spins a prim.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/startanimationaction)*