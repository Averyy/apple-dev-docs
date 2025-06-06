# NSCursor.FrameResizeDirection.Set

**Framework**: AppKit  
**Kind**: struct

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
- [init(NSCursor.FrameResizeDirection)](nscursor/frameresizedirection/set/init(_:).md)
  Creates a set of directions containing only the specified direction.
### Instance Methods
- [func contains(NSCursor.FrameResizeDirection) -> Bool](nscursor/frameresizedirection/set/contains(_:).md)
- [func insert(NSCursor.FrameResizeDirection) -> (inserted: Bool, memberAfterInsert: NSCursor.FrameResizeDirection)](nscursor/frameresizedirection/set/insert(_:).md)
- [func remove(NSCursor.FrameResizeDirection) -> NSCursor.FrameResizeDirection?](nscursor/frameresizedirection/set/remove(_:).md)
- [func update(with: NSCursor.FrameResizeDirection) -> NSCursor.FrameResizeDirection?](nscursor/frameresizedirection/set/update(with:).md)
### Type Properties
- [static let all: NSCursor.FrameResizeDirection.Set](nscursor/frameresizedirection/set/all.md)
  A set containing the inward and outward resizing directions.
- [static let inward: NSCursor.FrameResizeDirection.Set](nscursor/frameresizedirection/set/inward.md)
  A set containing only the inward resize direction.
- [static let outward: NSCursor.FrameResizeDirection.Set](nscursor/frameresizedirection/set/outward.md)
  A set containing only the outward resize direction.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/frameresizedirection/set)*