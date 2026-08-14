# UIMenuElement

**Framework**: UIKit  
**Kind**: class

An object representing a menu, action, or command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIMenuElement
```

#### Overview

[`UIMenuElement`](uimenuelement.md) defines the behavior shared by all menus, actions, and commands. You don’t create [`UIMenuElement`](uimenuelement.md) objects directly. Instead, you create an appropriate object that inherits from this class, such as [`UIMenu`](uimenu.md), [`UIAction`](uiaction.md), or [`UICommand`](uicommand.md).

## Topics

### Getting the element attributes
- [var title: String](uimenuelement/title.md)
  The title of the menu element.
- [var subtitle: String?](uimenuelement/subtitle.md)
  The subtitle to display alongside the menu element’s title.
- [var image: UIImage?](uimenuelement/image.md)
  The image to display alongside the menu element’s title.
### Creating a menu element
- [init?(coder: NSCoder)](uimenuelement/init(coder:).md)
  Creates a menu element from data in an unarchiver.
### Constants
- [UIMenuElement.Attributes](uimenuelement/attributes.md)
  Attributes that determine the style of the menu element.
- [UIMenuElement.State](uimenuelement/state.md)
  Constants that indicate the state of an action- or command-based menu element.
- [UIMenuElement.RepeatBehavior](uimenuelement/repeatbehavior.md)
  Possible repeat behaviors for a menu element.
### Instance Properties
- [var highlightStateUpdateHandler: ((UIMenuElement, Bool) -> Void)?](uimenuelement/highlightstateupdatehandler.md)
  A closure the system calls when the element’s highlight state changes in a menu.
- [var preferredImageVisibility: UIMenuElement.ImageVisibility](uimenuelement/preferredimagevisibility.md)
  The preferred visibility of the element’s image.
### Enumerations
- [UIMenuElement.ImageVisibility](uimenuelement/imagevisibility.md)
  Visibility options for a menu element’s image.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [UIAction](uiaction.md)
- [UICommand](uicommand.md)
- [UIDeferredMenuElement](uideferredmenuelement.md)
- [UIMenu](uimenu.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)

## See Also

- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](adopting-menus-and-uiactions-in-your-user-interface.md)
  Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [class UIAction](uiaction.md)
  A menu element that performs its action in a closure.
- [class UICommand](uicommand.md)
  A menu element that performs its action in a selector.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement)*