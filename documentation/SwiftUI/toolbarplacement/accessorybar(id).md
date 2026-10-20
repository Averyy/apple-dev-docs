# accessoryBar(id:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a unique accessory bar placement.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@backDeployed(before: macOS 14.0)
static func accessoryBar<ID>(id: ID) -> ToolbarPlacement where ID : Hashable
```

#### Discussion

On macOS, accessory bars are in a section below the title bar and toolbar area of the window. Each separate identifier will correspond to a separate accessory bar that is added to this area.

Use a custom placement to control the appearance of the containing bar for items using a custom [`ToolbarItemPlacement`](../toolbaritemplacement.md) with the same identifier.

```swift
private let favoritesBarID = "com.example.favoritesBar"
extension ToolbarItemPlacement {
    static let favoritesBar = accessoryBar(id: favoritesBarID)
}
extension ToolbarPlacement {
    static let favoritesBar = accessoryBar(id: favoritesBarID)
}
...
BrowserView()
    .toolbar {
        ToolbarItem(placement: .favoritesBar) {
            FavoritesBar()
        }
    }
    .toolbar(.hidden, for: .favoritesBar)
```

## Parameters

- `id`: A unique identifier for this placement.

## See Also

### Getting placements
- [static var automatic: ToolbarPlacement](./automatic.md)
  The primary toolbar.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarplacement/accessorybar(id:))*