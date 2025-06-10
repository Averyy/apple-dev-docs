# windowToolbarStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for the toolbar defined within this scene.

**Availability**:
- macOS 11.0+

## Declaration

```swift
nonisolated
func windowToolbarStyle<S>(_ style: S) -> some Scene where S : WindowToolbarStyle
```

## See Also

- [func toolbarBackground(_:for:)](view/toolbarbackground(_:for:).md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](view/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](view/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [protocol WindowToolbarStyle](windowtoolbarstyle.md)
  A specification for the appearance and behavior of a window’s toolbar.
- [var toolbarLabelStyle: ToolbarLabelStyle?](environmentvalues/toolbarlabelstyle.md)
  The label style to apply to controls within a toolbar.
- [struct ToolbarLabelStyle](toolbarlabelstyle.md)
  The label style of a toolbar.
- [struct SpacerSizing](spacersizing.md)
  A type which defines how spacers should size themselves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/windowtoolbarstyle(_:))*