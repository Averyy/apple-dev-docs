# WindowToolbarStyle

**Framework**: SwiftUI  
**Kind**: protocol

A specification for the appearance and behavior of a window’s toolbar.

**Availability**:
- macOS 11.0+

## Declaration

```swift
protocol WindowToolbarStyle
```

## Topics

### Getting built-in window toolbar styles
- [static var automatic: DefaultWindowToolbarStyle](windowtoolbarstyle/automatic.md)
  The automatic window toolbar style.
- [static var expanded: ExpandedWindowToolbarStyle](windowtoolbarstyle/expanded.md)
  A window toolbar style which displays its title bar area above the toolbar.
- [static var unified: UnifiedWindowToolbarStyle](windowtoolbarstyle/unified.md)
  A window toolbar style which displays its toolbar and title bar inline.
- [static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle](windowtoolbarstyle/unified(showstitle:).md)
  A window toolbar style which displays its toolbar and title bar inline.
- [static var unifiedCompact: UnifiedCompactWindowToolbarStyle](windowtoolbarstyle/unifiedcompact.md)
  A window toolbar style similar to [`unified`](windowtoolbarstyle/unified.md), but with a more compact vertical sizing.
- [static func unifiedCompact(showsTitle: Bool) -> UnifiedCompactWindowToolbarStyle](windowtoolbarstyle/unifiedcompact(showstitle:).md)
  A window toolbar style similar to [`unified`](windowtoolbarstyle/unified.md), but with a more compact vertical sizing.
### Supporting types
- [struct DefaultWindowToolbarStyle](defaultwindowtoolbarstyle.md)
  The default window toolbar style.
- [struct ExpandedWindowToolbarStyle](expandedwindowtoolbarstyle.md)
  A window toolbar style which displays its title bar area above the toolbar.
- [struct UnifiedWindowToolbarStyle](unifiedwindowtoolbarstyle.md)
  A window toolbar style which displays its toolbar and title bar inline.
- [struct UnifiedCompactWindowToolbarStyle](unifiedcompactwindowtoolbarstyle.md)
  A window toolbar style similar to [`unified`](windowtoolbarstyle/unified.md), but with a more compact vertical sizing.

## Relationships

### Conforming Types
- [DefaultWindowToolbarStyle](defaultwindowtoolbarstyle.md)
- [ExpandedWindowToolbarStyle](expandedwindowtoolbarstyle.md)
- [UnifiedCompactWindowToolbarStyle](unifiedcompactwindowtoolbarstyle.md)
- [UnifiedWindowToolbarStyle](unifiedwindowtoolbarstyle.md)

## See Also

- [func toolbarBackground(_:for:)](view/toolbarbackground(_:for:).md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](view/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](view/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func windowToolbarStyle<S>(S) -> some Scene](scene/windowtoolbarstyle(_:).md)
  Sets the style for the toolbar defined within this scene.
- [var toolbarLabelStyle: ToolbarLabelStyle?](environmentvalues/toolbarlabelstyle.md)
  The label style to apply to controls within a toolbar.
- [struct ToolbarLabelStyle](toolbarlabelstyle.md)
  The label style of a toolbar.
- [struct SpacerSizing](spacersizing.md)
  A type which defines how spacers should size themselves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowtoolbarstyle)*