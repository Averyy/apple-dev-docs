# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a command from data in an unarchiver.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Creating a command
- [convenience init(title: String, subtitle: String?, image: UIImage?, action: Selector, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](./init%28title,subtitle,image,action,propertylist,alternates,discoverabilitytitle,attributes,state%29.md)
  Creates a command with the specified title, subtitle, image, action, property list, alternative commands, discoverability title, attributes, and state.
- [convenience init(title: String, image: UIImage?, action: Selector, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](./init%28title,image,action,propertylist,alternates,discoverabilitytitle,attributes,state%29.md)
  Creates a command with the specified title, image, action, property list, alternative commands, discoverability title, attributes, and state.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommand/init(coder:))*