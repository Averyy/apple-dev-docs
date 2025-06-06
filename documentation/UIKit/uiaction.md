# UIAction

**Framework**: UIKit  
**Kind**: class

A menu element that performs its action in a closure.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAction
```

#### Overview

Create a [`UIAction`](uiaction.md) object when you want a menu element that performs its action in a closure. The following example adds an action-based menu to the File menu:

```swift
// Create a closure-based action to use as a menu element.
let refreshAction = UIAction(title: "Refresh") { (action) in
    print("Refresh the data.")
}

// Use the .displayInline option to avoid displaying the menu as a submenu,
// and to separate it from the other menu elements using a line separator.
let refreshMenuItem = UIMenu(title: "", options: .displayInline, children: [refreshAction])

// Insert the menu into the File menu before the Close menu.
builder.insertSibling(refreshMenuItem, beforeMenu: .close)
```

## Topics

### Creating an action
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](uiaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:state:handler:).md)
  Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.
- [convenience init(title: String, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](uiaction/init(title:image:identifier:discoverabilitytitle:attributes:state:handler:).md)
  Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [class func captureTextFromCamera(responder: any UIResponder & UIKeyInput, identifier: UIAction.Identifier?) -> Self](uiaction/capturetextfromcamera(responder:identifier:).md)
  Creates an action for capturing text using the device’s camera.
- [UIAction.Identifier](uiaction/identifier-swift.struct.md)
  A type that represents an action identifier.
- [typealias UIActionHandler](uiactionhandler.md)
  A type that defines the closure for an action handler.
### Getting information about the action
- [var title: String](uiaction/title.md)
  The action’s title.
- [var image: UIImage?](uiaction/image.md)
  The action’s image.
- [var identifier: UIAction.Identifier](uiaction/identifier-swift.property.md)
  The unique identifier for the action.
- [var discoverabilityTitle: String?](uiaction/discoverabilitytitle.md)
  An elaborated title that explains the purpose of the action.
- [var attributes: UIMenuElement.Attributes](uiaction/attributes.md)
  The attributes indicating the style of the action.
- [var state: UIMenuElement.State](uiaction/state.md)
  The state of the action.
- [var sender: Any?](uiaction/sender.md)
  The object responsible for the action handler.
### Initializers
- [convenience init(title: String, subtitle: String?, image: UIImage?, selectedImage: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](uiaction/init(title:subtitle:image:selectedimage:identifier:discoverabilitytitle:attributes:state:handler:).md)

## Relationships

### Inherits From
- [UIMenuElement](uimenuelement.md)
### Inherited By
- [UIWindowScene.ActivationAction](uiwindowscene/activationaction.md)
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
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIMenuLeaf](uimenuleaf.md)

## See Also

- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](adopting-menus-and-uiactions-in-your-user-interface.md)
  Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [class UIMenuElement](uimenuelement.md)
  An object representing a menu, action, or command.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction)*