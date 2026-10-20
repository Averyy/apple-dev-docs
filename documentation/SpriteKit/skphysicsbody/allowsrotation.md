# allowsRotation

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the physics body is affected by angular forces and impulses applied to it.

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
var allowsRotation: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsRotation;
```

#### Discussion

The default value is [`true`](../../Swift/true.md). This property is ignored on edge-based bodies, which are unaffected by forces in the system.

## See Also

### Defining How Forces Affect a Physics Body
- [var affectedByGravity: Bool](./affectedbygravity.md)
  A Boolean value that indicates whether this physics body is affected by the physics world’s gravity.
- [var isDynamic: Bool](./isdynamic.md)
  A Boolean value that indicates whether the physics body is moved by the physics simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/allowsrotation)*