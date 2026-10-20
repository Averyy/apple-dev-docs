# init(_:id:editActions:selection:rowContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
init<Data, ID, RowContent>(_ data: Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, selection: Binding<SelectionValue>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable
```

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<Data, ID, RowContent>(_ data: Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, selection: Binding<SelectionValue?>?, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable
```

```swift
nonisolated
init<Data, ID, RowContent>(_ data: Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable
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

Use [`deleteDisabled(_:)`](../view/deletedisabled%28_%29.md) and [`moveDisabled(_:)`](../view/movedisabled%28_%29.md) to disable respectively delete or move actions on a per-row basis.

Explicit [`onDelete(perform:)`](../dynamicviewcontent/ondelete%28perform%29.md), [`onMove(perform:)`](../dynamicviewcontent/onmove%28perform%29.md), or [`swipeActions(edge:allowsFullSwipe:content:)`](../view/swipeactions%28edge,allowsfullswipe,content%29.md) modifiers override any synthesized action.

## Parameters

- `data`: The identifiable data for computing and to be edited by the list.
- `id`: The key path to the data model’s identifier.
- `editActions`: The edit actions that are synthesized on `data`.
- `selection`: A binding to a non optional selected value.
- `rowContent`: A content builder that creates the view for a single row of

## See Also

### Creating a list from editable data
- [init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) -> RowContent)](./init%28_,editactions,rowcontent%29.md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
- [init(_:editActions:selection:rowContent:)](./init%28_,editactions,selection,rowcontent%29.md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.
- [init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) -> RowContent)](./init%28_,id,editactions,rowcontent%29.md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:id:editactions:selection:rowcontent:))*