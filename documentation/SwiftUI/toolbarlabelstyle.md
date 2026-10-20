# ToolbarLabelStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The label style of a toolbar.

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
struct ToolbarLabelStyle
```

#### Overview

Use this type in conjunction with modifiers like [`windowToolbarLabelStyle(fixed:)`](./scene/windowtoolbarlabelstyle%28fixed%29.md) and [`windowToolbarLabelStyle(_:)`](./scene/windowtoolbarlabelstyle%28_%29.md) to customize the appearance of window toolbars managed by SwiftUI.

## Topics

### Type Properties
- [static var automatic: ToolbarLabelStyle](./toolbarlabelstyle/automatic.md)
  The automatic label style. The toolbar will use a labelStyle that best fits the `Scene` it is applied to.
- [static var iconOnly: ToolbarLabelStyle](./toolbarlabelstyle/icononly.md)
  The icon only label style. The toolbar contents will only display the control
- [static var titleAndIcon: ToolbarLabelStyle](./toolbarlabelstyle/titleandicon.md)
  The title and icon label style. The toolbar contents will display both a control and title
- [static var titleOnly: ToolbarLabelStyle](./toolbarlabelstyle/titleonly.md)
  The title only label style. The toolbar contents will only display the title

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Styling a toolbar
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](./view/toolbarcolorscheme%28_,for%29.md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](./view/toolbarforegroundstyle%28_,for%29.md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func windowToolbarStyle<S>(S) -> some Scene](./scene/windowtoolbarstyle%28_%29.md)
  Sets the style for the toolbar defined within this scene.
- [protocol WindowToolbarStyle](./windowtoolbarstyle.md)
  A specification for the appearance and behavior of a window’s toolbar.
- [var toolbarLabelStyle: ToolbarLabelStyle?](./environmentvalues/toolbarlabelstyle.md)
  The label style to apply to controls within a toolbar.
- [struct SpacerSizing](./spacersizing.md)
  A type which defines how spacers should size themselves.
- [func toolbarBackground(_:for:)](./view/toolbarbackground%28_,for%29.md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarlabelstyle)*