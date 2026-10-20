# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with the provided section content.

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
init(@ContentBuilder content: () -> Content)
```

Available when `Parent` is `EmptyView` and `Footer` is `EmptyView`.

**Other overloads**:

```swift
nonisolated
init<V>(@TableRowBuilder<V> content: () -> Content) where Parent == EmptyTableRowContent<V>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue
```

## Parameters

- `content`: The section’s content.

## See Also

### Creating a section
- [init(_:content:)](./init%28_,content%29.md)
  Creates a section with the provided section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(content:))*