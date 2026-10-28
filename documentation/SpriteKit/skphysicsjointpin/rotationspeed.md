# rotationSpeed

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The speed, in radians per second, at which the physics bodies are driven around the pin joint.

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
var rotationSpeed: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat rotationSpeed;
```

## Discussion

The [`frictionTorque`](./frictiontorque.md) property limits the maximum amount of torque that can be applied to the physics bodies.

## See Also

### Configuring a Pin Joint
- [var shouldEnableLimits: Bool](./shouldenablelimits.md)
  A Boolean value that indicates whether the pin joint’s rotation is limited to a specific range of values.
- [var lowerAngleLimit: CGFloat](./loweranglelimit.md)
  The smallest angle allowed for the pin joint, in radians.
- [var upperAngleLimit: CGFloat](./upperanglelimit.md)
  The largest angle allowed for the pin joint, in radians.
- [var frictionTorque: CGFloat](./frictiontorque.md)
  The resistance applied by the pin joint to spinning around the anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/rotationspeed)*