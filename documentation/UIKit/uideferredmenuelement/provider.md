# UIDeferredMenuElement.Provider

**Framework**: UIKit  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
class Provider
```

#### Overview

```None
      When the containing menu for a responder-based deferred element is presented, the system asks the
      responder chain for one of these element providers for the deferred element.
```

## Topics

### Initializers
- [convenience init((([UIMenuElement]) -> Void) -> Void)](uideferredmenuelement/provider/init(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

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
- [UIMenuElement.Attributes](uimenuelement/attributes.md)
  Attributes that determine the style of the menu element.
- [UIMenuElement.State](uimenuelement/state.md)
  Constants that indicate the state of an action- or command-based menu element.
- [protocol UIMenuLeaf](uimenuleaf.md)
  An interface for an object that represents a menu element without child elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uideferredmenuelement/provider)*