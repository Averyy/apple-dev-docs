# init(_:editActions:rowContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.

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
nonisolated
init<Data, RowContent>(_ data: Binding<Data>, editActions: EditActions<Data>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

## Discussion

The following example creates a list to display a collection of favorite foods allowing the user to delete or move elements from the collection.

```swift
List($foods, editActions: [.delete, .move]) { $food in
   HStack {
       Text(food.name)
       Toggle("Favorite", isOn: $food.isFavorite)
   }
}
```

Use [`deleteDisabled(_:)`](../view/deletedisabled%28_%29.md) and [`moveDisabled(_:)`](../view/movedisabled%28_%29.md) to disable respectively delete or move actions on a per-row basis.

Explicit [`onDelete(perform:)`](../dynamicviewcontent/ondelete%28perform%29.md), [`onMove(perform:)`](../dynamicviewcontent/onmove%28perform%29.md), or [`swipeActions(edge:allowsFullSwipe:content:)`](../view/swipeactions%28edge,allowsfullswipe,content%29.md) modifiers override any synthesized action.

## Parameters

- `data`: A collection of identifiable data for computing the list.
- `editActions`: The edit actions that are synthesized on `data`.
- `rowContent`: A content builder that creates the view for a single row of the list.

## See Also

### Creating a list from editable data
- [init(_:editActions:selection:rowContent:)](./init%28_,editactions,selection,rowcontent%29.md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.
- [init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) -> RowContent)](./init%28_,id,editactions,rowcontent%29.md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
- [init(_:id:editActions:selection:rowContent:)](./init%28_,id,editactions,selection,rowcontent%29.md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:editactions:rowcontent:))*