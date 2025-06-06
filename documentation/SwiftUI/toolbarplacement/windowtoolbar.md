# windowToolbar

**Framework**: SwiftUI  
**Kind**: property

The placement for the containing window’s toolbar, sometimes referred to as the titlebar.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static var windowToolbar: ToolbarPlacement { get }
```

#### Discussion

When hidden using [`toolbar(_:for:)`](view/toolbar(_:for:).md), this hides the entire window toolbar, including the title and “traffic light” window controls. To remove the custom toolbar item content only, use [`automatic`](toolbarplacement/automatic.md).

Use [`toolbarBackground(_:for:)`](view/toolbarbackground(_:for:).md) to hide the background of the window toolbar.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarplacement/windowtoolbar)*