# toolbarLabelStyle

**Framework**: SwiftUI  
**Kind**: property

The label style to apply to controls within a toolbar.

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
var toolbarLabelStyle: ToolbarLabelStyle? { get }
```

#### Discussion

The default is `nil` for items outside the window toolbar.

## See Also

- [func toolbarBackground(_:for:)](view/toolbarbackground(_:for:).md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](view/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](view/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func windowToolbarStyle<S>(S) -> some Scene](scene/windowtoolbarstyle(_:).md)
  Sets the style for the toolbar defined within this scene.
- [protocol WindowToolbarStyle](windowtoolbarstyle.md)
  A specification for the appearance and behavior of a window’s toolbar.
- [struct ToolbarLabelStyle](toolbarlabelstyle.md)
  The label style of a toolbar.
- [struct SpacerSizing](spacersizing.md)
  A type which defines how spacers should size themselves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/toolbarlabelstyle)*