# boundaries

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Specifies that the dynamic items, associated with the collision behavior, collide only with specified collision boundaries and don’t collide with each other.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var boundaries: UICollisionBehavior.Mode { get }
```

```c
UICollisionBehaviorModeBoundaries
```

## See Also

### Constants
- [static var items: UICollisionBehavior.Mode](./items.md)
  Specifies that the dynamic items, associated with the collision behavior, collide only with each other and not with specified collision boundaries.
- [static var everything: UICollisionBehavior.Mode](./everything.md)
  Specifies that the dynamic items, associated with the collision behavior, collide with each other *and* with specified collision boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/mode/boundaries)*