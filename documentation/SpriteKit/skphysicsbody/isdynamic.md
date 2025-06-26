# isDynamic

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the physics body is moved by the physics simulation.

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
var isDynamic: Bool { get set }
```

## Mentions

- [Getting Started with Spring Joints](getting-started-with-spring-joints.md)
- [Getting Started with Physics Bodies](getting-started-with-physics-bodies.md)

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true). If the value is [`false`](https://developer.apple.com/documentation/swift/false), the physics body ignores all forces and impulses applied to it. This property is ignored on edge-based bodies; they are automatically static.

## See Also

- [var affectedByGravity: Bool](skphysicsbody/affectedbygravity.md)
  A Boolean value that indicates whether this physics body is affected by the physics world’s gravity.
- [var allowsRotation: Bool](skphysicsbody/allowsrotation.md)
  A Boolean value that indicates whether the physics body is affected by angular forces and impulses applied to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/isdynamic)*