# contextMenu(menuItems:)

**Framework**: SwiftUI  
**Kind**: method

Adds a context menu to a view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func contextMenu<MenuItems>(@ViewBuilder menuItems: () -> MenuItems) -> some View where MenuItems : View
```

#### Return Value

A view that can display a context menu.

#### Discussion

Use this modifier to add a context menu to a view in your app’s user interface. Compose the menu by returning controls like [`Button`](button.md), [`Toggle`](toggle.md), and [`Picker`](picker.md) from the `menuItems` closure. You can also use [`Menu`](menu.md) to define submenus or [`Section`](section.md) to group items.

The following example creates a [`Text`](text.md) view that has a context menu with two buttons:

```swift
Text("Turtle Rock")
    .padding()
    .contextMenu {
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
```

When someone activates the context menu with an action like touch and hold in iOS or iPadOS, the system displays the menu next to the content:

![A screenshot of a context menu showing two menu items: Add to](https://docs-assets.developer.apple.com/published/175048e4c43b6463112139fd1c3f69c8/View-contextMenu-1-iOS%402x.png)

The system dismisses the menu if someone makes a selection, or taps or clicks outside the menu.

To customize the default preview, apply a [`contentShape(_:_:eoFill:)`](view/contentshape(_:_:eofill:).md) with a [`contextMenuPreview`](contentshapekinds/contextmenupreview.md) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

> **Note**: This view modifier produces a context menu on macOS, but that platform doesn’t display a preview.

If you want to show a different preview, you can use [`contextMenu(menuItems:preview:)`](view/contextmenu(menuitems:preview:).md). To add a context menu to a container that supports selection, like a [`List`](list.md) or a [`Table`](table.md), and to distinguish between menu activation on a selection and activation in an empty area of the container, use [`contextMenu(forSelectionType:menu:primaryAction:)`](view/contextmenu(forselectiontype:menu:primaryaction:).md).

## Parameters

- `menuItems`: A closure that produces the menu’s contents. You   can deactivate the context menu by returning nothing from the closure.

## See Also

- [func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View](view/contextmenu(menuitems:preview:).md)
  Adds a context menu with a custom preview to a view.
- [func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M, primaryAction: ((Set<I>) -> Void)?) -> some View](view/contextmenu(forselectiontype:menu:primaryaction:).md)
  Adds an item-based context menu to a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/contextmenu(menuitems:))*