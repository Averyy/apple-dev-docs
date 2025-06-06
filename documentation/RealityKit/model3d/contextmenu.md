# contextMenu(_:)

**Framework**: RealityKit  
**Kind**: method

Adds a context menu to the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func contextMenu<MenuItems>(_ contextMenu: ContextMenu<MenuItems>?) -> some View where MenuItems : View
```

#### Return Value

A view that can show a context menu.

#### Discussion

Use this method to attach a specified context menu to a view. You can make the context menu unavailable by conditionally passing `nil` as the value for the `contextMenu`.

The example below creates a `ContextMenu` that contains two items and passes them into the modifier. The Boolean value `shouldShowMenu`, which defaults to `true`, controls the context menu availability:

```None
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

To customize the default preview, apply a `View/contentShape(_:_:eoFill:)` with a `ContentShapeKinds/contextMenuPreview` kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

## Parameters

- `contextMenu`: A context menu container for views that you   present as menu items in a context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/contextmenu(_:))*