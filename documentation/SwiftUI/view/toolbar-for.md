# toolbar(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the visibility of a bar managed by SwiftUI.

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
func toolbar(_ visibility: Visibility, for bars: ToolbarPlacement...) -> some View
```

#### Discussion

The preferred visibility flows up to the nearest container that renders a bar. This could be a [`NavigationView`](navigationview.md) or [`TabView`](tabview.md) in iOS, or the root view of a [`WindowGroup`](windowgroup.md) in macOS.

This examples shows a view that hides the navigation bar on iOS, or the window toolbar items on macOS.

```swift
NavigationView {
    ContentView()
        .toolbar(.hidden)
}
```

To hide the entire titlebar on macOS, use this modifier with [`windowToolbar`](toolbarplacement/windowtoolbar.md) placement.

```swift
NavigationView {
    ContentView()
        .toolbar(.hidden, for: .windowToolbar)
}
```

You can provide multiple [`ToolbarPlacement`](toolbarplacement.md) instances to hide multiple bars at once.

```swift
TabView {
    NavigationView {
        ContentView()
            .toolbar(
                .hidden, for: .navigationBar, .tabBar)
    }
}
```

> **Note**: In macOS, if you provide [`ToolbarCommands`](toolbarcommands.md) to the scene of your app, this modifier disables the toolbar visibility command while the value of the modifier is not [`automatic`](toolbarplacement/automatic.md).

In macOS, if you provide [`ToolbarCommands`](toolbarcommands.md) to the scene of your app, this modifier disables the toolbar visibility command while the value of the modifier is not [`automatic`](toolbarplacement/automatic.md).

Depending on the specified bars, the requested visibility may not be able to be fulfilled.

## Parameters

- `visibility`: The preferred visibility of the bar.
- `bars`: The bars to update the visibility of or    if empty.

## See Also

- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [struct ToolbarPlacement](toolbarplacement.md)
  The placement of a toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbar(_:for:))*