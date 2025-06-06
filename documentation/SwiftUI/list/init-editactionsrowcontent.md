# init(_:editActions:rowContent:)

**Framework**: SwiftUI  
**Kind**: init

Creates a list that computes its rows on demand from an underlying collection of identifiable data and allows to edit the collection.

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
@MainActor
@preconcurrency init<Data, RowContent>(_ data: Binding<Data>, editActions: EditActions<Data>, @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

#### Discussion

The following example creates a list to display a collection of favorite foods allowing the user to delete or move elements from the collection.

```swift
List($foods, editActions: [.delete, .move]) { $food in
   HStack {
       Text(food.name)
       Toggle("Favorite", isOn: $food.isFavorite)
   }
}
```

Use [`deleteDisabled(_:)`](view/deletedisabled(_:).md) and [`moveDisabled(_:)`](view/movedisabled(_:).md) to disable respectively delete or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`, `DynamicViewContent.onMove(perform:)`, or `View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any synthesized action

## Parameters

- `data`: A collection of identifiable data for computing the list.
- `editActions`: The edit actions that are synthesized on  .
- `rowContent`: A view builder that creates the view for a single row of   the list.

## See Also

- [init(_:editActions:selection:rowContent:)](list/init(_:editactions:selection:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, allows to edit the collection, and requires a selection of a single row.
- [init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) -> RowContent)](list/init(_:id:editactions:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data and allows to edit the collection.
- [init(_:id:editActions:selection:rowContent:)](list/init(_:id:editactions:selection:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable, allows to edit the collection, and requires a selection of a single row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:editactions:rowcontent:))*