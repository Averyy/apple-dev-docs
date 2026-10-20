# shouldEnableLimits

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the pin joint’s rotation is limited to a specific range of values.

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
var shouldEnableLimits: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldEnableLimits;
```

#### Discussion

The default value is [`false`](../../Swift/false.md). If [`true`](../../Swift/true.md), the [`lowerAngleLimit`](./loweranglelimit.md) and [`upperAngleLimit`](./upperanglelimit.md) properties are used to limit the angle of the pin joint.

## See Also

### Configuring a Pin Joint
- [var rotationSpeed: CGFloat](./rotationspeed.md)
  The speed, in radians per second, at which the physics bodies are driven around the pin joint.
- [var lowerAngleLimit: CGFloat](./loweranglelimit.md)
  The smallest angle allowed for the pin joint, in radians.
- [var upperAngleLimit: CGFloat](./upperanglelimit.md)
  The largest angle allowed for the pin joint, in radians.
- [var frictionTorque: CGFloat](./frictiontorque.md)
  The resistance applied by the pin joint to spinning around the anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/shouldenablelimits)*