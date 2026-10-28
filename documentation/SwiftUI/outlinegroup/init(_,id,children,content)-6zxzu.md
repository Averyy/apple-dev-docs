# init(_:id:children:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an outline group from a collection of root data elements, the key path to a data element’s identifier, and a key path to its children.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init<DataElement>(_ data: Data, id: KeyPath<DataElement, ID>, children: KeyPath<DataElement, Data?>, @ContentBuilder content: @escaping (DataElement) -> Leaf) where DataElement == Data.Element
```

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to `Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is `DisclosureGroup<Parent, OutlineSubgroupChildren>`.

**Other overloads**:

```swift
init<C, E>(_ data: Binding<C>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>, @ContentBuilder content: @escaping (Binding<E>) -> Leaf) where Data == Binding<C>, C : MutableCollection, C : RandomAccessCollection, E == C.Element
```

```swift
init<C, E>(_ root: Binding<E>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>, @ContentBuilder content: @escaping (Binding<E>) -> Leaf) where Data == Binding<C>, C : MutableCollection, C : RandomAccessCollection, E == C.Element
```

```swift
init<DataElement>(_ data: Data, id: KeyPath<DataElement, ID>, children: KeyPath<DataElement, Data?>, @TableRowBuilder<DataElement> content: @escaping (DataElement) -> Leaf) where ID == DataElement.ID, DataElement == Data.Element
```

```swift
init<DataElement>(_ root: DataElement, id: KeyPath<DataElement, ID>, children: KeyPath<DataElement, Data?>, @ContentBuilder content: @escaping (DataElement) -> Leaf) where DataElement == Data.Element
```

```swift
init<DataElement>(_ root: DataElement, id: KeyPath<DataElement, ID>, children: KeyPath<DataElement, Data?>, @TableRowBuilder<DataElement> content: @escaping (DataElement) -> Leaf) where ID == DataElement.ID, DataElement == Data.Element
```

## Discussion

This initializer creates an instance that uniquely identifies views across updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to replace that element with a new element, one with a new identity. If the ID of an element changes, then the content view generated from that element will lose any current state and animations.

## Parameters

- `data`: A collection of tree-structured, identified data.
- `id`: The key path to a data element’s identifier.
- `children`: A key path to a property whose non-`nil` value gives the children of `data`. A non-`nil` but empty value denotes an element capable of having children that’s currently childless, such as an empty directory in a file system. On the other hand, if the property at the key path is `nil`, then the outline group treats `data` as a leaf in the tree, like a regular file in a file system.
- `content`: A content builder that produces a content view based on an element in `data`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/outlinegroup/init(_:id:children:content:)-6zxzu)*