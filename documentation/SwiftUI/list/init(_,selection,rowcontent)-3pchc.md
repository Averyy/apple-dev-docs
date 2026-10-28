# init(_:selection:rowContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list that computes its rows on demand from an underlying collection of identifiable data, optionally allowing users to select a single row.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@export(implementation)
nonisolated init<Data, RowContent>(_ data: Data, selection: Binding<SelectionValue?>?, @ContentBuilder rowContent: @escaping (Data.Element) -> RowContent) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable
```

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<Data, RowContent>(_ data: Binding<Data>, selection: Binding<SelectionValue?>?, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

```swift
@export(implementation)
nonisolated init<Data, RowContent>(_ data: Binding<Data>, selection: Binding<Set<SelectionValue>>?, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

```swift
@export(implementation)
nonisolated init<Data, RowContent>(_ data: Data, selection: Binding<Set<SelectionValue>>?, @ContentBuilder rowContent: @escaping (Data.Element) -> RowContent) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable
```

```swift
@export(implementation)
nonisolated init<RowContent>(_ data: Range<Int>, selection: Binding<SelectionValue?>?, @ContentBuilder rowContent: @escaping (Int) -> RowContent) where Content == ForEach<Range<Int>, Int, RowContent>, RowContent : View
```

```swift
nonisolated
init<Data, RowContent>(_ data: Data, selection: Binding<SelectionValue>, @ContentBuilder rowContent: @escaping (Data.Element) -> RowContent) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable
```

```swift
nonisolated
init<RowContent>(_ data: Range<Int>, selection: Binding<SelectionValue>, @ContentBuilder rowContent: @escaping (Int) -> RowContent) where Content == ForEach<Range<Int>, Int, HStack<RowContent>>, RowContent : View
```

```swift
nonisolated
init<RowContent>(_ data: Range<Int>, selection: Binding<Set<SelectionValue>>?, @ContentBuilder rowContent: @escaping (Int) -> RowContent) where Content == ForEach<Range<Int>, Int, HStack<RowContent>>, RowContent : View
```

## Parameters

- `data`: The identifiable data for computing the list.
- `selection`: A binding to a selected value.
- `rowContent`: A content builder that creates the view for a single row of the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:selection:rowcontent:)-3pchc)*