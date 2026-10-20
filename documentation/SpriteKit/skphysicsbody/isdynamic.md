# isDynamic

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the physics body is moved by the physics simulation.

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
var isDynamic: Bool { get set }
```

```objc
@property (nonatomic, getter=isDynamic) BOOL dynamic;
```

## Mentions

- [Getting Started with Physics Bodies](../getting-started-with-physics-bodies.md)
- [Getting Started with Spring Joints](../getting-started-with-spring-joints.md)

#### Discussion

The default value is [`true`](../../Swift/true.md). If the value is [`false`](../../Swift/false.md), the physics body ignores all forces and impulses applied to it. This property is ignored on edge-based bodies; they are automatically static.

## See Also

### Defining How Forces Affect a Physics Body
- [var affectedByGravity: Bool](./affectedbygravity.md)
  A Boolean value that indicates whether this physics body is affected by the physics world’s gravity.
- [var allowsRotation: Bool](./allowsrotation.md)
  A Boolean value that indicates whether the physics body is affected by angular forces and impulses applied to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/isdynamic)*