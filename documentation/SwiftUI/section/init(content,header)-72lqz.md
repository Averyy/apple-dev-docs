# init(content:header:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with a header and the provided section content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<V, H>(@TableRowBuilder<V> content: () -> Content, @ContentBuilder header: () -> H) where Parent == TableHeaderRowContent<V, H>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue, H : View
```

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to `TableRowContent`, and `Footer` conforms to `TableRowContent`.

**Other overloads**:

```swift
@export(implementation)
init(@ContentBuilder content: () -> Content, @ContentBuilder header: () -> Parent)
```

## Parameters

- `content`: The section’s content.
- `header`: A view to use as the section’s header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(content:header:)-72lqz)*