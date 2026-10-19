# init(input:modifierFlags:action:discoverabilityTitle:)

**Framework**: UIKit  
**Kind**: init

Creates a key command object that matches the specified input and has a title.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector, discoverabilityTitle: String)
```

#### Return Value

The initialized key command object.

#### Discussion

After creating a key command object, you can add it to a view controller using the [`addKeyCommand(_:)`](uiviewcontroller/addkeycommand(_:).md) method of the view controller. You can also override any responder class and return the key command directly from the responder’s [`keyCommands`](uiresponder/keycommands.md) property.

## Parameters

- `input`: The keys that a person must press. The string must contain one or more characters corresponding to the keys a person pressed. For a list of special characters that don’t have a textual representation, see [`Input strings for special keys`](input-strings-for-special-keys.md).
- `modifierFlags`: The bit mask of modifier keys that a person must press. You can use this parameter to specify which modifier keys (Command, Option, and so on) a person must also press. You may specify more than one modifier key. For a list of possible values, see [`UIKeyModifierFlags`](uikeymodifierflags.md).
- `action`: The action method to execute on the responder object.
- `discoverabilityTitle`: An elaborated title that explains the purpose of the key command.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/init(input:modifierflags:action:discoverabilitytitle:))*