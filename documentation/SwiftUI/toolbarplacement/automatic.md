# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The primary toolbar.

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
static var automatic: ToolbarPlacement { get }
```

## Discussion

Depending on the context, this may refer to the navigation bar of an app on iOS, or watchOS, the tab bar of an app on tvOS, or the window toolbar / window titlebar of an app on macOS.

## See Also

### Getting placements
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
- [init<ID>(id: ID)](./init%28id%29.md)
  Creates a custom accessory bar placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarplacement/automatic)*