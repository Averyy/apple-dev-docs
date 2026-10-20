# init(sidebar:detail:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a two-column navigation split view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(@ContentBuilder sidebar: () -> Sidebar, @ContentBuilder detail: () -> Detail) where Content == EmptyView
```

## Mentions

- [Migrating to new navigation types](../migrating-to-new-navigation-types.md)

## Parameters

- `sidebar`: The view to show in the leading column.
- `detail`: The view to show in the detail area.

## See Also

### Creating a navigation split view
- [init(sidebar: () -> Sidebar, content: () -> Content, detail: () -> Detail)](./init%28sidebar,content,detail%29.md)
  Creates a three-column navigation split view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitview/init(sidebar:detail:))*