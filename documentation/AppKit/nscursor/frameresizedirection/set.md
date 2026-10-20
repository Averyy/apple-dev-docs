# NSCursor.FrameResizeDirection.Set

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

An efficient set of frame resize directions.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct Set
```

## Topics

### Initializers
- [init(NSCursor.FrameResizeDirection)](./set/init%28_%29.md)
  Creates a set of directions containing only the specified direction.
### Instance Methods
- [func contains(NSCursor.FrameResizeDirection) -> Bool](./set/contains%28_%29.md)
- [func insert(NSCursor.FrameResizeDirection) -> (inserted: Bool, memberAfterInsert: NSCursor.FrameResizeDirection)](./set/insert%28_%29.md)
- [func remove(NSCursor.FrameResizeDirection) -> NSCursor.FrameResizeDirection?](./set/remove%28_%29.md)
- [func update(with: NSCursor.FrameResizeDirection) -> NSCursor.FrameResizeDirection?](./set/update%28with%29.md)
### Type Properties
- [static let all: NSCursor.FrameResizeDirection.Set](./set/all.md)
  A set containing the inward and outward resizing directions.
- [static let inward: NSCursor.FrameResizeDirection.Set](./set/inward.md)
  A set containing only the inward resize direction.
- [static let outward: NSCursor.FrameResizeDirection.Set](./set/outward.md)
  A set containing only the outward resize direction.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../../Swift/hashable.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [SetAlgebra](../../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/frameresizedirection/set)*