# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with the provided section content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<V>(@TableRowBuilder<V> content: () -> Content) where Parent == EmptyTableRowContent<V>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue
```

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to `TableRowContent`, and `Footer` conforms to `TableRowContent`.

**Other overloads**:

```swift
@export(implementation)
init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content`: The section’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(content:)-1c3ry)*