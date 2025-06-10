# NSHorizontalDirection.Set

**Framework**: AppKit  
**Kind**: struct

An efficient set of horizontal directions.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
@frozen
struct Set
```

## Topics

### Initializers
- [init(NSHorizontalDirection)](nshorizontaldirection/set/init(_:).md)
  Creates a set of horizontal directions containing only the specified direction.
### Instance Methods
- [func contains(NSHorizontalDirection) -> Bool](nshorizontaldirection/set/contains(_:).md)
- [func insert(NSHorizontalDirection) -> (inserted: Bool, memberAfterInsert: NSHorizontalDirection)](nshorizontaldirection/set/insert(_:).md)
- [func remove(NSHorizontalDirection) -> NSHorizontalDirection?](nshorizontaldirection/set/remove(_:).md)
- [func update(with: NSHorizontalDirection) -> NSHorizontalDirection?](nshorizontaldirection/set/update(with:).md)
### Type Properties
- [static let all: NSHorizontalDirection.Set](nshorizontaldirection/set/all.md)
  A set containing the all horizontal directions (left and right).
- [static let left: NSHorizontalDirection.Set](nshorizontaldirection/set/left.md)
  A set containing only the left direction.
- [static let right: NSHorizontalDirection.Set](nshorizontaldirection/set/right.md)
  A set containing only the right direction.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshorizontaldirection/set)*