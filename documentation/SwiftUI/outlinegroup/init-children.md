# init(_:children:)

**Framework**: SwiftUI  
**Kind**: init

Creates an outline group from a collection of root data elements and a key path to element’s children.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init<DataElement>(_ data: Data, children: KeyPath<DataElement, Data?>) where ID == DataElement.ID, Parent == TableRow<DataElement>, Leaf == TableRow<DataElement>, Subgroup == TableRow<DataElement>, DataElement : Identifiable, DataElement == Data.Element
```

#### Discussion

This initializer provides a default `TableRowBuilder` using `TableRow` for each data element.

This initializer creates an instance that uniquely identifies table rows across updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

## Parameters

- `data`: A collection of tree-structured, identified data.
- `children`: A key path to a property whose non-  value gives the   children of  . A non-  but empty value denotes an element   capable of having children that’s currently childless, such as an   empty directory in a file system. On the other hand, if the property   at the key path is  , then the outline group treats   as a   leaf in the tree, like a regular file in a file system.

## See Also

- [init(_:children:content:)](outlinegroup/init(_:children:content:).md)
  Creates an outline group from a binding to a collection of root data elements and a key path to its children.
- [init(_:id:children:content:)](outlinegroup/init(_:id:children:content:).md)
  Creates an outline group from a binding to a collection of root data elements, the key path to a data element’s identifier, and a key path to its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/outlinegroup/init(_:children:))*