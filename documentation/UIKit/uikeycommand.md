# UIKeyCommand

**Framework**: UIKit  
**Kind**: class

An object that specifies a key press perform on a hardware keyboard and the resulting action.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIKeyCommand
```

## Mentions

- [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md)

#### Overview

Hardware keyboards allow a user to hold down the Control, Option, Command, or other modifier key and press another key in combination to initiate commands such as Cut, Copy, or Paste. You can use instances of this class to define custom command sequences that your app recognizes and then provide an appropriate response.

To use this class, you create instances and associate them with your app’s responder objects. Each responder has a [`keyCommands`](uiresponder/keycommands.md) property that you can redefine and use to return the key command objects that responder supports. Key command sequences are generated only for devices with an attached hardware keyboard.

The system always has the first opportunity to handle key commands. Key commands that map to known system events (such as Cut, Copy, and Paste) are automatically routed to the appropriate responder methods. For other key commands, the system looks for an object in the responder chain with a key command object that matches the pressed keys. If it finds such an object, it then searches the responder chain, looking for the first object that implements the corresponding action method, and calls the first one it finds.

iPad apps that run in macOS can use [`UIKeyCommand`](uikeycommand.md) to create menu elements that have keyboard shortcuts.

## Topics

### Creating a key command object
- [convenience init(title: String, image: UIImage?, action: Selector, input: String, modifierFlags: UIKeyModifierFlags, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](uikeycommand/init(title:image:action:input:modifierflags:propertylist:alternates:discoverabilitytitle:attributes:state:).md)
  Creates a key command that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.
- [convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector)](uikeycommand/init(input:modifierflags:action:).md)
  Creates a key command that matches the specified input.
- [init?(coder: NSCoder)](uikeycommand/init(coder:).md)
  Creates a key command from data in an unarchiver.
- [init()](uikeycommand/init.md)
  Creates a key command.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
### Getting information about the key command
- [var title: String](uikeycommand/title.md)
  The key command’s title.
- [var image: UIImage?](uikeycommand/image.md)
  The key command’s image.
- [var input: String?](uikeycommand/input.md)
  The string of characters corresponding to the keys that must be pressed to match this key command.
- [var action: Selector?](uikeycommand/action.md)
  The command’s action-method selector.
- [var modifierFlags: UIKeyModifierFlags](uikeycommand/modifierflags.md)
  The bit mask of modifier flags that must be pressed to match this key command.
- [struct UIKeyModifierFlags](uikeymodifierflags.md)
  Constants that indicate which modifier keys are pressed.
- [var discoverabilityTitle: String?](uikeycommand/discoverabilitytitle.md)
  An elaborated title that explains the purpose of the key command.
- [var attributes: UIMenuElement.Attributes](uikeycommand/attributes.md)
  The attributes indicating the style of the key command.
- [var state: UIMenuElement.State](uikeycommand/state.md)
  The state of the key command.
### Getting command alternatives
- [var alternates: [UICommandAlternate]](uikeycommand/alternates.md)
  An array of alternative actions to take for the key command.
- [class UICommandAlternate](uicommandalternate.md)
  An object representing an alternative action for a command.
### Localizing keyboard shortcuts
- [var allowsAutomaticLocalization: Bool](uikeycommand/allowsautomaticlocalization.md)
  A Boolean value that determines whether the system automatically remaps keyboard shortcuts based on the keyboard layout.
- [var allowsAutomaticMirroring: Bool](uikeycommand/allowsautomaticmirroring.md)
  A Boolean value that determines whether the system automatically swaps input strings for some keyboard shortcuts when the interface direction changes.
### Overriding the key event delivery behavior
- [var wantsPriorityOverSystemBehavior: Bool](uikeycommand/wantspriorityoversystembehavior.md)
  A Boolean value that indicates whether the key command takes precedence over text input or focus movements.
### Associating data
- [var propertyList: Any?](uikeycommand/propertylist.md)
  An object that contains data to associate with the key command.
- [let UICommandTagShare: String](uicommandtagshare.md)
  A value that identifies a command as a Share menu.
### Converting strings to key commands
- [Input strings for special keys](input-strings-for-special-keys.md)
  Constants that represent the text input strings that correspond to special nonvisible keys.
### Deprecated
- [convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector, discoverabilityTitle: String)](uikeycommand/init(input:modifierflags:action:discoverabilitytitle:).md)
  Creates a key command object that matches the specified input and has a title.

## Relationships

### Inherits From
- [UICommand](uicommand.md)
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
- [class UICommand](uicommand.md)
  A menu element that performs its action in a selector.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand)*