# NSMenu.PresentationStyle.palette

**Framework**: AppKit  
**Kind**: case

A menu presentation style where items to display align horizontally.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case palette
```

#### Discussion

You can turn any menu into a palette menu by setting the menu’s presentation style to `.palette`. For each menu item, set its image. For template images, AppKit automatically adds the appropriate selection tint. Alternatively you can set the [`offStateImage`](nsmenuitem/offstateimage.md) and the [`onStateImage`](nsmenuitem/onstateimage.md). Use the `onStateImage` to indicate selection.

The following example creates a presentation style menu that displays a list of sport images. When a menu item selects, the system automatically tints the image.

![A palette style menu that expands to the right from a selected sports menu item listing a series of sport images horizonally. The second item in the list is tinted indicating selection.](https://docs-assets.developer.apple.com/published/8563e34565a1851e905ce287868a8bb1/media-4304532%402x.png)

**Swift**:

```swift
let parentMenu = NSMenu()

// Create a menu.
let paletteMenu = NSMenu()
let symbols = ["figure.barre", "figure.american.football", "figure.soccer", "figure.fishing", "figure.roll"]
for symbol in symbols {
    let item = NSMenuItem(title: symbol, action: nil, keyEquivalent: "")
    item.image = NSImage(systemSymbolName: symbol, accessibilityDescription: symbol)
    paletteMenu.addItem(item)
}

// Set the presentation style of the menu to palette.
paletteMenu.presentationStyle = .palette

// Create a menu item for the palette.
let paletteMenuItem = NSMenuItem()
paletteMenuItem.submenu = paletteMenu

// Create a menu and corresponding menu item to contain the palette menu item.
let menu = NSMenu(title: "Sports")
menu.addItem(.sectionHeader(title: "Sports Menu"))
menu.addItem(paletteMenuItem)

let menuItem = NSMenuItem()
menuItem.title = "Sports"
menuItem.submenu = menu

// Add the menu containing the palette to the parent menu.
parentMenu.addItem(menuItem)
```

**Objective-C**:

```objc
NSMenu *parentMenu = [[NSMenu alloc] init];

// Create a menu.
NSMenu *paletteMenu = [[NSMenu alloc] init];
NSArray *symbols = @[@"figure.barre", @"figure.american.football", @"figure.soccer", @"figure.fishing", @"figure.roll"];
int index;
for(NSInteger index = 0; index < symbols.count; index++) {
    NSString *symbol = symbols[index];
    NSMenuItem *item = [[NSMenuItem alloc] initWithTitle:symbol action:nil keyEquivalent:@""];
    item.image = [NSImage imageWithSystemSymbolName:symbol accessibilityDescription:@""];
    [paletteMenu addItem:item];
}

// Set the presentation style of the menu to palette.
paletteMenu.presentationStyle = NSMenuPresentationStylePalette;

// Create a menu item for the palette.
NSMenuItem *paletteMenuItem = [[NSMenuItem alloc] init];
paletteMenuItem.submenu = paletteMenu;

// Create a menu and corresponding menu item to contain the palette menu item.
NSMenu *menu = [[NSMenu alloc] initWithTitle:@"Sports"];
[menu addItem:[NSMenuItem sectionHeaderWithTitle:@"Sports Menu"]];
[menu addItem:paletteMenuItem];

NSMenuItem *menuItem = [[NSMenuItem alloc] init];
menuItem.title = @"Sports";
menuItem.submenu = menu;

// Add the menu containing the palette to the parent menu.
[parentMenu addItem:menuItem];
```

## See Also

- [NSMenu.PresentationStyle.regular](nsmenu/presentationstyle-swift.enum/regular.md)
  The default presentation style for a menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/presentationstyle-swift.enum/palette)*