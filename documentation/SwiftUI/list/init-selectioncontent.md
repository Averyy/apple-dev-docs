# init(selection:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a list with the given content that supports selecting a single row that cannot be deselcted.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency init(selection: Binding<SelectionValue>, @ViewBuilder content: () -> Content)
```

## Parameters

- `selection`: A binding to a selected row.
- `content`: The content of the list.

## See Also

- [init(content: () -> Content)](list/init(content:).md)
  Creates a list with the given content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(selection:content:))*