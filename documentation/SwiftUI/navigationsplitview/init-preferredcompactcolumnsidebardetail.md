# init(preferredCompactColumn:sidebar:detail:)

**Framework**: SwiftUI  
**Kind**: init

Creates a two-column navigation split view that enables programmatic control over which column appears on top when the view collapses into a single column in narrow sizes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, @ViewBuilder sidebar: () -> Sidebar, @ViewBuilder detail: () -> Detail) where Content == EmptyView
```

## Parameters

- `preferredCompactColumn`: A   to state that controls which   column appears on top when the view collapses.
- `sidebar`: The view to show in the leading column.
- `detail`: The view to show in the detail area.

## See Also

- [init(preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: () -> Sidebar, content: () -> Content, detail: () -> Detail)](navigationsplitview/init(preferredcompactcolumn:sidebar:content:detail:).md)
  Creates a three-column navigation split view that enables programmatic control over which column appears on top when the view collapses into a single column in narrow sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitview/init(preferredcompactcolumn:sidebar:detail:))*