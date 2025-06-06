# accessoryBar(id:)

**Framework**: SwiftUI  
**Kind**: method

Creates a unique accessory bar placement.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@backDeployed(before: macOS 14.0)
static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement where ID : Hashable
```

#### Discussion

On macOS, items with an accessory bar placement are placed in a section below the title bar and toolbar area of the window. Each separate identifier will correspond to a separate accessory bar that is added to this area.

```swift
extension ToolbarItemPlacement {
    static let favoritesBar = accessoryBar(id: "com.example.favorites")
}
...
BrowserView()
    .toolbar {
        ToolbarItem(placement: .favoritesBar) {
            FavoritesBar()
        }
    }
```

## Parameters

- `id`: A unique identifier for this placement.

## See Also

- [static var topBarLeading: ToolbarItemPlacement](toolbaritemplacement/topbarleading.md)
  Places the item in the leading edge of the top bar.
- [static var topBarTrailing: ToolbarItemPlacement](toolbaritemplacement/topbartrailing.md)
  Places the item in the trailing edge of the top bar.
- [static let bottomBar: ToolbarItemPlacement](toolbaritemplacement/bottombar.md)
  Places the item in the bottom toolbar.
- [static let bottomOrnament: ToolbarItemPlacement](toolbaritemplacement/bottomornament.md)
  Places the item in an ornament under the window.
- [static let keyboard: ToolbarItemPlacement](toolbaritemplacement/keyboard.md)
  The item is placed in the keyboard section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/accessorybar(id:))*