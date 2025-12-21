# allowsRotation

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the physics body is affected by angular forces and impulses applied to it.

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
var allowsRotation: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). This property is ignored on edge-based bodies, which are unaffected by forces in the system.

## See Also

- [var affectedByGravity: Bool](skphysicsbody/affectedbygravity.md)
  A Boolean value that indicates whether this physics body is affected by the physics world’s gravity.
- [var isDynamic: Bool](skphysicsbody/isdynamic.md)
  A Boolean value that indicates whether the physics body is moved by the physics simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/allowsrotation)*