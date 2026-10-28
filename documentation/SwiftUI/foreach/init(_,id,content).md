# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
init(_ data: Data, id: KeyPath<Data.Element, ID>, @MapContentBuilder content: @escaping (Data.Element) -> Content)
```

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to `Hashable`, and `Content` conforms to `MapContent`.

**Other overloads**:

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

```swift
nonisolated
init<V>(_ data: Data, id: KeyPath<Data.Element, ID>, @TableRowBuilder<V> content: @escaping (Data.Element) -> Content) where V == Content.TableRowValue
```

## Mentions

- [Creating performant scrollable stacks](../creating-performant-scrollable-stacks.md)

## Discussion

It’s important that the `id` of a data element doesn’t change, unless the data element has been replaced with a new data element that has a new identity. If the `id` of a data element changes, then the map content generated from that data element will lose any current state and animations.

## Parameters

- `data`: The data that the [`ForEach`](../foreach.md) instance uses to create map content dynamically.
- `id`: The key path to the provided data’s identifier.
- `content`: The map content builder that creates map content dynamically.

## See Also

### Creating a collection
- [init(Data)](./init%28_%29.md)
  Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:content:)](./init%28_,content%29.md)
  Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init<V>(sections: V, content: (SectionConfiguration) -> Content)](./init%28sections,content%29.md)
  Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.
- [init<V>(subviews: V, content: (Subview) -> Content)](./init%28subviews,content%29.md)
  Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(_:id:content:))*