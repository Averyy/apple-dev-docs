# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that uniquely identifies and creates table rows across updates based on the provided key path to the underlying data’s identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<V>(_ data: Data, id: KeyPath<Data.Element, ID>, @TableRowBuilder<V> content: @escaping (Data.Element) -> Content) where V == Content.TableRowValue
```

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to `Hashable`, and `Content` conforms to `TableRowContent`.

**Other overloads**:

```swift
@MainActor
init(_ data: Data, id: KeyPath<Data.Element, ID>, @MapContentBuilder content: @escaping (Data.Element) -> Content)
```

```swift
@export(implementation)
init(_ data: Data, id: KeyPath<Data.Element, ID>, @ContentBuilder content: @escaping (Data.Element) -> Content)
```

```swift
@export(implementation)
init<C>(_ data: Binding<C>, id: KeyPath<C.Element, ID>, @ContentBuilder content: @escaping (Binding<C.Element>) -> Content) where Data == LazyMapSequence<C.Indices, (C.Index, ID)>, C : MutableCollection, C : RandomAccessCollection, C.Index : Hashable
```

```swift
init(_ data: Data, id: KeyPath<Data.Element, ID>, @AttachmentContentBuilder content: @escaping (Data.Element) -> Content)
```

```swift
nonisolated
init(_ data: Data, id: KeyPath<Data.Element, ID>, @Chart3DContentBuilder content: @escaping (Data.Element) -> Content)
```

```swift
nonisolated
init<V>(_ data: Data, id: KeyPath<Data.Element, ID>, @TabContentBuilder<V> content: @escaping (Data.Element) -> Content) where V == Content.TabValue
```

```swift
nonisolated
init<V>(_ data: Data, id: KeyPath<Data.Element, ID>, @TabContentBuilder<V?> content: @escaping (Data.Element) -> Content) where V : Hashable, Content.TabValue == V?
```

## Parameters

- `data`: The data that the [`ForEach`](../foreach.md) instance uses to create table rows dynamically.
- `id`: The key path to the provided data’s identifier.
- `content`: The table row builder that creates rows dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(_:id:content:)-7inug)*