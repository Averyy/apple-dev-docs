# contextMenu(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a context menu to the view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 7.0

> **Deprecated**: Use [`contextMenu(menuItems:)`](./contextmenu%28menuitems%29.md) instead.

## Declaration

```swift
nonisolated
func contextMenu<MenuItems>(_ contextMenu: ContextMenu<MenuItems>?) -> some View where MenuItems : View
```

## Return Value

A view that can show a context menu.

## Discussion

Use this method to attach a specified context menu to a view. You can make the context menu unavailable by conditionally passing `nil` as the value for the `contextMenu`.

The example below creates a [`ContextMenu`](../contextmenu.md) that contains two items and passes them into the modifier. The Boolean value `shouldShowMenu`, which defaults to `true`, controls the context menu availability:

```swift
private let menuItems = ContextMenu {
    Button {
        // Add this item to a list of favorites.
    } label: {
        Label("Add to Favorites", systemImage: "heart")
    }
    Button {
        // Open Maps and center it on this item.
    } label: {
        Label("Show in Maps", systemImage: "mappin")
    }
}

private struct ContextMenuMenuItems: View {
    @State private var shouldShowMenu = true

    var body: some View {
        Text("Turtle Rock")
            .contextMenu(shouldShowMenu ? menuItems : nil)
    }
}
```

![A screenshot of a context menu showing two menu items: Add to Favorites, and Show in Maps.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-contextMenu-1-iOS@2x.png)

## Parameters

- `contextMenu`: A context menu container for views that you present as menu items in a context menu.

## See Also

### Auxiliary view modifiers
- [func navigationBarTitle(_:)](./navigationbartitle%28_%29.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(_:displayMode:)](./navigationbartitle%28_,displaymode%29.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](./navigationbaritems%28leading%29.md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](./navigationbaritems%28leading,trailing%29.md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<T>(trailing: T) -> some View](./navigationbaritems%28trailing%29.md)
  Configures the navigation bar items for this view.
- [func navigationBarHidden(Bool) -> some View](./navigationbarhidden%28_%29.md)
  Hides the navigation bar for this view.
- [func statusBar(hidden: Bool) -> some View](./statusbar%28hidden%29.md)
  Sets the visibility of the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/contextmenu(_:))*