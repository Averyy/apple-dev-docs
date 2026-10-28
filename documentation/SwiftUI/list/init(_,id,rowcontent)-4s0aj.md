# init(_:id:rowContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list that identifies its rows based on a key path to the identifier of the underlying data.

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
nonisolated init<Data, ID, RowContent>(_ data: Data, id: KeyPath<Data.Element, ID>, @ContentBuilder rowContent: @escaping (Data.Element) -> RowContent) where Content == ForEach<Data, ID, RowContent>, Data : RandomAccessCollection, ID : Hashable, RowContent : View
```

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<Data, ID, RowContent>(_ data: Binding<Data>, id: KeyPath<Data.Element, ID>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, ID)>, ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable
```

## Parameters

- `data`: The data for populating the list.
- `id`: The key path to the data model’s identifier.
- `rowContent`: A content builder that creates the view for a single row of the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:id:rowcontent:)-4s0aj)*