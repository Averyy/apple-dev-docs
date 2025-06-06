# toolbarVisibility(_:for:)

**Framework**: RealityKit  
**Kind**: method

Specifies the visibility of a bar managed by SwiftUI.

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
func toolbarVisibility(_ visibility: Visibility, for bars: ToolbarPlacement...) -> some View
```

#### Discussion

The preferred visibility flows up to the nearest container that renders a bar. This could be a `NavigationView` or `TabView` in iOS, or the root view of a `WindowGroup` in macOS.

This examples shows a view that hides the navigation bar on iOS, or the window toolbar items on macOS.

```None
NavigationView {
    ContentView()
        .toolbarVisibility(.hidden)
}
```

To hide the entire titlebar on macOS, use this modifier with `ToolbarPlacement/windowToolbar` placement.

```None
NavigationView {
    ContentView()
        .toolbarVisibility(.hidden, for: .windowToolbar)
}
```

You can provide multiple `ToolbarPlacement` instances to hide multiple bars at once.

```None
TabView {
    NavigationView {
        ContentView()
            .toolbarVisibility(
                .hidden, for: .navigationBar, .tabBar)
    }
}
```

> **Note**: In macOS, if you provide `ToolbarCommands` to the scene of your app, this modifier disables the toolbar visibility command while the value of the modifier is not `ToolbarPlacement/automatic`.

In macOS, if you provide `ToolbarCommands` to the scene of your app, this modifier disables the toolbar visibility command while the value of the modifier is not `ToolbarPlacement/automatic`.

Depending on the specified bars, the requested visibility may not be able to be fulfilled.

## Parameters

- `visibility`: The preferred visibility of the bar.
- `bars`: The bars to update the visibility of or    if empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/toolbarvisibility(_:for:))*