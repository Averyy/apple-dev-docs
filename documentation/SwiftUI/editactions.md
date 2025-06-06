# EditActions

**Framework**: SwiftUI  
**Kind**: struct

A set of edit actions on a collection of data that a view can offer to a user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct EditActions<Data>
```

## Topics

### Getting edit operations
- [static var all: EditActions<Data>](editactions/all-45m4m.md)
  All the edit actions available on this collection.
- [static var all: EditActions<Data>](editactions/all-4dctm.md)
  All the edit actions available on this collection.
- [static var all: EditActions<Data>](editactions/all-4uyun.md)
  All the edit actions available on this collection.
- [static var all: EditActions<Data>](editactions/all-6ryvk.md)
  All the edit actions available on this collection.
- [static var delete: EditActions<Data>](editactions/delete.md)
  An edit action that allows the user to delete one or more elements of a collection.
- [static var move: EditActions<Data>](editactions/move.md)
  An edit action that allows the user to move elements of a collection.
### Creating an edit operation
- [init(rawValue: Int)](editactions/init(rawvalue:).md)
  Creates a new set from a raw value.
- [let rawValue: Int](editactions/rawvalue.md)
  The raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func moveDisabled(Bool) -> some View](view/movedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is movable.
- [func deleteDisabled(Bool) -> some View](view/deletedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is deletable.
- [var editMode: Binding<EditMode>?](environmentvalues/editmode.md)
  An indication of whether the user can edit the contents of a view associated with this environment.
- [enum EditMode](editmode.md)
  A mode that indicates whether the user can edit a view’s content.
- [struct EditableCollectionContent](editablecollectioncontent.md)
  An opaque wrapper view that adds editing capabilities to a row in a list.
- [struct IndexedIdentifierCollection](indexedidentifiercollection.md)
  A collection wrapper that iterates over the indices and identifiers of a collection together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/editactions)*