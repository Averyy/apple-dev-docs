# frictionTorque

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The resistance applied by the pin joint to spinning around the anchor point.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var frictionTorque: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat frictionTorque;
```

## Mentions

- [Pinning and Rotating Physics Bodies](../pinning-and-rotating-physics-bodies.md)

#### Discussion

The range of values is from `0.0` to `1.0`. The default value is `0.0`. If a value greater than the default is specified, friction is applied to reduce the object’s angular velocity around the pin.

## See Also

### Configuring a Pin Joint
- [var rotationSpeed: CGFloat](./rotationspeed.md)
  The speed, in radians per second, at which the physics bodies are driven around the pin joint.
- [var shouldEnableLimits: Bool](./shouldenablelimits.md)
  A Boolean value that indicates whether the pin joint’s rotation is limited to a specific range of values.
- [var lowerAngleLimit: CGFloat](./loweranglelimit.md)
  The smallest angle allowed for the pin joint, in radians.
- [var upperAngleLimit: CGFloat](./upperanglelimit.md)
  The largest angle allowed for the pin joint, in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/frictiontorque)*