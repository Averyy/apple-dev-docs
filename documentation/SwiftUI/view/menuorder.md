# menuOrder(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the preferred order of items for menus presented from this view.

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
nonisolated
func menuOrder(_ order: MenuOrder) -> some View
```

#### Return Value

A view that uses the specified menu ordering strategy.

#### Discussion

Use this modifier to override the default menu order. On supported platforms, [`priority`](menuorder/priority.md) order keeps the first items closer to the user’s point of interaction, whereas [`fixed`](menuorder/fixed.md) order always orders items from top to bottom.

On iOS, the [`automatic`](menuorder/automatic.md) order resolves to [`fixed`](menuorder/fixed.md) for menus presented within scrollable content. Pickers that use the [`menu`](pickerstyle/menu.md) style also default to [`fixed`](menuorder/fixed.md) order. In all other cases, menus default to [`priority`](menuorder/priority.md) order.

On macOS, tvOS and watchOS, the [`automatic`](menuorder/automatic.md) order always resolves to [`fixed`](menuorder/fixed.md) order.

The following example creates a menu that presents its content in a fixed order from top to bottom:

```swift
Menu {
    Button("Select", action: selectFolders)
    Button("New Folder", action: createFolder)
    Picker("Appearance", selection: $appearance) {
        Label("Icons", systemImage: "square.grid.2x2").tag(Appearance.icons)
        Label("List", systemImage: "list.bullet").tag(Appearance.list)
    }
} label: {
    Label("Settings", systemImage: "ellipsis.circle")
}
.menuOrder(.fixed)
```

You can use this modifier on controls that present a menu. For example, the code below creates a [`Picker`](picker.md) using the [`menu`](pickerstyle/menu.md) style with a priority-based order:

```swift
Picker("Flavor", selection: $selectedFlavor) {
    Text("Chocolate").tag(Flavor.chocolate)
    Text("Vanilla").tag(Flavor.vanilla)
    Text("Strawberry").tag(Flavor.strawberry)
}
.pickerStyle(.menu)
.menuOrder(.priority)
```

You can also use this modifier on context menus. The example below creates a context menu that presents its content in a fixed order:

```swift
Text("Favorite Card Suit")
    .padding()
    .contextMenu {
        Button("♥️ - Hearts", action: selectHearts)
        Button("♣️ - Clubs", action: selectClubs)
        Button("♠️ - Spades", action: selectSpades)
        Button("♦️ - Diamonds", action: selectDiamonds)
    }
    .menuOrder(.fixed)
```

The modifier has no effect when applied to a subsection or submenu of a menu.

## Parameters

- `order`: The menu item ordering strategy to apply.

## See Also

- [var menuOrder: MenuOrder](environmentvalues/menuorder.md)
  The preferred order of items for menus presented from this view.
- [struct MenuOrder](menuorder.md)
  The order in which a menu presents its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/menuorder(_:))*