# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a group of map content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
init(@MapContentBuilder content: () -> Content)
```

Available when `Content` conforms to `MapContent`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(@ContentBuilder content: () -> Content)
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

```swift
nonisolated
init<R>(@TableRowBuilder<R> content: () -> Content) where R == Content.TableRowValue
```

## Parameters

- `content`: A map content builder that produces the map content to group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/group/init(content:)-p8cr)*