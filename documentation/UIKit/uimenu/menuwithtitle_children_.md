# menuWithTitle:children:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a menu with the specified title and child menu elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```objc
+ (UIMenu *) menuWithTitle:(NSString *) title children:(NSArray<UIMenuElement *> *) children;
```

## Return Value

A new menu object.

## Discussion

This method creates a unique identifier for the menu and exposes that value from the [`identifier`](./identifier-swift.property.md) property.

## Parameters

- `title`: The title of the menu.
- `children`: The menu elements in the menu. Specify leaf menu elements using [`UIMenuElement`](../uimenuelement.md) subclasses like [`UIAction`](../uiaction.md), [`UICommand`](../uicommand.md), or [`UIKeyCommand`](../uikeycommand.md), and specify submenus using [`UIMenu`](../uimenu.md) objects. You may specify an empty array if the menu has no child menu elements.

## See Also

### Creating a menu object
- [+ menuWithChildren:](./menuwithchildren_.md)
  Creates a new menu with the specified child elements.
- [+ menuWithTitle:image:identifier:options:children:](./menuwithtitle_image_identifier_options_children_.md)
  Creates a new menu with the specified values.
- [UIMenu.Identifier](./identifier-swift.struct.md)
  Constants you use to identify an app’s standard menus.
- [UIMenu.Options](./options-swift.struct.md)
  Options you use to configure a menu’s appearance.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a menu from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/menuwithtitle:children:)*