# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that uniquely identifies and creates views across updates based on the identity of the underlying data.

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
init(_ data: Data, @ContentBuilder content: @escaping (Data.Element) -> Content)
```

Available when `Data` conforms to `RandomAccessCollection`, `ID` is `Data.Element.ID`, and `Data.Element` conforms to `Identifiable`.

**Other overloads**:

```swift
@MainActor
init(_ data: Data, @MapContentBuilder content: @escaping (Data.Element) -> Content) where ID == Data.Element.ID, Data.Element : Identifiable
```

```swift
@MainActor
init(_ data: Range<Int>, @MapContentBuilder content: @escaping (Int) -> Content) where Data == Range<Int>, ID == Int
```

```swift
@export(implementation)
init(_ data: Range<Int>, @ContentBuilder content: @escaping (Int) -> Content)
```

```swift
@export(implementation)
init<C>(_ data: Binding<C>, @ContentBuilder content: @escaping (Binding<C.Element>) -> Content) where Data == LazyMapSequence<C.Indices, (C.Index, ID)>, ID == C.Element.ID, C : MutableCollection, C : RandomAccessCollection, C.Element : Identifiable, C.Index : Hashable
```

```swift
@export(implementation)
nonisolated init<V>(_ data: Data, @TableRowBuilder<V> content: @escaping (Data.Element) -> Content) where ID == Data.Element.ID, V == Content.TableRowValue, Data.Element : Identifiable
```

```swift
init(_ data: Data, @AttachmentContentBuilder content: @escaping (Data.Element) -> Content)
```

```swift
init<V>(_ data: Data, @TabContentBuilder<V> content: @escaping (Data.Element) -> Content) where V == Content.TabValue
```

```swift
init<V>(_ data: Data, @TabContentBuilder<V?> content: @escaping (Data.Element) -> Content) where V : Hashable, Content.TabValue == V?
```

```swift
init<V>(_ data: Range<Int>, @TabContentBuilder<V> content: @escaping (Int) -> Content) where V == Content.TabValue
```

```swift
init<V>(_ data: Range<Int>, @TabContentBuilder<V?> content: @escaping (Int) -> Content) where V : Hashable, Content.TabValue == V?
```

```swift
nonisolated
init(_ data: Data, @Chart3DContentBuilder content: @escaping (Data.Element) -> Content) where ID == Data.Element.ID, Data.Element : Identifiable
```

```swift
nonisolated
init<V>(_ data: Range<Int>, @TableRowBuilder<V> content: @escaping (Int) -> Content) where Data == Range<Int>, ID == Int, V == Content.TableRowValue
```

## Discussion

It’s important that the `id` of a data element doesn’t change unless you replace the data element with a new data element that has a new identity. If the `id` of a data element changes, the content view generated from that data element loses any current state and animations.

## Parameters

- `data`: The identified data that the [`ForEach`](../foreach.md) instance uses to create views dynamically.
- `content`: The content builder that creates views dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(_:content:)-6if9a)*