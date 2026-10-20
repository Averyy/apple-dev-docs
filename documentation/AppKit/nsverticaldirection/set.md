# NSVerticalDirection.Set

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

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
- [init(NSVerticalDirection)](./set/init%28_%29.md)
  Creates a set of directions containing only the specified direction.
### Instance Methods
- [func contains(NSVerticalDirection) -> Bool](./set/contains%28_%29.md)
- [func insert(NSVerticalDirection) -> (inserted: Bool, memberAfterInsert: NSVerticalDirection)](./set/insert%28_%29.md)
- [func remove(NSVerticalDirection) -> NSVerticalDirection?](./set/remove%28_%29.md)
- [func update(with: NSVerticalDirection) -> NSVerticalDirection?](./set/update%28with%29.md)
### Type Properties
- [static let all: NSVerticalDirection.Set](./set/all.md)
  A set containing all vertical directions (up and down)
- [static let down: NSVerticalDirection.Set](./set/down.md)
  A set containing only the down direction.
- [static let up: NSVerticalDirection.Set](./set/up.md)
  A set containing only the up direction.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsverticaldirection/set)*