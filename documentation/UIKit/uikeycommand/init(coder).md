# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a key command from data in an unarchiver.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Creating a key command object
- [convenience init(title: String, image: UIImage?, action: Selector, input: String, modifierFlags: UIKeyModifierFlags, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](./init%28title,image,action,input,modifierflags,propertylist,alternates,discoverabilitytitle,attributes,state%29.md)
  Creates a key command that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.
- [convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector)](./init%28input,modifierflags,action%29.md)
  Creates a key command that matches the specified input.
- [init()](./init%28%29.md)
  Creates a key command.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Navigating an app’s user interface using a keyboard](../navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector, discoverabilityTitle: String)](./init%28input,modifierflags,action,discoverabilitytitle%29.md)
  Creates a key command object that matches the specified input and has a title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/init(coder:))*