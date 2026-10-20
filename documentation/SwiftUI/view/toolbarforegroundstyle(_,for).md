# toolbarForegroundStyle(_:for:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies the preferred foreground style of bars managed by SwiftUI.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
func toolbarForegroundStyle<S>(_ style: S, for bars: ToolbarPlacement...) -> some View where S : ShapeStyle
```

#### Discussion

This examples shows a view that renders the navigation bar with a blue foreground color.

```swift
NavigationStack {
    ContentView()
        .navigationTitle("Blue")
        .toolbarForegroundStyle(
            .blue, for: .navigationBar)
}
```

## See Also

### Styling a toolbar
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](./toolbarcolorscheme%28_,for%29.md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func windowToolbarStyle<S>(S) -> some Scene](../scene/windowtoolbarstyle%28_%29.md)
  Sets the style for the toolbar defined within this scene.
- [protocol WindowToolbarStyle](../windowtoolbarstyle.md)
  A specification for the appearance and behavior of a window’s toolbar.
- [var toolbarLabelStyle: ToolbarLabelStyle?](../environmentvalues/toolbarlabelstyle.md)
  The label style to apply to controls within a toolbar.
- [struct ToolbarLabelStyle](../toolbarlabelstyle.md)
  The label style of a toolbar.
- [struct SpacerSizing](../spacersizing.md)
  A type which defines how spacers should size themselves.
- [func toolbarBackground(_:for:)](./toolbarbackground%28_,for%29.md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbarforegroundstyle(_:for:))*