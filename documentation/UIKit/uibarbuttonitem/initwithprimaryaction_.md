# initWithPrimaryAction:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a plain-style item using the specified primary action.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithPrimaryAction:(UIAction *) primaryAction;
```

#### Return Value

A newly initialized [`UIBarButtonItem`](../uibarbuttonitem.md).

## Parameters

- `primaryAction`: A [`UIAction`](../uiaction.md) to associate with the item, which the item uses to configure its title and image.

## See Also

### Creating items
- [- initWithPrimaryAction:menu:](./initwithprimaryaction_menu_.md)
  Creates a plain-style item using the specified primary action and context menu.
- [- initWithTitle:image:target:action:menu:](./initwithtitle_image_target_action_menu_.md)
  Creates a plain-style item the specified title, image, target, action, and context menu.
- [- initWithTitle:menu:](./initwithtitle_menu_.md)
  Creates a plain-style item using the specified title and menu.
- [- initWithImage:menu:](./initwithimage_menu_.md)
  Creates a plain-style item using the specified image and context menu.
- [init()](./init%28%29.md)
  Initializes the item to its default state.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an item from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/initwithprimaryaction:)*