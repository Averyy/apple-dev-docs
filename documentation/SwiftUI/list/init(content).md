# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list with the given content.

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
nonisolated
init(@ContentBuilder content: () -> Content)
```

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

## Parameters

- `content`: The content of the list.

## See Also

### Creating a list from a set of views
- [init(selection:content:)](./init%28selection,content%29.md)
  Creates a list with the given content that supports selecting a single row that cannot be deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(content:))*