# IndexedIdentifierCollection

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A collection wrapper that iterates over the indices and identifiers of a collection together.

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
struct IndexedIdentifierCollection<Base, ID> where Base : Collection, ID : Hashable
```

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your behalf.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Editing a list
- [func moveDisabled(Bool) -> some View](./view/movedisabled%28_%29.md)
  Adds a condition for whether the view’s view hierarchy is movable.
- [func deleteDisabled(Bool) -> some View](./view/deletedisabled%28_%29.md)
  Adds a condition for whether the view’s view hierarchy is deletable.
- [var editMode: Binding<EditMode>?](./environmentvalues/editmode.md)
  An indication of whether the user can edit the contents of a view associated with this environment.
- [enum EditMode](./editmode.md)
  A mode that indicates whether the user can edit a view’s content.
- [struct EditActions](./editactions.md)
  A set of edit actions on a collection of data that a view can offer to a user.
- [struct EditableCollectionContent](./editablecollectioncontent.md)
  An opaque wrapper view that adds editing capabilities to a row in a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/indexedidentifiercollection)*