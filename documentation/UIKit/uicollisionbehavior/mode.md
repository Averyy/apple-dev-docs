# UICollisionBehavior.Mode

**Framework**: UIKit  
**Kind**: struct

The types of edges that participate in collisions for a collision behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct Mode
```

## Topics

### Constants
- [static var items: UICollisionBehavior.Mode](uicollisionbehavior/mode/items.md)
  Specifies that the dynamic items, associated with the collision behavior, collide only with each other and not with specified collision boundaries.
- [static var boundaries: UICollisionBehavior.Mode](uicollisionbehavior/mode/boundaries.md)
  Specifies that the dynamic items, associated with the collision behavior, collide only with specified collision boundaries and don’t collide with each other.
- [static var everything: UICollisionBehavior.Mode](uicollisionbehavior/mode/everything.md)
  Specifies that the dynamic items, associated with the collision behavior, collide with each other  with specified collision boundaries.
### Initializers
- [init(rawValue: UInt)](uicollisionbehavior/mode/init(rawvalue:).md)
  Creates a collision behavior mode structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/mode)*