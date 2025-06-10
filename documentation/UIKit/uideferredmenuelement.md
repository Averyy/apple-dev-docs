# UIDeferredMenuElement

**Framework**: UIKit  
**Kind**: class

A placeholder menu element that the system replaces with the result of the block’s completion handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDeferredMenuElement
```

## Topics

### Creating a deferred menu element
- [convenience init((([UIMenuElement]) -> Void) -> Void)](uideferredmenuelement/init(_:).md)
  A convenience initializer that creates a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [class func uncached((([UIMenuElement]) -> Void) -> Void) -> Self](uideferredmenuelement/uncached(_:).md)
  Returns a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [class func usingFocus(identifier: UIDeferredMenuElement.Identifier, shouldCacheItems: Bool) -> Self](uideferredmenuelement/usingfocus(identifier:shouldcacheitems:).md)
### Setting an identifier
- [var identifier: UIDeferredMenuElement.Identifier](uideferredmenuelement/identifier-swift.property.md)
  The identifier of this deferred menu element.
- [UIDeferredMenuElement.Identifier](uideferredmenuelement/identifier-swift.struct.md)

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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)

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
- [UIDeferredMenuElement.Provider](uideferredmenuelement/provider.md)
- [UIMenuElement.Attributes](uimenuelement/attributes.md)
  Attributes that determine the style of the menu element.
- [UIMenuElement.State](uimenuelement/state.md)
  Constants that indicate the state of an action- or command-based menu element.
- [protocol UIMenuLeaf](uimenuleaf.md)
  An interface for an object that represents a menu element without child elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uideferredmenuelement)*