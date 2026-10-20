# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a group of content.

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
nonisolated init(@ContentBuilder content: () -> Content)
```

**Other overloads**:

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

```swift
nonisolated
init<R>(@TableRowBuilder<R> content: () -> Content) where R == Content.TableRowValue
```

## Parameters

- `content`: A [`ContentBuilder`](../contentbuilder.md) that produces the content to group.

## See Also

### Creating a group
- [init<Base, Result>(sections: Base, transform: (SectionCollection) -> Result)](./init%28sections,transform%29.md)
  Constructs a group from the sections of the given view.
- [init<Base, Result>(subviews: Base, transform: (SubviewsCollection) -> Result)](./init%28subviews,transform%29.md)
  Constructs a group from the subviews of the given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/group/init(content:))*