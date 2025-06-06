# init(_:id:editActions:selection:rowContent:)

**Framework**: SwiftUI  
**Kind**: init

Creates a list that computes its rows on demand from an underlying collection of identifiable, allows to edit the collection, and requires a selection of a single row.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency init<Data, ID, RowContent>(_ data: Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, selection: Binding<SelectionValue>, @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable
```

#### Discussion

The following example creates a list to display a collection of favorite foods allowing the user to delete or move elements from the collection, and selects a single row.

```swift
List(
    $foods,
    editActions: [.delete, .move],
    selection: $selectedFood
) { $food in
   HStack {
       Text(food.name)
       Toggle("Favorite", isOn: $food.isFavorite)
   }
}
```

Use [`deleteDisabled(_:)`](view/deletedisabled(_:).md) and [`moveDisabled(_:)`](view/movedisabled(_:).md) to disable respectively delete or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`, `DynamicViewContent.onMove(perform:)`, or `View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any synthesized action

## Parameters

- `data`: The identifiable data for computing and to be edited by   the list.
- `id`: The key path to the data model’s identifier.
- `editActions`: The edit actions that are synthesized on  .
- `selection`: A binding to a non optional selected value.
- `rowContent`: A view builder that creates the view for a single row of

## See Also

- [init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) -> RowContent)](list/init(_:editactions:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data and allows to edit the collection.
- [init(_:editActions:selection:rowContent:)](list/init(_:editactions:selection:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, allows to edit the collection, and requires a selection of a single row.
- [init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) -> RowContent)](list/init(_:id:editactions:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data and allows to edit the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:id:editactions:selection:rowcontent:))*