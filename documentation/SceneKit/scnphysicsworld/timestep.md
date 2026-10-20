# timeStep

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The time interval between updates to the physics simulation.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var timeStep: TimeInterval { get set }
```

```objc
@property (nonatomic) NSTimeInterval timeStep;
```

#### Discussion

SceneKit processes the physics simulation and updates the state of all physics bodies once per the time interval specified by this property. The default value is 1/60 second (a rate of 60 Hz).

A faster simulation rate provides more accuracy in simulation results—such as collisions between fast-moving objects—but at a higher cost in CPU time (which may in turn slow down your app’s rendering frame rate). Typically, you should set this property to match your target rendering frame rate (as defined by the [`preferredFramesPerSecond`](../scnview/preferredframespersecond.md) property of the [`SCNView`](../scnview.md) object rendering your scene).

## See Also

### Managing the Physics Simulation
- [var gravity: SCNVector3](./gravity.md)
  A vector that specifies the gravitational acceleration applied to physics bodies in the physics world.
- [var speed: CGFloat](./speed.md)
  The rate at which the simulation executes.
- [func updateCollisionPairs()](./updatecollisionpairs%28%29.md)
  Forces the physics engine to reevaluate possible collisions between physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/timestep)*