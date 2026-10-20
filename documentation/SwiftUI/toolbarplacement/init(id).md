# init(id:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a custom accessory bar placement.

**Availability**:
- macOS 13.0+ - Deprecated in 14.0 (renamed: accessoryBar)

> **Deprecated**: Use [`init(id:)`](./init%28id%29.md) instead.

## Declaration

```swift
init<ID>(id: ID) where ID : Hashable
```

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
- [static var windowToolbar: ToolbarPlacement](./windowtoolbar.md)
  The placement for the containing window’s toolbar, sometimes referred to as the titlebar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarplacement/init(id:))*