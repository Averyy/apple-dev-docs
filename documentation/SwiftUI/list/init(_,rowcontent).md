# init(_:rowContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list that computes its rows on demand from an underlying collection of identifiable data.

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
@export(implementation)
nonisolated init<Data, RowContent>(_ data: Binding<Data>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<Data, RowContent>(_ data: Data, @ContentBuilder rowContent: @escaping (Data.Element) -> RowContent) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable
```

```swift
@export(implementation)
nonisolated init<RowContent>(_ data: Range<Int>, @ContentBuilder rowContent: @escaping (Int) -> RowContent) where Content == ForEach<Range<Int>, Int, RowContent>, RowContent : View
```

## Parameters

- `data`: A collection of identifiable data for computing the list.
- `rowContent`: A content builder that creates the view for a single row of the list.

## See Also

### Creating a list from enumerated data
- [init(_:selection:rowContent:)](./init%28_,selection,rowcontent%29.md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, optionally allowing users to select a single row.
- [init(_:id:rowContent:)](./init%28_,id,rowcontent%29.md)
  Creates a list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:selection:rowContent:)](./init%28_,id,selection,rowcontent%29.md)
  Creates a list that identifies its rows based on a key path to the identifier of the underlying data, optionally allowing users to select a single row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:rowcontent:))*