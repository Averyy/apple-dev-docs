# DropOperation.Set

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [init(rawValue: Int)](./set/init%28rawvalue%29.md)
  Creates a set of drop operations using the provided raw value.
### Type Properties
- [static let alias: DropOperation.Set](./set/alias.md)
- [static let cancel: DropOperation.Set](./set/cancel.md)
  Cancel the operation.
- [static let copy: DropOperation.Set](./set/copy.md)
  Copy the data to the modified view.
- [static let delete: DropOperation.Set](./set/delete.md)
  Delete the data.
- [static let forbidden: DropOperation.Set](./set/forbidden.md)
  The operation is forbidden.
- [static let move: DropOperation.Set](./set/move.md)
  Move the data represented by the drag items instead of copying it.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropoperation/set)*