# ContextMenu

**Framework**: SwiftUI  
**Kind**: struct

A container for views that you present as menu items in a context menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct ContextMenu<MenuItems> where MenuItems : View
```

#### Overview

A context menu view allows you to present a situationally specific menu that enables taking actions relevant to the current task.

You can create a context menu by first defining a `ContextMenu` container with the controls that represent the actions people can take, and then using the [`contextMenu(_:)`](view/contextmenu(_:).md) view modifier to apply the menu to a view.

The example below creates and applies a two item context menu container to a [`Text`](text.md) view. The Boolean value `shouldShowMenu`, which defaults to true, controls the availability of context menu:

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

![A screenshot of a context menu showing two menu items: Add to Favorites, and Show in Maps.](https://docs-assets.developer.apple.com/published/175048e4c43b6463112139fd1c3f69c8/View-contextMenu-1-iOS%402x.png)

## Topics

### Creating a context menu
- [init(menuItems: () -> MenuItems)](contextmenu/init(menuitems:).md)
  Creates a context menu.

## See Also

- [struct MenuButton](menubutton.md)
  A button that displays a menu containing a list of choices when pressed.
- [typealias PullDownButton](pulldownbutton.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contextmenu)*