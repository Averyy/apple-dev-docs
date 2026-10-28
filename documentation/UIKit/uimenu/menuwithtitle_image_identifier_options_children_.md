# menuWithTitle:image:identifier:options:children:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a new menu with the specified values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```objc
+ (UIMenu *) menuWithTitle:(NSString *) title image:(UIImage *) image identifier:(UIMenuIdentifier) identifier options:(UIMenuOptions) options children:(NSArray<UIMenuElement *> *) children;
```

## Return Value

A new menu object containing the specified menu elements.

## Parameters

- `title`: The title of the menu.
- `image`: The image to display next to the menu’s title.
- `identifier`: The unique identifier for the menu. When creating standard menus for your app, specify an appropriate constant defined in [`UIMenu.Identifier`](./identifier-swift.struct.md). For custom menus, specify a custom reverse domain name value, or specify `nil` to let this method create a unique identifier for you.
- `options`: Additional configuration options for the menu. For a list of possible values, see [`UIMenu.Options`](./options-swift.struct.md).
- `children`: The menu elements in the menu. Specify leaf menu elements using [`UIMenuElement`](../uimenuelement.md) subclasses like [`UIAction`](../uiaction.md), [`UICommand`](../uicommand.md), or [`UIKeyCommand`](../uikeycommand.md), and specify submenus using [`UIMenu`](../uimenu.md) objects. You may specify an empty array if the menu has no child menu elements.

## See Also

### Creating a menu object
- [+ menuWithChildren:](./menuwithchildren_.md)
  Creates a new menu with the specified child elements.
- [+ menuWithTitle:children:](./menuwithtitle_children_.md)
  Creates a menu with the specified title and child menu elements.
- [UIMenu.Identifier](./identifier-swift.struct.md)
  Constants you use to identify an app’s standard menus.
- [UIMenu.Options](./options-swift.struct.md)
  Options you use to configure a menu’s appearance.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a menu from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/menuwithtitle:image:identifier:options:children:)*