# toolbarBackground(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the preferred shape style of the background of a bar managed by SwiftUI.

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
func toolbarBackground<S>(_ style: S, for bars: ToolbarPlacement...) -> some View where S : ShapeStyle
```

#### Discussion

The preferred style flows up to the nearest container that renders a bar. This could be a [`NavigationView`](navigationview.md) or [`TabView`](tabview.md) in iOS, or the root view of a [`WindowGroup`](windowgroup.md) in macOS. This example shows a view that renders the navigation bar with a blue background and dark color scheme.

```swift
NavigationView {
    ContentView()
        .toolbarBackground(.white)
        .toolbarColorScheme(.dark)
}
```

You can provide multiple [`ToolbarPlacement`](toolbarplacement.md) instances to customize multiple bars at once.

```swift
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

When used within a [`TabView`](tabview.md), the specified style will be preferred while the tab is currently active. You can use a [`Group`](group.md) to specify the same preferred background for every tab.

```swift
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

## See Also

- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](view/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](view/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func windowToolbarStyle<S>(S) -> some Scene](scene/windowtoolbarstyle(_:).md)
  Sets the style for the toolbar defined within this scene.
- [protocol WindowToolbarStyle](windowtoolbarstyle.md)
  A specification for the appearance and behavior of a window’s toolbar.
- [var toolbarLabelStyle: ToolbarLabelStyle?](environmentvalues/toolbarlabelstyle.md)
  The label style to apply to controls within a toolbar.
- [struct ToolbarLabelStyle](toolbarlabelstyle.md)
  The label style of a toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbarbackground(_:for:))*