# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that uniquely identifies and creates tabs across updates based on the provided key path to the underlying data’s identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
init<V>(_ data: Data, id: KeyPath<Data.Element, ID>, @TabContentBuilder<V?> content: @escaping (Data.Element) -> Content) where V : Hashable, Content.TabValue == V?
```

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to `Hashable`, and `Content` conforms to `TabContent`.

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
init<V>(_ data: Data, id: KeyPath<Data.Element, ID>, @TableRowBuilder<V> content: @escaping (Data.Element) -> Content) where V == Content.TableRowValue
```

## Discussion

It’s important that the `id` of a data element doesn’t change, unless SwiftUI considers the data element to have been replaced with a new data element that has a new identity. If the `id` of a data element changes, then the tabs generated from that data element will lose any current state and animations.

This initializer overload allows for non optional tab content to be passed into `content`, even if the selection value of the tab view is optional.

## Parameters

- `data`: The data that the [`ForEach`](../foreach.md) instance uses to create views dynamically.
- `id`: The key path to the provided data’s identifier.
- `content`: The builder that creates tabs dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(_:id:content:)-iz9s)*