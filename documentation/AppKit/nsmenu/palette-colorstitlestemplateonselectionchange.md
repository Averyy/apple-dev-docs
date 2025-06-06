# palette(colors:titles:template:onSelectionChange:)

**Framework**: AppKit  
**Kind**: method

Creates a palette style menu displaying user-selectable color tags that tint using the specified array of colors.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static func palette(colors: [NSColor], titles: [String] = [], template: NSImage? = nil, onSelectionChange: ((NSMenu) -> Void)? = nil) -> NSMenu
```

#### Return Value

A menu in the palette presentation style.

#### Discussion

This factory method creates a presentation style menu as a selectable number of tags that display as colored circles or images. If `templateImage` is `nil`, a solid circle of color displays. If `templateImage` isn’t `nil`, the `templateImage` displays.

This code creates a menu with a group header and a palette menu. The palette menu display a solid circle for each color you pass into the `colors` parameter and adds a checkmark to the middle of the circle when you select the item. You can also optionally pass in a closure that executes when any selection changes.

```swift
let parentMenu = NSMenu()
        
// Create a palette styled menu using the factory method.
let colors: [NSColor] = [.systemRed, .systemOrange, .systemYellow, .systemGreen, .systemBlue]
let titles = ["red", "orange", "yellow", "green", "blue"]
let paletteMenu = NSMenu.palette(colors: colors, titles: titles) { menu in
    // Optionally add a closure to handle any selection changes.
    print("Currently selected colors: \(menu.selectedItems.map { $0.title })")
}

// Create a menu item for the palette and add the palette as a submenu.
let paletteMenuItem = NSMenuItem()
paletteMenuItem.submenu = paletteMenu

// Create a menu and corresponding menu item to contain the palette menu item.
let menu = NSMenu(title: "Colors")
menu.addItem(.sectionHeader(title: "Color Palette Menu"))
menu.addItem(paletteMenuItem)

let menuItem = NSMenuItem()
menuItem.title = "Colors"
menuItem.submenu = menu

// Add the menu containing the palette to the parent menu.
parentMenu.addItem(menuItem)
```

![A presentation style menu with five solid colored circles of various colors that display horizontally left to right. The first two circles have checkmarks in the middle.](https://docs-assets.developer.apple.com/published/1f23b72d94db32f4efc69882003da882/media-4304328%402x.png)

This code is similar to the previous example, only here the menu displays the `templateImage` of a flag tinted to the corresponding color you set in the `colors` array. When you select an item in this menu the image changes from a flag to a checkmark.

```swift
let parentMenu = NSMenu()
        
// Create a palette styled menu using the factory method.
let colors: [NSColor] = [.systemRed, .systemOrange, .systemYellow, .systemGreen, .systemBlue]
let titles = ["red", "orange", "yellow", "green", "blue"]
let template = NSImage(systemSymbolName: "flag.fill", accessibilityDescription: "flag")
let paletteMenu = NSMenu.palette(colors: colors, titles: titles, template: template) { menu in
    // Optionally add a closure to handle any selection changes.
    print("Currently selected flag colors: \(menu.selectedItems.map { $0.title })")
}

// Create a menu item for the palette and add the palette as a submenu.
let paletteMenuItem = NSMenuItem()
paletteMenuItem.submenu = paletteMenu

// Create a menu and corresponding menu item to contain the palette menu item.
let menu = NSMenu(title: "Flags")
menu.addItem(.sectionHeader(title: "Flags Palette Menu"))
menu.addItem(paletteMenuItem)

let menuItem = NSMenuItem()
menuItem.title = "Flags"
menuItem.submenu = menu

// Add the menu containing the palette to the parent menu.
parentMenu.addItem(menuItem)
```

![A presentation style menu showing two checkmarks and three flags of various colors that display horizontally left to right.](https://docs-assets.developer.apple.com/published/33abeeccf164cbe50f7bcf312810f72a/media-4304329%402x.png)

When setting the `template` image favor images that tint (such as system images). Raster images don’t tint in this presentation style.

Menus that you create using this convenience method have a [`presentationStyle`](nsmenu/presentationstyle-swift.property.md) of type [`NSMenu.PresentationStyle.palette`](nsmenu/presentationstyle-swift.enum/palette.md) and a [`selectionMode`](nsmenu/selectionmode-swift.property.md) of type [`NSMenu.SelectionMode.selectAny`](nsmenu/selectionmode-swift.enum/selectany.md).

## Parameters

- `colors`: The display colors for the menu items.
- `titles`: The menu item titles.
- `template`: The image the system displays for the menu items.
- `onSelectionChange`: The closure to invoke when someone selects the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/palette(colors:titles:template:onselectionchange:))*