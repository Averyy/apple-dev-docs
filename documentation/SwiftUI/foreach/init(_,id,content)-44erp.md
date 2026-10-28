# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(_ data: Data, id: KeyPath<Data.Element, ID>, @AttachmentContentBuilder content: @escaping (Data.Element) -> Content)
```

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to `Hashable`, and `Content` conforms to `AttachmentContent`.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(_:id:content:)-44erp)*