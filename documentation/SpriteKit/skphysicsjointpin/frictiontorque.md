# frictionTorque

**Framework**: SpriteKit  
**Kind**: property

The resistance applied by the pin joint to spinning around the anchor point.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var frictionTorque: CGFloat { get set }
```

## Mentions

- [Pinning and Rotating Physics Bodies](pinning-and-rotating-physics-bodies.md)

#### Discussion

The range of values is from `0.0` to `1.0`. The default value is `0.0`. If a value greater than the default is specified, friction is applied to reduce the object’s angular velocity around the pin.

## See Also

- [var rotationSpeed: CGFloat](skphysicsjointpin/rotationspeed.md)
  The speed, in radians per second, at which the physics bodies are driven around the pin joint.
- [var shouldEnableLimits: Bool](skphysicsjointpin/shouldenablelimits.md)
  A Boolean value that indicates whether the pin joint’s rotation is limited to a specific range of values.
- [var lowerAngleLimit: CGFloat](skphysicsjointpin/loweranglelimit.md)
  The smallest angle allowed for the pin joint, in radians.
- [var upperAngleLimit: CGFloat](skphysicsjointpin/upperanglelimit.md)
  The largest angle allowed for the pin joint, in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/frictiontorque)*