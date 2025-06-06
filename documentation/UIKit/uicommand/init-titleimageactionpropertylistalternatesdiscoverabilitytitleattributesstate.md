# init(title:image:action:propertyList:alternates:discoverabilityTitle:attributes:state:)

**Framework**: UIKit  
**Kind**: init

Creates a command with the specified title, image, action, property list, alternative commands, discoverability title, attributes, and state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(title: String = "", image: UIImage? = nil, action: Selector, propertyList: Any? = nil, alternates: [UICommandAlternate] = [], discoverabilityTitle: String? = nil, attributes: UIMenuElement.Attributes = [], state: UIMenuElement.State = .off)
```

## Parameters

- `title`: The title to display for the command.
- `image`: The image to display next to the command’s title. Only the   menu system supports the display of an image, and only when the app is running in iOS.
- `action`: The action to take after a person user selects the command.
- `propertyList`: An object that contains data to associate with the command.
- `alternates`: An array of alternatives for the command.
- `discoverabilityTitle`: An elaborated title that explains the purpose of the command.
- `attributes`: The attributes indicating the style of the command.
- `state`: The initial state of the command.

## See Also

- [convenience init(title: String, subtitle: String?, image: UIImage?, action: Selector, propertyList: Any?, alternates: [UICommandAlternate], discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State)](uicommand/init(title:subtitle:image:action:propertylist:alternates:discoverabilitytitle:attributes:state:).md)
  Creates a command with the specified title, subtitle, image, action, property list, alternative commands, discoverability title, attributes, and state.
- [init?(coder: NSCoder)](uicommand/init(coder:).md)
  Creates a command from data in an unarchiver.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommand/init(title:image:action:propertylist:alternates:discoverabilitytitle:attributes:state:))*