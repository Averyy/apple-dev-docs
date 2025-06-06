# Preliminary_Action

**Framework**: RealityKit

A specific task that a trigger performs.

#### Overview

Because it inherits `Typed`, this schema declares a `Preliminary_Action` as a type of prim. For more information about typed schemas, see USD Specification > [`Typed`](https://developer.apple.comhttp://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-TypedSchema).

When a behavior executes an action, the behavior modifies the state of the scene dynamically. For example, an action might start an animation, change the location of a prim, or start playing audio.

##### Declaration

```swift
class "Preliminary_Action" (
    inherits = </Typed>
)
```

##### Define an Action That Slides a Cube

The following example shows an action prim called `PushCube` that affects an impulse feature.

```swift
#usda 1.0

def Cube "Cube" {}

def Preliminary_Action "PushCube" {    
    uniform token info:id = "Impulse"
    rel affectedObjects = [ </Cube> ]
    uniform vector3d velocity = (1.0, 0.0, 0.0)
}
```

## Topics

### Properties
- [info:id](info-id.md)
  The action’s unique identifier.
- [multiplePerformOperation](multipleperformoperation.md)
  An option that indicates how an action handles an additional invocation while running.

## See Also

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
- [VisibilityAction](visibilityaction.md)
  An action that displays or hides objects over a period of time.
- [WaitAction](waitaction.md)
  An action that performs a delay.
- [NotificationAction](notificationaction.md)
  An action that sends a custom notification to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/preliminary-action)*