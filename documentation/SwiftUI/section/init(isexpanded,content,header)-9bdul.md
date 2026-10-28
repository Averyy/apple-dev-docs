# init(isExpanded:content:header:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with a header and the provided section content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<V, H>(isExpanded: Binding<Bool>, @TableRowBuilder<V> content: () -> Content, @ContentBuilder header: () -> H) where Parent == TableHeaderRowContent<V, H>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue, H : View
```

Available when `Parent` conforms to `TableRowContent` and `Content` conforms to `TableRowContent`.

**Other overloads**:

```swift
@export(implementation)
init(isExpanded: Binding<Bool>, @ContentBuilder content: () -> Content, @ContentBuilder header: () -> Parent)
```

## Parameters

- `isExpanded`: A binding to a Boolean value that determines the section’s expansion state (expanded or collapsed).
- `content`: The section’s content.
- `header`: A view to use as the section’s header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(isexpanded:content:header:)-9bdul)*