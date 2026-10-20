# UICollisionBehavior.Mode

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The types of edges that participate in collisions for a collision behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
struct Mode
```

```c
enum UICollisionBehaviorMode : NSUInteger;
```

## Topics

### Constants
- [static var items: UICollisionBehavior.Mode](./mode/items.md)
  Specifies that the dynamic items, associated with the collision behavior, collide only with each other and not with specified collision boundaries.
- [static var boundaries: UICollisionBehavior.Mode](./mode/boundaries.md)
  Specifies that the dynamic items, associated with the collision behavior, collide only with specified collision boundaries and don’t collide with each other.
- [static var everything: UICollisionBehavior.Mode](./mode/everything.md)
  Specifies that the dynamic items, associated with the collision behavior, collide with each other *and* with specified collision boundaries.
### Initializers
- [init(rawValue: UInt)](./mode/init%28rawvalue%29.md)
  Creates a collision behavior mode structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/mode)*