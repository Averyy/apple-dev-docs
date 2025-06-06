# init()

**Framework**: UIKit  
**Kind**: init

Creates a key command.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init()
```

## See Also

- [convenience init(title: String, image: UIImage?, action: Selector, input: String, modifierFlags: UIKeyModifierFlags, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](uikeycommand/init(title:image:action:input:modifierflags:propertylist:alternates:discoverabilitytitle:attributes:state:).md)
  Creates a key command that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.
- [convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector)](uikeycommand/init(input:modifierflags:action:).md)
  Creates a key command that matches the specified input.
- [init?(coder: NSCoder)](uikeycommand/init(coder:).md)
  Creates a key command from data in an unarchiver.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/init())*