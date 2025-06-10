# ToolbarPlacement

**Framework**: SwiftUI  
**Kind**: struct

The placement of a toolbar.

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
struct ToolbarPlacement
```

#### Overview

Use this type in conjunction with modifiers like [`toolbarBackground(_:for:)`](view/toolbarbackground(_:for:).md) and [`toolbar(_:for:)`](view/toolbar(_:for:).md) to customize the appearance of different bars managed by SwiftUI. Not all bars support all types of customizations.

See [`ToolbarItemPlacement`](toolbaritemplacement.md) to learn about the different regions of these toolbars that you can place your own controls into.

## Topics

### Getting placements
- [static var automatic: ToolbarPlacement](toolbarplacement/automatic.md)
  The primary toolbar.
- [static func accessoryBar<ID>(id: ID) -> ToolbarPlacement](toolbarplacement/accessorybar(id:).md)
  Creates a unique accessory bar placement.
- [static var bottomBar: ToolbarPlacement](toolbarplacement/bottombar.md)
  The bottom toolbar of an app.
- [static var bottomOrnament: ToolbarPlacement](toolbarplacement/bottomornament.md)
  The bottom ornament of an app.
- [static var navigationBar: ToolbarPlacement](toolbarplacement/navigationbar.md)
  The navigation bar of an app.
- [static var tabBar: ToolbarPlacement](toolbarplacement/tabbar.md)
  The tab bar of an app.
- [static var windowToolbar: ToolbarPlacement](toolbarplacement/windowtoolbar.md)
  The placement for the containing window’s toolbar, sometimes referred to as the titlebar.
### Deprecated symbols
- [init<ID>(id: ID)](toolbarplacement/init(id:).md)
  Creates a custom accessory bar placement.

## See Also

- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](view/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [struct ContentToolbarPlacement](contenttoolbarplacement.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarplacement)*