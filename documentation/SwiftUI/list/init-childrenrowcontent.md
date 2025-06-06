# init(_:children:rowContent:)

**Framework**: SwiftUI  
**Kind**: init

Creates a hierarchical list that computes its rows on demand from a binding to an underlying collection of identifiable data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency init<Data, RowContent>(_ data: Binding<Data>, children: WritableKeyPath<Data.Element, Data?>, @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == OutlineGroup<Binding<Data>, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable
```

## Parameters

- `data`: A collection of identifiable data for computing the list.
- `children`: A key path to a property whose non-  value gives the   children of  . A non-  but empty value denotes a node capable   of having children that is currently childless, such as an empty   directory in a file system. On the other hand, if the property at the   key path is  , then   is treated as a leaf node in the tree,   like a regular file in a file system.
- `rowContent`: A view builder that creates the view for a single row of   the list.

## See Also

- [init(_:children:selection:rowContent:)](list/init(_:children:selection:rowcontent:).md)
  Creates a hierarchical list that computes its rows on demand from a binding to an underlying collection of identifiable data and allowing users to have exactly one row always selected.
- [init(_:id:children:rowContent:)](list/init(_:id:children:rowcontent:).md)
  Creates a hierarchical list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:children:selection:rowContent:)](list/init(_:id:children:selection:rowcontent:).md)
  Creates a hierarchical list that identifies its rows based on a key path to the identifier of the underlying data and allowing users to have exactly one row always selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:children:rowcontent:))*