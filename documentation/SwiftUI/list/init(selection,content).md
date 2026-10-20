# init(selection:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list with the given content that supports selecting a single row that cannot be deselected.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
init(selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

**Other overloads**:

```swift
nonisolated
init(selection: Binding<SelectionValue?>?, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(selection: Binding<Set<SelectionValue>>?, @ContentBuilder content: () -> Content)
```

## Parameters

- `selection`: A binding to a selected row.
- `content`: The content of the list.

## See Also

### Creating a list from a set of views
- [init(content: () -> Content)](./init%28content%29.md)
  Creates a list with the given content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(selection:content:))*