# SpacerSizing

**Framework**: SwiftUI  
**Kind**: struct

A type which defines how spacers should size themselves.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
struct SpacerSizing
```

#### Overview

Use this type in coordination with the [`ToolbarSpacer`](toolbarspacer.md) type to define if the spacer should be a flexible size, or a fixed size using system-defined sizing rules.

For example, the following adds a fixed-size toolbar spacer between the share and more buttons in the toolbar:

```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") {
           TagButton()
        }
        ToolbarItem(id: "share") {
           ShareButton()
        }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") {
           MoreButton()
        }
    }
```

## Topics

### Type Properties
- [static let fixed: SpacerSizing](spacersizing/fixed.md)
  The fixed spacer sizing behavior. The spacer will use a pre-defined size determined by the system and the context in which the spacer is used.
- [static let flexible: SpacerSizing](spacersizing/flexible.md)
  The flexible spacer sizing behavior. The spacer will expand to accommodate as much space as it is given in the current context.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var toolbarLabelStyle: ToolbarLabelStyle?](environmentvalues/toolbarlabelstyle.md)
  The label style to apply to controls within a toolbar.
- [struct ToolbarLabelStyle](toolbarlabelstyle.md)
  The label style of a toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spacersizing)*