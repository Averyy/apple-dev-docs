# DropOperation.Set

**Framework**: SwiftUI  
**Kind**: struct

A set of drop operations, corresponding to matching cases in `DropOperation`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Set
```

## Topics

### Initializers
- [init(rawValue: Int)](dropoperation/set/init(rawvalue:).md)
  Creates a set of drop operations using the provided raw value.
### Type Properties
- [static let alias: DropOperation.Set](dropoperation/set/alias.md)
- [static let cancel: DropOperation.Set](dropoperation/set/cancel.md)
  Cancel the operation.
- [static let copy: DropOperation.Set](dropoperation/set/copy.md)
  Copy the data to the modified view.
- [static let delete: DropOperation.Set](dropoperation/set/delete.md)
  Delete the data.
- [static let forbidden: DropOperation.Set](dropoperation/set/forbidden.md)
  The operation is forbidden.
- [static let move: DropOperation.Set](dropoperation/set/move.md)
  Move the data represented by the drag items instead of copying it.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropoperation/set)*