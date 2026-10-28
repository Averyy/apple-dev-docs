# init(_:selection:rowContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list that computes its views on demand over a constant range, optionally allowing users to select multiple rows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<RowContent>(_ data: Range<Int>, selection: Binding<Set<SelectionValue>>?, @ContentBuilder rowContent: @escaping (Int) -> RowContent) where Content == ForEach<Range<Int>, Int, HStack<RowContent>>, RowContent : View
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
nonisolated init<Data, RowContent>(_ data: Data, selection: Binding<SelectionValue?>?, @ContentBuilder rowContent: @escaping (Data.Element) -> RowContent) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable
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

## Discussion

This instance only reads the initial value of `data` and doesn’t need to identify views across updates. To compute views on demand over a dynamic range, use [`init(_:id:selection:rowContent:)`](./init%28_,id,selection,rowcontent%29.md).

## Parameters

- `data`: A constant range of data to populate the list.
- `selection`: A binding to a set that identifies selected rows.
- `rowContent`: A content builder that creates the view for a single row of the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(_:selection:rowcontent:)-2bobo)*