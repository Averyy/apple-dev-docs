# menuWithChildren:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a new menu with the specified child elements.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
+ (UIMenu *) menuWithChildren:(NSArray<UIMenuElement *> *) children;
```

## Parameters

- `children`: The menu elements in the menu. Specify leaf menu elements using [`UIMenuElement`](../uimenuelement.md) subclasses like [`UIAction`](../uiaction.md), [`UICommand`](../uicommand.md), or [`UIKeyCommand`](../uikeycommand.md), and specify submenus using [`UIMenu`](../uimenu.md) objects. You may specify an empty array if the menu has no child menu elements.

## See Also

### Creating a menu object
- [+ menuWithTitle:children:](./menuwithtitle_children_.md)
  Creates a menu with the specified title and child menu elements.
- [+ menuWithTitle:image:identifier:options:children:](./menuwithtitle_image_identifier_options_children_.md)
  Creates a new menu with the specified values.
- [UIMenu.Identifier](./identifier-swift.struct.md)
  Constants you use to identify an app’s standard menus.
- [UIMenu.Options](./options-swift.struct.md)
  Options you use to configure a menu’s appearance.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a menu from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/menuwithchildren:)*