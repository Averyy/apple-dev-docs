# init(_:rowContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list that computes its views on demand over a constant range.

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
nonisolated init<RowContent>(_ data: Range<Int>, @ContentBuilder rowContent: @escaping (Int) -> RowContent) where Content == ForEach<Range<Int>, Int, RowContent>, RowContent : View
```

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<Data, RowContent>(_ data: Binding<Data>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

```swift
@export(implementation)
nonisolated init<Data, RowContent>(_ data: Data, @ContentBuilder rowContent: @escaping (Data.Element) -> RowContent) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable
```

## Discussion

This instance only reads the initial value of `data` and doesn’t need to identify views across updates. To compute views on demand over a dynamic range, use [`init(_:id:rowContent:)`](./init%28_,id,rowcontent%29.md).

## Parameters

- `data`: A constant range of data to populate the list.
- `rowContent`: A content builder that creates the view for a single row of the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:rowcontent:)-9jce2)*