# upperAngleLimit

**Framework**: SpriteKit  
**Kind**: property

The largest angle allowed for the pin joint, in radians.

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
var upperAngleLimit: CGFloat { get set }
```

## Mentions

- [Pinning and Rotating Physics Bodies](pinning-and-rotating-physics-bodies.md)

#### Discussion

The default value is `0.0`.

## See Also

- [var rotationSpeed: CGFloat](skphysicsjointpin/rotationspeed.md)
  The speed, in radians per second, at which the physics bodies are driven around the pin joint.
- [var shouldEnableLimits: Bool](skphysicsjointpin/shouldenablelimits.md)
  A Boolean value that indicates whether the pin joint’s rotation is limited to a specific range of values.
- [var lowerAngleLimit: CGFloat](skphysicsjointpin/loweranglelimit.md)
  The smallest angle allowed for the pin joint, in radians.
- [var frictionTorque: CGFloat](skphysicsjointpin/frictiontorque.md)
  The resistance applied by the pin joint to spinning around the anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/upperanglelimit)*