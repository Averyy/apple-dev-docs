# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a group of tab content.

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
init<V>(@TabContentBuilder<V> content: () -> Content) where V == Content.TabValue
```

Available when `Content` conforms to `TabContent`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(@ContentBuilder content: () -> Content)
```

```swift
init(@MapContentBuilder content: () -> Content)
```

```swift
init<V>(@TabContentBuilder<V?> content: () -> Content) where V : Hashable, Content.TabValue == V?
```

```swift
nonisolated
init(@SceneBuilder content: () -> Content)
```

```swift
nonisolated
init<R, C>(@TableColumnBuilder<R, C> content: () -> Content) where R == Content.TableRowValue, C == Content.TableColumnSortComparator
```

```swift
nonisolated
init<R>(@TableRowBuilder<R> content: () -> Content) where R == Content.TableRowValue
```

## Parameters

- `content`: A [`TabContentBuilder`](../tabcontentbuilder.md) that produces the content to group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/group/init(content:)-1amme)*