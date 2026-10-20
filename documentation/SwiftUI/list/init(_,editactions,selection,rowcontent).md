# init(_:editActions:selection:rowContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
init<Data, RowContent>(_ data: Binding<Data>, editActions: EditActions<Data>, selection: Binding<SelectionValue>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<Data, RowContent>(_ data: Binding<Data>, editActions: EditActions<Data>, selection: Binding<SelectionValue?>?, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

```swift
nonisolated
init<Data, RowContent>(_ data: Binding<Data>, editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

#### Discussion

The following example creates a list to display a collection of favorite foods allowing the user to delete or move elements from the collection, and select a single element.

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

Use [`deleteDisabled(_:)`](../view/deletedisabled%28_%29.md) and [`moveDisabled(_:)`](../view/movedisabled%28_%29.md) to disable respectively delete or move actions on a per-row basis.

Explicit [`onDelete(perform:)`](../dynamicviewcontent/ondelete%28perform%29.md), [`onMove(perform:)`](../dynamicviewcontent/onmove%28perform%29.md), or [`swipeActions(edge:allowsFullSwipe:content:)`](../view/swipeactions%28edge,allowsfullswipe,content%29.md) modifiers override any synthesized action.

## Parameters

- `data`: The identifiable data for computing the list.
- `editActions`: The edit actions that are synthesized on `data`.
- `selection`: A binding to a non optional selected value.
- `rowContent`: A content builder that creates the view for a single row of the list.

## See Also

### Creating a list from editable data
- [init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) -> RowContent)](./init%28_,editactions,rowcontent%29.md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
- [init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) -> RowContent)](./init%28_,id,editactions,rowcontent%29.md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
- [init(_:id:editActions:selection:rowContent:)](./init%28_,id,editactions,selection,rowcontent%29.md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:editactions:selection:rowcontent:))*