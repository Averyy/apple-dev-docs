# toolbarBackground(_:for:)

**Framework**: FinanceKitUI  
**Kind**: method

Specifies the preferred shape style of the background of a bar managed by SwiftUI.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func toolbarBackground<S>(_ style: S, for bars: ToolbarPlacement...) -> some View where S : ShapeStyle
```

#### Discussion

The preferred style flows up to the nearest container that renders a bar. This could be a `NavigationView` or `TabView` in iOS, or the root view of a `WindowGroup` in macOS. This example shows a view that renders the navigation bar with a blue background and dark color scheme.

```None
NavigationView {
    ContentView()
        .toolbarBackground(.white)
        .toolbarColorScheme(.dark)
}
```

You can provide multiple `ToolbarPlacement` instances to customize multiple bars at once.

```None
TabView {
    NavigationView {
        ContentView()
            .toolbarBackground(
                .blue, for: .navigationBar, .tabBar)
            .toolbarColorScheme(
                .dark, for: .navigationBar, .tabBar)
    }
}
```

When used within a `TabView`, the specified style will be preferred while the tab is currently active. You can use a `Group` to specify the same preferred background for every tab.

```None
TabView {
    Group {
        MainView()
        SettingsView()
    }
    .toolbarBackground(.blue, for: .tabBar)
}
```

Depending on the specified bars, the requested style may not be able to be fullfilled.

## Parameters

- `style`: The style to display as the background of the bar.
- `bars`: The bars to use the style for or    if empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/toolbarbackground(_:for:)-2vb8w)*