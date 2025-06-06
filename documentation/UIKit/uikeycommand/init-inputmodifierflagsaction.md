# init(input:modifierFlags:action:)

**Framework**: UIKit  
**Kind**: init

Creates a key command that matches the specified input.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector)
```

#### Return Value

A newly initialized key command object.

#### Discussion

After creating a key command object, you can:

- Add it as a child of a [`UIMenu`](uimenu.md) using the menu’s [`init(title:image:identifier:options:children:)`](uimenu/init(title:image:identifier:options:children:).md) method.
- Add it to a view controller using the [`addKeyCommand(_:)`](uiviewcontroller/addkeycommand(_:).md) method of the view controller.
- Override any responder class and return the key command directly from the responder’s [`keyCommands`](uiresponder/keycommands.md) property.

## Parameters

- `input`: The keys that a person must press. The string must contain one or more characters corresponding to the keys a person pressed. For a list of special characters that don’t have a textual representation, see  .
- `modifierFlags`: The bit mask of modifier keys that a person must press. You can use this parameter to specify which modifier keys (Command, Option, and so on) a person must also press. You may specify more than one modifier key. For a list of possible values, see  .
- `action`: The action method to execute on the responder object.

## See Also

- [convenience init(title: String, image: UIImage?, action: Selector, input: String, modifierFlags: UIKeyModifierFlags, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](uikeycommand/init(title:image:action:input:modifierflags:propertylist:alternates:discoverabilitytitle:attributes:state:).md)
  Creates a key command that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.
- [init?(coder: NSCoder)](uikeycommand/init(coder:).md)
  Creates a key command from data in an unarchiver.
- [init()](uikeycommand/init.md)
  Creates a key command.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/init(input:modifierflags:action:))*