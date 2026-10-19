# init(id:)

**Framework**: SwiftUI  
**Kind**: init

Creates a custom accessory bar placement.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init<ID>(id: ID) where ID : Hashable
```

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
- [static var windowToolbar: ToolbarPlacement](toolbarplacement/windowtoolbar.md)
  The placement for the containing window’s toolbar, sometimes referred to as the titlebar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarplacement/init(id:))*