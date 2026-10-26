# initWithTitle:image:target:action:menu:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a plain-style item the specified title, image, target, action, and context menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithTitle:(NSString *) title image:(UIImage *) image target:(id) target action:(SEL) action menu:(UIMenu *) menu;
```

#### Return Value

A newly initialized [`UIBarButtonItem`](../uibarbuttonitem.md).

## Parameters

- `title`: The item’s title. If `nil`, a title doesn’t appear.
- `image`: The item’s image. If `nil`, an image doesn’t appear.

  The images displayed on the bar derive from this image. If this image is too large to fit on the bar, it’s scaled to fit. Typically, the size of a toolbar and navigation bar image is `20` x `20` points. The system uses the alpha values in the source image to create the images, ignoring opaque values.
- `target`: The object that receives the `action` message.
- `action`: The action to send to `target` when a person selects this item.
- `menu`: The menu to present. The context menu displays in response to a person tapping the item.

## See Also

### Creating items
- [- initWithPrimaryAction:menu:](./initwithprimaryaction_menu_.md)
  Creates a plain-style item using the specified primary action and context menu.
- [- initWithPrimaryAction:](./initwithprimaryaction_.md)
  Creates a plain-style item using the specified primary action.
- [- initWithTitle:menu:](./initwithtitle_menu_.md)
  Creates a plain-style item using the specified title and menu.
- [- initWithImage:menu:](./initwithimage_menu_.md)
  Creates a plain-style item using the specified image and context menu.
- [init()](./init%28%29.md)
  Initializes the item to its default state.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an item from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/initwithtitle:image:target:action:menu:)*