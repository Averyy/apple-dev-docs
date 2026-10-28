# init(input:modifierFlags:action:discoverabilityTitle:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a key command object that matches the specified input and has a title.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: Use [`init(input:modifierFlags:action:)`](./init%28input,modifierflags,action%29.md) instead.

## Declaration

```swift
convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector, discoverabilityTitle: String)
```

```objc
+ (instancetype) keyCommandWithInput:(NSString *) input modifierFlags:(UIKeyModifierFlags) modifierFlags action:(SEL) action discoverabilityTitle:(NSString *) discoverabilityTitle;
```

## Return Value

The initialized key command object.

## Discussion

After creating a key command object, you can add it to a view controller using the [`addKeyCommand(_:)`](../uiviewcontroller/addkeycommand%28_%29.md) method of the view controller. You can also override any responder class and return the key command directly from the responder’s [`keyCommands`](../uiresponder/keycommands.md) property.

## Parameters

- `input`: The keys that a person must press. The string must contain one or more characters corresponding to the keys a person pressed. For a list of special characters that don’t have a textual representation, see [Input strings for special keys](../input-strings-for-special-keys.md).
- `modifierFlags`: The bit mask of modifier keys that a person must press. You can use this parameter to specify which modifier keys (Command, Option, and so on) a person must also press. You may specify more than one modifier key. For a list of possible values, see [`UIKeyModifierFlags`](../uikeymodifierflags.md).
- `action`: The action method to execute on the responder object.
- `discoverabilityTitle`: An elaborated title that explains the purpose of the key command.

## See Also

### Creating a key command object
- [convenience init(title: String, image: UIImage?, action: Selector, input: String, modifierFlags: UIKeyModifierFlags, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](./init%28title,image,action,input,modifierflags,propertylist,alternates,discoverabilitytitle,attributes,state%29.md)
  Creates a key command that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.
- [convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector)](./init%28input,modifierflags,action%29.md)
  Creates a key command that matches the specified input.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a key command from data in an unarchiver.
- [init()](./init%28%29.md)
  Creates a key command.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Navigating an app’s user interface using a keyboard](../navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [+ commandWithTitle:image:action:input:modifierFlags:propertyList:](./commandwithtitle_image_action_input_modifierflags_propertylist_.md)
  Creates a key command that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.
- [+ commandWithTitle:image:action:input:modifierFlags:propertyList:alternates:](./commandwithtitle_image_action_input_modifierflags_propertylist_alternates_.md)
  Creates a key command with alternatives that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/init(input:modifierflags:action:discoverabilitytitle:))*