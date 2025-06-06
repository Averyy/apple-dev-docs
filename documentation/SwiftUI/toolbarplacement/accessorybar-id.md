# accessoryBar(id:)

**Framework**: SwiftUI  
**Kind**: method

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

Use a custom placement to control the appearance of the containing bar for items using a custom [`ToolbarItemPlacement`](toolbaritemplacement.md) with the same identifier.

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

- [static var automatic: ToolbarPlacement](toolbarplacement/automatic.md)
  The primary toolbar.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarplacement/accessorybar(id:))*