# init(content:header:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with a header and the provided section content.

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
init(@ContentBuilder content: () -> Content, @ContentBuilder header: () -> Parent)
```

Available when `Footer` is `EmptyView`.

**Other overloads**:

```swift
nonisolated
init<V, H>(@TableRowBuilder<V> content: () -> Content, @ContentBuilder header: () -> H) where Parent == TableHeaderRowContent<V, H>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue, H : View
```

## Parameters

- `content`: The section’s content.
- `header`: A view to use as the section’s header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(content:header:)-8u854)*