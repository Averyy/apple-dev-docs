# toolbarBackgroundVisibility(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func toolbarBackgroundVisibility(_ visibility: Visibility, for bars: ToolbarPlacement...) -> some View
```

#### Discussion

The preferred visibility flows up to the nearest container that renders a bar. This could be a [`NavigationView`](navigationview.md) or [`TabView`](tabview.md) in iOS, or the root view of a [`WindowGroup`](windowgroup.md) in macOS.

In iOS, a value of [`automatic`](toolbarplacement/automatic.md) makes the visibility of a tab bar or navigation bar background depend on where a [`List`](list.md) or [`ScrollView`](scrollview.md) settles. For example, when aligned to the bottom edge of of a scroll view’s content, the background of a tab bar becomes transparent.

Specify a value of [`Visibility.visible`](visibility/visible.md) to ensure that the background of a bar remains visible regardless of where any scroll view or list stops scrolling.

This example shows a view that prefers to always have the tab bar visible when the middle tab is selected:

```swift
TabView {
    FirstTab()
    MiddleTab()
        .toolbarBackgroundVisibility(.visible, for: .tabBar)
    LastTab()
}
```

You can provide multiple placements to customize multiple bars at once, as in the following example:

```swift
TabView {
    NavigationView {
        ContentView()
            .toolbarBackgroundVisibility(
                .visible, for: .navigationBar, .tabBar)
    }
}
```

## Parameters

- `visibility`: The preferred visibility of the background of the bar.
- `bars`: The bars to update the color scheme of or    if empty.

## See Also

- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](view/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [struct ToolbarPlacement](toolbarplacement.md)
  The placement of a toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbarbackgroundvisibility(_:for:))*