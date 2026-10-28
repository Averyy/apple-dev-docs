# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a group of table rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<R>(@TableRowBuilder<R> content: () -> Content) where R == Content.TableRowValue
```

Available when `Content` conforms to `TableRowContent`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(@ContentBuilder content: () -> Content)
```

```swift
init(@MapContentBuilder content: () -> Content)
```

```swift
init<V>(@TabContentBuilder<V> content: () -> Content) where V == Content.TabValue
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

## Parameters

- `content`: A [`TableRowBuilder`](../tablerowbuilder.md) that produces the rows to group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/group/init(content:)-2nilv)*