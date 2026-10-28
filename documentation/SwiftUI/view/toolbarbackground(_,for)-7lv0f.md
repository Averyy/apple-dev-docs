# toolbarBackground(_:for:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2 (renamed: toolbarBackgroundVisibility(_:for:))
- iPadOS 16.0+ - Deprecated in 27.2 (renamed: toolbarBackgroundVisibility(_:for:))
- Mac Catalyst 16.0+ - Deprecated in 27.2 (renamed: toolbarBackgroundVisibility(_:for:))
- macOS 13.0+ - Deprecated in 27.2 (renamed: toolbarBackgroundVisibility(_:for:))
- tvOS 16.0+ - Deprecated in 27.2 (renamed: toolbarBackgroundVisibility(_:for:))
- visionOS 1.0+
- watchOS 9.0+ - Deprecated in 27.2 (renamed: toolbarBackgroundVisibility(_:for:))

## Declaration

```swift
nonisolated
func toolbarBackground(_ visibility: Visibility, for bars: ToolbarPlacement...) -> some View
```

**Other overloads**:

```swift
nonisolated
func toolbarBackground<S>(_ style: S, for bars: ToolbarPlacement...) -> some View where S : ShapeStyle
```

## Discussion

The preferred visibility flows up to the nearest container that renders a bar. This could be a [`NavigationView`](../navigationview.md) or [`TabView`](../tabview.md) in iOS, or the root view of a [`WindowGroup`](../windowgroup.md) in macOS.

In iOS, a value of [`automatic`](../toolbarplacement/automatic.md) makes the visibility of a tab bar or navigation bar background depend on where a [`List`](../list.md) or [`ScrollView`](../scrollview.md) settles. For example, when aligned to the bottom edge of of a scroll view’s content, the background of a tab bar becomes transparent.

Specify a value of [`Visibility.visible`](../visibility/visible.md) to ensure that the background of a bar remains visible regardless of where any scroll view or list stops scrolling.

This example shows a view that prefers to always have the tab bar visible when the middle tab is selected:

```swift
TabView {
    FirstTab()
    MiddleTab()
        .toolbarBackground(.visible, for: .tabBar)
    LastTab()
}
```

You can provide multiple placements to customize multiple bars at once, as in the following example:

```swift
TabView {
    NavigationView {
        ContentView()
            .toolbarBackground(
                .visible, for: .navigationBar, .tabBar)
    }
}
```

## Parameters

- `visibility`: The preferred visibility of the background of the bar.
- `bars`: The bars to update the color scheme of or [`automatic`](../toolbarplacement/automatic.md) if empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbarbackground(_:for:)-7lv0f)*