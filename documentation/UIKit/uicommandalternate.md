# UICommandAlternate

**Framework**: UIKit  
**Kind**: class

An object representing an alternative action for a command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICommandAlternate
```

#### Overview

Create a [`UICommandAlternate`](uicommandalternate.md) object and add it to a [`UICommand`](uicommand.md) or [`UIKeyCommand`](uikeycommand.md) object when you want to provide users an alternative action for the command. The command alternate is available to the user when they press the keyboard modifier keys, like Control or Option, specified in the [`modifierFlags`](uicommandalternate/modifierflags.md) property.

For instance, an app may have a Reload menu, created with a key command, that has the keyboard shortcut Command+R. When the user selects Reload, or presses Command+R on their keyboard, the app reloads the data displayed in the current window. The app, however, can display more than one window, so it includes a Reload All alternative for Reload that reloads data in all windows, not just the current one.

The Reload All command alternate specifies [`alternate`](uikeymodifierflags/alternate.md) in its [`modifierFlags`](uicommandalternate/modifierflags.md) property, which makes Reload All available to the user when they press the Option key. To select Reload All, the user can press and hold the Option key while displaying the menu that contains Reload. This replaces the Reload menu with Reload All. The user can also select Reload All by pressing Option+Command+R.

```swift
// Create an alternate for the reload command. The alternative command appears
// in the menu system when the user holds down the keys specified in `modifierFlags`.
let reloadAlternate = UICommandAlternate(title: "Reload All",
                                         action: #selector(reloadAllData(_:)),
                                         modifierFlags: [.alternate])

// Create a selector-based action with a keyboard shortcut to use as a menu element.
let reloadCommand = UIKeyCommand(title: "Reload",
                                action: #selector(reloadData(_:)),
                                input: "r",
                                modifierFlags: [.command],
                                alternates: [reloadAlternate])

// Use the .displayInline option to avoid displaying the menu as a submenu,
// and to separate it from the other menu elements using a line separator.
let reloadMenuItem = UIMenu(title: "", options: .displayInline, children: [reloadCommand])

// Insert the menu into the File menu before the Close menu.
builder.insertSibling(reloadMenuItem, beforeMenu: .close)
```

## Topics

### Creating a command alternative
- [convenience init(title: String, action: Selector, modifierFlags: UIKeyModifierFlags)](uicommandalternate/init(title:action:modifierflags:).md)
  Creates a command alternative with the specified title, action, and modifier flags.
- [init?(coder: NSCoder)](uicommandalternate/init(coder:).md)
  Creates a command alternative from data in an unarchiver.
### Getting information about the alternative
- [var title: String](uicommandalternate/title.md)
  The command alternative’s title.
- [var action: Selector](uicommandalternate/action.md)
  The command alternative’s action-method selector.
- [var modifierFlags: UIKeyModifierFlags](uicommandalternate/modifierflags.md)
  The bit mask of modifier keys that the user must press to invoke the action for the alternative command.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

## See Also

- [var alternates: [UICommandAlternate]](uicommand/alternates.md)
  An array of alternative actions to take for the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommandalternate)*