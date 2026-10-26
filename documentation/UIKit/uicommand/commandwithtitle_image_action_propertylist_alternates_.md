# commandWithTitle:image:action:propertyList:alternates:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a command with the specified title, image, action, property list, and alternative commands.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) commandWithTitle:(NSString *) title image:(UIImage *) image action:(SEL) action propertyList:(id) propertyList alternates:(NSArray<UICommandAlternate *> *) alternates;
```

#### Return Value

A newly initialized command object.

## Parameters

- `title`: The title to display for the command.
- `image`: The image to display next to the command’s title. Only the [`context`](../uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.
- `action`: The action to take after a person selects the command.
- `propertyList`: An object that contains data to associate with the command.
- `alternates`: An array of alternatives for the command.

## See Also

### Creating a command
- [+ commandWithTitle:image:action:propertyList:](./commandwithtitle_image_action_propertylist_.md)
  Creates a command with the specified title, image, action, and property list.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a command from data in an unarchiver.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommand/commandwithtitle:image:action:propertylist:alternates:)*