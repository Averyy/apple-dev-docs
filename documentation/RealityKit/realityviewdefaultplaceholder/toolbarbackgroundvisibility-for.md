# toolbarBackgroundVisibility(_:for:)

**Framework**: RealityKit  
**Kind**: method

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
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

The preferred visibility flows up to the nearest container that renders a bar. This could be a `NavigationView` or `TabView` in iOS, or the root view of a `WindowGroup` in macOS.

In iOS, a value of `ToolbarPlacement/automatic` makes the visibility of a tab bar or navigation bar background depend on where a `List` or `ScrollView` settles. For example, when aligned to the bottom edge of of a scroll view’s content, the background of a tab bar becomes transparent.

Specify a value of `Visibility/visible` to ensure that the background of a bar remains visible regardless of where any scroll view or list stops scrolling.

This example shows a view that prefers to always have the tab bar visible when the middle tab is selected:

```None
TabView {
    FirstTab()
    MiddleTab()
        .toolbarBackgroundVisibility(.visible, for: .tabBar)
    LastTab()
}
```

You can provide multiple placements to customize multiple bars at once, as in the following example:

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/toolbarbackgroundvisibility(_:for:))*