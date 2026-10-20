# windowToolbar

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The placement for the containing window’s toolbar, sometimes referred to as the titlebar.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static var windowToolbar: ToolbarPlacement { get }
```

#### Discussion

When hidden using [`toolbarVisibility(_:for:)`](../view/toolbarvisibility%28_,for%29.md), this hides the entire window toolbar, including the title and “traffic light” window controls. To remove the custom toolbar item content only, use [`automatic`](./automatic.md).

Use [`toolbarBackground(_:for:)`](../view/toolbarbackground%28_,for%29.md) to hide the background of the window toolbar.

## See Also

### Getting placements
- [static var automatic: ToolbarPlacement](./automatic.md)
  The primary toolbar.
- [static func accessoryBar<ID>(id: ID) -> ToolbarPlacement](./accessorybar%28id%29.md)
  Creates a unique accessory bar placement.
- [static var bottomBar: ToolbarPlacement](./bottombar.md)
  The bottom toolbar of an app.
- [static var bottomOrnament: ToolbarPlacement](./bottomornament.md)
  The bottom ornament of an app.
- [static var navigationBar: ToolbarPlacement](./navigationbar.md)
  The navigation bar of an app.
- [static var tabBar: ToolbarPlacement](./tabbar.md)
  The tab bar of an app.
- [init<ID>(id: ID)](./init%28id%29.md)
  Creates a custom accessory bar placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarplacement/windowtoolbar)*