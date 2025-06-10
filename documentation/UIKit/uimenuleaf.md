# UIMenuLeaf

**Framework**: UIKit  
**Kind**: protocol

An interface for an object that represents a menu element without child elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIMenuLeaf : NSObjectProtocol
```

#### Overview

`UIMenuLeaf` defines the behavior shared by menu elements that don’t have child elements. Don’t implement the `UIMenuLeaf` protocol in your object directly. Instead, create an appropriate object that implements this protocol, such as [`UIAction`](uiaction.md) or [`UICommand`](uicommand.md).

## Topics

### Managing the appearance
- [var title: String](uimenuleaf/title.md)
  A short display title for the menu element.
- [var discoverabilityTitle: String?](uimenuleaf/discoverabilitytitle.md)
  A long, informative title to use in the keyboard shortcut overlay.
- [var image: UIImage?](uimenuleaf/image.md)
  An image that appears next to the menu element.
- [var attributes: UIMenuElement.Attributes](uimenuleaf/attributes.md)
  The attributes that determine the style of the menu element.
- [var presentationSourceItem: (any UIPopoverPresentationControllerSourceItem)?](uimenuleaf/presentationsourceitem.md)
  The item you can use as an anchor for subsequent presentations.
### Managing the selection state
- [var state: UIMenuElement.State](uimenuleaf/state.md)
  The menu element’s selection state.
- [var selectedImage: UIImage?](uimenuleaf/selectedimage.md)
  An image that appears next to the menu element when the menu element is in the selected state.
### Performing actions
- [var sender: Any?](uimenuleaf/sender.md)
  The object on behalf of which to perform the menu element’s primary action.
- [func performWithSender(Any?, target: Any?)](uimenuleaf/performwithsender(_:target:).md)
  Performs the element’s primary action.
### Instance Properties
- [var repeatBehavior: UIMenuElement.RepeatBehavior](uimenuleaf/repeatbehavior.md)
  The leaf’s preferred repeat behavior. Menu leaves can repeatedly perform their primary actions on prolonged interactions, such as by holding down their keyboard shortcut.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIAction](uiaction.md)
- [UICommand](uicommand.md)
- [UIKeyCommand](uikeycommand.md)
- [UIWindowScene.ActivationAction](uiwindowscene/activationaction.md)

## See Also

- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](adopting-menus-and-uiactions-in-your-user-interface.md)
  Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [class UIMenuElement](uimenuelement.md)
  An object representing a menu, action, or command.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuleaf)*