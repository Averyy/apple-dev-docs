# init(columnVisibility:preferredCompactColumn:sidebar:content:detail:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a three-column navigation split view that enables programmatic control of leading columns’ visibility in regular sizes and which column appears on top when the view collapses into a single column in narrow sizes.

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
init(columnVisibility: Binding<NavigationSplitViewVisibility>, preferredCompactColumn: Binding<NavigationSplitViewColumn>, @ContentBuilder sidebar: () -> Sidebar, @ContentBuilder content: () -> Content, @ContentBuilder detail: () -> Detail)
```

Available when `Sidebar` conforms to `View`, `Content` conforms to `View`, and `Detail` conforms to `View`.

## Parameters

- `columnVisibility`: A [`Binding`](../binding.md) to state that controls the visibility of the leading columns.
- `preferredCompactColumn`: A [`Binding`](../binding.md) to state that controls which column appears on top when the view collapses.
- `sidebar`: The view to show in the leading column.
- `content`: The view to show in the middle column.
- `detail`: The view to show in the detail area.

## See Also

### Specifying a preferred compact column and column visibility
- [init(columnVisibility: Binding<NavigationSplitViewVisibility>, preferredCompactColumn: Binding<NavigationSplitViewColumn>, sidebar: () -> Sidebar, detail: () -> Detail)](./init%28columnvisibility,preferredcompactcolumn,sidebar,detail%29.md)
  Creates a two-column navigation split view that enables programmatic control of the sidebar’s visibility in regular sizes and which column appears on top when the view collapses into a single column in narrow sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitview/init(columnvisibility:preferredcompactcolumn:sidebar:content:detail:))*