# UIMenu

**Framework**: UIKit  
**Kind**: class

A container for grouping related menu elements in an app menu or contextual menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIMenu
```

#### Overview

Create [`UIMenu`](uimenu.md) objects and use them to construct the menus and submenus your app displays. You provide menus for your app when it runs on macOS, and key command elements in those menus also appear in the discoverability HUD on iPad when someone presses the Command key. You also use menus to display contextual actions in response to specific interactions with one of your views. Every menu has a title, an optional image, and an optional set of child elements. When someone selects an element from the menu, the system executes the code you provide. The code sample below illustrates adding a menu group that contains two menu elements — New and Open — to the File menu.

```swift
// Ensure that the builder is modifying the menu bar system.
guard builder.system == UIMenuSystem.main else { return }

let newDocument = UIKeyCommand(title: "New",
                               action: #selector(newDocument(_:)),
                               input: "n",
                               modifierFlags: .command)

let openDocument = UIKeyCommand(title: "Open...",
                                action: #selector(openDocument(_:)),
                                input: "o",
                                modifierFlags: .command)

// Use the .displayInline option to avoid displaying the menu as a submenu,
// and to separate it from the other menu elements using a line separator.
let newMenu = UIMenu(title: "", options: .displayInline, children: [newDocument, openDocument])

// Insert the menu item at the top of the File menu.
builder.insertChild(newMenu, atStartOfMenu: .file)
```

For examples of how you use [`UIMenu`](uimenu.md), see [`Adding menus and shortcuts to the menu bar and user interface`](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md).

## Topics

### Creating a menu object
- [convenience init(title: String, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](uimenu/init(title:image:identifier:options:children:).md)
  Creates a new menu with the specified values.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](uimenu/init(title:subtitle:image:identifier:options:children:).md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, and child elements.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, preferredElementSize: UIMenu.ElementSize, children: [UIMenuElement])](uimenu/init(title:subtitle:image:identifier:options:preferredelementsize:children:).md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, element size, and child elements.
- [UIMenu.Identifier](uimenu/identifier-swift.struct.md)
  Constants you use to identify an app’s standard menus.
- [UIMenu.Options](uimenu/options-swift.struct.md)
  Options you use to configure a menu’s appearance.
- [init?(coder: NSCoder)](uimenu/init(coder:).md)
  Creates a menu from data in an unarchiver.
### Accessing child elements
- [var children: [UIMenuElement]](uimenu/children.md)
  The contents of the menu.
- [func replacingChildren([UIMenuElement]) -> UIMenu](uimenu/replacingchildren(_:).md)
  Creates a new menu with the same configuration as the current menu, but with a new set of child elements.
### Accessing selected elements
- [var selectedElements: [UIMenuElement]](uimenu/selectedelements.md)
  The elements in the menu and its sub-menus that are in the on state.
### Getting menu details
- [var identifier: UIMenu.Identifier](uimenu/identifier-swift.property.md)
  The unique identifier for the current menu.
- [var options: UIMenu.Options](uimenu/options-swift.property.md)
  The configuration options for the current menu.
### Specifying size of menu elements
- [var preferredElementSize: UIMenu.ElementSize](uimenu/preferredelementsize.md)
  The size of the menu’s child elements.
- [UIMenu.ElementSize](uimenu/elementsize.md)
  Constants that determine the size of an element in a menu.
### Customizing menu display
- [var displayPreferences: UIMenuDisplayPreferences?](uimenu/displaypreferences.md)
  An object that configures how UIKit displays the menu.
- [class UIMenuDisplayPreferences](uimenudisplaypreferences.md)
  An object that contains information for configuring a menu’s display.

## Relationships

### Inherits From
- [UIMenuElement](uimenuelement.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)

## See Also

- [protocol UIMenuBuilder](uimenubuilder.md)
  An interface for adding and removing menus from a menu system.
- [class UIMenuSystem](uimenusystem.md)
  An object representing a main or contextual menu system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu)*