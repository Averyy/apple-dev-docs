# gravity

**Framework**: SpriteKit  
**Kind**: property

A vector that specifies the gravitational acceleration applied to physics bodies in the physics world.

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
var gravity: CGVector { get set }
```

#### Discussion

The components of this property are measured in meters per second. The default value is `(0.0,-9.8)`, which represent’s Earth’s gravity.

## See Also

- [var speed: CGFloat](skphysicsworld/speed.md)
  The rate at which the simulation executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsworld/gravity)*