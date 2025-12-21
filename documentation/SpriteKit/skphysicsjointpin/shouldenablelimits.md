# shouldEnableLimits

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the pin joint’s rotation is limited to a specific range of values.

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
var shouldEnableLimits: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false). If [`true`](https://developer.apple.com/documentation/Swift/true), the [`lowerAngleLimit`](skphysicsjointpin/loweranglelimit.md) and [`upperAngleLimit`](skphysicsjointpin/upperanglelimit.md) properties are used to limit the angle of the pin joint.

## See Also

- [var rotationSpeed: CGFloat](skphysicsjointpin/rotationspeed.md)
  The speed, in radians per second, at which the physics bodies are driven around the pin joint.
- [var lowerAngleLimit: CGFloat](skphysicsjointpin/loweranglelimit.md)
  The smallest angle allowed for the pin joint, in radians.
- [var upperAngleLimit: CGFloat](skphysicsjointpin/upperanglelimit.md)
  The largest angle allowed for the pin joint, in radians.
- [var frictionTorque: CGFloat](skphysicsjointpin/frictiontorque.md)
  The resistance applied by the pin joint to spinning around the anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/shouldenablelimits)*