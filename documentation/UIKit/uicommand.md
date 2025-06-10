# UICommand

**Framework**: UIKit  
**Kind**: class

A menu element that performs its action in a selector.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICommand
```

#### Overview

Create a [`UICommand`](uicommand.md) object when you want a menu element that performs its action in a selector available in the responder chain.

```swift
// Create a selector-based action to use as a menu element.
let refreshCommand = UICommand(title: "Refresh", action: #selector(refreshData(_:)))

// Use the .displayInline option to avoid displaying the menu as a submenu,
// and to separate it from the other menu elements using a line separator.
let refreshMenuItem = UIMenu(title: "", options: .displayInline, children: [refreshCommand])

// Insert the menu into the File menu before the Close menu.
builder.insertSibling(refreshMenuItem, beforeMenu: .close)
```

## Topics

### Creating a command
- [convenience init(title: String, subtitle: String?, image: UIImage?, action: Selector, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](uicommand/init(title:subtitle:image:action:propertylist:alternates:discoverabilitytitle:attributes:state:).md)
  Creates a command with the specified title, subtitle, image, action, property list, alternative commands, discoverability title, attributes, and state.
- [convenience init(title: String, image: UIImage?, action: Selector, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](uicommand/init(title:image:action:propertylist:alternates:discoverabilitytitle:attributes:state:).md)
  Creates a command with the specified title, image, action, property list, alternative commands, discoverability title, attributes, and state.
- [init?(coder: NSCoder)](uicommand/init(coder:).md)
  Creates a command from data in an unarchiver.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
### Getting information about the command
- [var title: String](uicommand/title.md)
  The command’s title.
- [var image: UIImage?](uicommand/image.md)
  The command’s image.
- [var action: Selector](uicommand/action.md)
  The selector identifying the action method called after the user selects the command.
- [var discoverabilityTitle: String?](uicommand/discoverabilitytitle.md)
  An elaborated title that explains the purpose of the command.
- [var attributes: UIMenuElement.Attributes](uicommand/attributes.md)
  The attributes indicating the style of the command.
- [var state: UIMenuElement.State](uicommand/state.md)
  The state of the command.
### Getting command alternatives
- [var alternates: [UICommandAlternate]](uicommand/alternates.md)
  An array of alternative actions to take for the command.
- [class UICommandAlternate](uicommandalternate.md)
  An object representing an alternative action for a command.
### Associating data
- [var propertyList: Any?](uicommand/propertylist.md)
  An object that contains data to associate with the command.
- [let UICommandTagShare: String](uicommandtagshare.md)
  A value that identifies a command as a Share menu.
### Initializers
- [convenience init(title: String, subtitle: String?, image: UIImage?, selectedImage: UIImage?, action: Selector, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](uicommand/init(title:subtitle:image:selectedimage:action:propertylist:alternates:discoverabilitytitle:attributes:state:).md)

## Relationships

### Inherits From
- [UIMenuElement](uimenuelement.md)
### Inherited By
- [UIKeyCommand](uikeycommand.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIMenuLeaf](uimenuleaf.md)

## See Also

- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](adopting-menus-and-uiactions-in-your-user-interface.md)
  Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [class UIMenuElement](uimenuelement.md)
  An object representing a menu, action, or command.
- [class UIAction](uiaction.md)
  A menu element that performs its action in a closure.
- [class UIKeyCommand](uikeycommand.md)
  An object that specifies a key press perform on a hardware keyboard and the resulting action.
- [class UIDeferredMenuElement](uideferredmenuelement.md)
  A placeholder menu element that the system replaces with the result of the block’s completion handler.
- [UIDeferredMenuElement.Provider](uideferredmenuelement/provider.md)
- [UIMenuElement.Attributes](uimenuelement/attributes.md)
  Attributes that determine the style of the menu element.
- [UIMenuElement.State](uimenuelement/state.md)
  Constants that indicate the state of an action- or command-based menu element.
- [protocol UIMenuLeaf](uimenuleaf.md)
  An interface for an object that represents a menu element without child elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommand)*