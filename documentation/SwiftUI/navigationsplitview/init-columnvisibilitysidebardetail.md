# init(columnVisibility:sidebar:detail:)

**Framework**: SwiftUI  
**Kind**: init

Creates a two-column navigation split view that enables programmatic control of the sidebar’s visibility.

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
init(columnVisibility: Binding<NavigationSplitViewVisibility>, @ContentBuilder sidebar: () -> Sidebar, @ContentBuilder detail: () -> Detail) where Content == EmptyView
```

## Parameters

- `columnVisibility`: A [`Binding`](binding.md) to state that controls the visibility of the leading column.
- `sidebar`: The view to show in the leading column.
- `detail`: The view to show in the detail area.

## See Also

- [init(columnVisibility: Binding<NavigationSplitViewVisibility>, sidebar: () -> Sidebar, content: () -> Content, detail: () -> Detail)](navigationsplitview/init(columnvisibility:sidebar:content:detail:).md)
  Creates a three-column navigation split view that enables programmatic control of leading columns’ visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitview/init(columnvisibility:sidebar:detail:))*