# NSHorizontalDirection.Set

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

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
- [init(NSHorizontalDirection)](./set/init%28_%29.md)
  Creates a set of horizontal directions containing only the specified direction.
### Instance Methods
- [func contains(NSHorizontalDirection) -> Bool](./set/contains%28_%29.md)
- [func insert(NSHorizontalDirection) -> (inserted: Bool, memberAfterInsert: NSHorizontalDirection)](./set/insert%28_%29.md)
- [func remove(NSHorizontalDirection) -> NSHorizontalDirection?](./set/remove%28_%29.md)
- [func update(with: NSHorizontalDirection) -> NSHorizontalDirection?](./set/update%28with%29.md)
### Type Properties
- [static let all: NSHorizontalDirection.Set](./set/all.md)
  A set containing the all horizontal directions (left and right).
- [static let left: NSHorizontalDirection.Set](./set/left.md)
  A set containing only the left direction.
- [static let right: NSHorizontalDirection.Set](./set/right.md)
  A set containing only the right direction.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshorizontaldirection/set)*