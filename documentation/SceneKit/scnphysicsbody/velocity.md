# velocity

**Framework**: SceneKit  
**Kind**: property

A vector describing both the current speed (in meters per second) and direction of motion of the physics body.

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
var velocity: SCNVector3 { get set }
```

#### Discussion

SceneKit’s physics simulation determines the velocity (and corresponding change in position) of each dynamic physics body in the scene. You can also set a body’s velocity directly to set the physics simulation in motion or influence its behavior.

The effect of reading or setting this property’s value changes based on the current context:

- When invoked within a rendering loop method (any of the methods in the [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md) protocol), or from any other code invoked from within such a method, reading the property returns the current result of the physics simulation, and setting the property immediately applies the change.
- When invoked at any other time, reading the property returns the last value set for the property, and setting the property does not take effect until the next pass through the rendering loop.

## See Also

- [var angularVelocity: SCNVector4](scnphysicsbody/angularvelocity.md)
  A vector describing both the current rotation axis and rotational speed (in radians per second) of the physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/velocity)*