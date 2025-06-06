# init(columnVisibility:sidebar:content:detail:)

**Framework**: SwiftUI  
**Kind**: init

Creates a three-column navigation split view that enables programmatic control of leading columns’ visibility.

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
init(columnVisibility: Binding<NavigationSplitViewVisibility>, @ViewBuilder sidebar: () -> Sidebar, @ViewBuilder content: () -> Content, @ViewBuilder detail: () -> Detail)
```

## Parameters

- `columnVisibility`: A   to state that controls the   visibility of the leading columns.
- `sidebar`: The view to show in the leading column.
- `content`: The view to show in the middle column.
- `detail`: The view to show in the detail area.

## See Also

- [init(columnVisibility: Binding<NavigationSplitViewVisibility>, sidebar: () -> Sidebar, detail: () -> Detail)](navigationsplitview/init(columnvisibility:sidebar:detail:).md)
  Creates a two-column navigation split view that enables programmatic control of the sidebar’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitview/init(columnvisibility:sidebar:content:detail:))*