# timeStep

**Framework**: SceneKit  
**Kind**: property

The time interval between updates to the physics simulation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var timeStep: TimeInterval { get set }
```

#### Discussion

SceneKit processes the physics simulation and updates the state of all physics bodies once per the time interval specified by this property. The default value is 1/60 second (a rate of 60 Hz).

A faster simulation rate provides more accuracy in simulation results—such as collisions between fast-moving objects—but at a higher cost in CPU time (which may in turn slow down your app’s rendering frame rate). Typically, you should set this property to match your target rendering frame rate (as defined by the [`preferredFramesPerSecond`](scnview/preferredframespersecond.md) property of the [`SCNView`](scnview.md) object rendering your scene).

## See Also

- [var gravity: SCNVector3](scnphysicsworld/gravity.md)
  A vector that specifies the gravitational acceleration applied to physics bodies in the physics world.
- [var speed: CGFloat](scnphysicsworld/speed.md)
  The rate at which the simulation executes.
- [func updateCollisionPairs()](scnphysicsworld/updatecollisionpairs.md)
  Forces the physics engine to reevaluate possible collisions between physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/timestep)*