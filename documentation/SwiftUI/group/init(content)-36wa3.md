# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a group of scenes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init(@SceneBuilder content: () -> Content)
```

Available when `Content` conforms to `Scene`.

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
init<R, C>(@TableColumnBuilder<R, C> content: () -> Content) where R == Content.TableRowValue, C == Content.TableColumnSortComparator
```

```swift
nonisolated
init<R>(@TableRowBuilder<R> content: () -> Content) where R == Content.TableRowValue
```

## Parameters

- `content`: A [`SceneBuilder`](../scenebuilder.md) that produces the scenes to group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/group/init(content:)-36wa3)*