# deleteDisabled(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds a condition for whether the view’s view hierarchy is deletable.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func deleteDisabled(_ isDisabled: Bool) -> some View
```

## See Also

- [func moveDisabled(Bool) -> some View](view/movedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is movable.
- [var editMode: Binding<EditMode>?](environmentvalues/editmode.md)
  An indication of whether the user can edit the contents of a view associated with this environment.
- [enum EditMode](editmode.md)
  A mode that indicates whether the user can edit a view’s content.
- [struct EditActions](editactions.md)
  A set of edit actions on a collection of data that a view can offer to a user.
- [struct EditableCollectionContent](editablecollectioncontent.md)
  An opaque wrapper view that adds editing capabilities to a row in a list.
- [struct IndexedIdentifierCollection](indexedidentifiercollection.md)
  A collection wrapper that iterates over the indices and identifiers of a collection together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/deletedisabled(_:))*