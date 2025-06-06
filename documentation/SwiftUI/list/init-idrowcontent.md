# init(_:id:rowContent:)

**Framework**: SwiftUI  
**Kind**: init

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
@MainActor
@preconcurrency init<Data, ID, RowContent>(_ data: Binding<Data>, id: KeyPath<Data.Element, ID>, @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, ID)>, ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable
```

## Parameters

- `data`: The data for populating the list.
- `id`: The key path to the data model’s identifier.
- `rowContent`: A view builder that creates the view for a single row of   the list.

## See Also

- [init(_:rowContent:)](list/init(_:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data.
- [init(_:selection:rowContent:)](list/init(_:selection:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, optionally allowing users to select a single row.
- [init(_:id:selection:rowContent:)](list/init(_:id:selection:rowcontent:).md)
  Creates a list that identifies its rows based on a key path to the identifier of the underlying data, optionally allowing users to select a single row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:id:rowcontent:))*