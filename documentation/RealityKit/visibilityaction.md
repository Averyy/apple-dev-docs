# VisibilityAction

**Framework**: RealityKit

An action that displays or hides objects over a period of time.

#### Overview

Use this action to display or hide a prim with a transform animation. This action is distinct from `UsdGeomImageable` because the animation doesn’t alter the `visible` property.

##### Declaration

```other
class Preliminary_Action "VisibilityAction"
```

## Topics

### Properties
- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [type](type.md)
  An option that controls the order in which the actions execute.
- [style](style.md)
  An option that implements different kinds of animation timing.
- [motionType](motiontype.md)
  An option that determines how the action displays or hides a prim.
- [easeType](easetype.md)
  An option that describes the animation’s change in pace over time.
- [moveDistance](movedistance.md)
  The distance that this action moves the target prims.

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
- [StartAnimationAction](startanimationaction.md)
  An action that plays an asset’s animation.
- [TransformAction](transformaction.md)
  An action that animates from one transform to another.
- [TransformAnimationAction](transformanimationaction.md)
  An action that plays a transform animation.
- [WaitAction](waitaction.md)
  An action that performs a delay.
- [NotificationAction](notificationaction.md)
  An action that sends a custom notification to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/visibilityaction)*