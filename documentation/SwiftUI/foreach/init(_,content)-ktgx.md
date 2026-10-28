# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that computes views on demand over a given constant range.

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
init(_ data: Range<Int>, @ContentBuilder content: @escaping (Int) -> Content)
```

Available when `Data` is `Range<Int>` and `ID` is `Int`.

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
init(_ data: Data, @ContentBuilder content: @escaping (Data.Element) -> Content)
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

The instance only reads the initial value of the provided `data` and doesn’t need to identify views across updates. To compute views on demand over a dynamic range, use [`init(_:id:content:)`](./init%28_,id,content%29.md).

## Parameters

- `data`: A constant range.
- `content`: The content builder that creates views dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(_:content:)-ktgx)*