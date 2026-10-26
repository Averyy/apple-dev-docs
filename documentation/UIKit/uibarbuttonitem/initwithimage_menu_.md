# initWithImage:menu:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a plain-style item using the specified image and context menu.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithImage:(UIImage *) image menu:(UIMenu *) menu;
```

#### Return Value

A newly initialized [`UIBarButtonItem`](../uibarbuttonitem.md).

## Parameters

- `image`: The item’s image. If `nil`, an image doesn’t appear.

  The images displayed on the bar derive from this image. If this image is too large to fit on the bar, it’s scaled to fit. Typically, the size of a toolbar and navigation bar image is `20` x `20` points. The system uses the alpha values in the source image to create the images, ignoring opaque values.
- `menu`: The menu to present. The context menu displays in response to a person tapping the item.

## See Also

### Creating items
- [- initWithPrimaryAction:menu:](./initwithprimaryaction_menu_.md)
  Creates a plain-style item using the specified primary action and context menu.
- [- initWithPrimaryAction:](./initwithprimaryaction_.md)
  Creates a plain-style item using the specified primary action.
- [- initWithTitle:image:target:action:menu:](./initwithtitle_image_target_action_menu_.md)
  Creates a plain-style item the specified title, image, target, action, and context menu.
- [- initWithTitle:menu:](./initwithtitle_menu_.md)
  Creates a plain-style item using the specified title and menu.
- [init()](./init%28%29.md)
  Initializes the item to its default state.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an item from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/initwithimage:menu:)*