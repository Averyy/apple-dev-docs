# init(_:rowContent:)

**Framework**: SwiftUI  
**Kind**: init

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
@MainActor
@preconcurrency init<Data, RowContent>(_ data: Binding<Data>, @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

## Parameters

- `data`: A collection of identifiable data for computing the list.
- `rowContent`: A view builder that creates the view for a single row of   the list.

## See Also

- [init(_:selection:rowContent:)](list/init(_:selection:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, optionally allowing users to select a single row.
- [init(_:id:rowContent:)](list/init(_:id:rowcontent:).md)
  Creates a list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:selection:rowContent:)](list/init(_:id:selection:rowcontent:).md)
  Creates a list that identifies its rows based on a key path to the identifier of the underlying data, optionally allowing users to select a single row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:rowcontent:))*