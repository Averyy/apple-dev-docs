# UIMenuElement.State

**Framework**: UIKit  
**Kind**: enum

Constants that indicate the state of an action- or command-based menu element.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum State
```

## Topics

### States
- [UIMenuElement.State.off](uimenuelement/state/off.md)
  A constant indicating the menu element is in the “off” state.
- [UIMenuElement.State.on](uimenuelement/state/on.md)
  A constant indicating the menu element is in the “on” state.
- [UIMenuElement.State.mixed](uimenuelement/state/mixed.md)
  A constant indicating the menu element is in the “mixed” state.
### Initializers
- [init?(rawValue: Int)](uimenuelement/state/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [protocol UIMenuLeaf](uimenuleaf.md)
  An interface for an object that represents a menu element without child elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement/state)*