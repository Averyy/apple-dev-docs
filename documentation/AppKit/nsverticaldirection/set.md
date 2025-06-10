# NSVerticalDirection.Set

**Framework**: AppKit  
**Kind**: struct

An efficient set of vertical directions.

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
- [init(NSVerticalDirection)](nsverticaldirection/set/init(_:).md)
  Creates a set of directions containing only the specified direction.
### Instance Methods
- [func contains(NSVerticalDirection) -> Bool](nsverticaldirection/set/contains(_:).md)
- [func insert(NSVerticalDirection) -> (inserted: Bool, memberAfterInsert: NSVerticalDirection)](nsverticaldirection/set/insert(_:).md)
- [func remove(NSVerticalDirection) -> NSVerticalDirection?](nsverticaldirection/set/remove(_:).md)
- [func update(with: NSVerticalDirection) -> NSVerticalDirection?](nsverticaldirection/set/update(with:).md)
### Type Properties
- [static let all: NSVerticalDirection.Set](nsverticaldirection/set/all.md)
  A set containing all vertical directions (up and down)
- [static let down: NSVerticalDirection.Set](nsverticaldirection/set/down.md)
  A set containing only the down direction.
- [static let up: NSVerticalDirection.Set](nsverticaldirection/set/up.md)
  A set containing only the up direction.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsverticaldirection/set)*