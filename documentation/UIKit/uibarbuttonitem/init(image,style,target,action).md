# init(image:style:target:action:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an item using the specified image, style, target, and action.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
convenience init(image: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)
```

```objc
- (instancetype) initWithImage:(UIImage *) image style:(UIBarButtonItemStyle) style target:(id) target action:(SEL) action;
```

#### Return Value

A newly initialized [`UIBarButtonItem`](../uibarbuttonitem.md).

## Parameters

- `image`: The item’s image. If `nil`, an image doesn’t appear.

  The images displayed on the bar derive from this image. If this image is too large to fit on the bar, it’s scaled to fit. Typically, the size of a toolbar and navigation bar image is `20` x `20` points. The system uses the alpha values in the source image to create the images, ignoring opaque values.
- `style`: The style of the item. For possible values, see [`UIBarButtonItem.Style`](./style-swift.enum.md).
- `target`: The object that receives the `action` message.
- `action`: The action to send to `target` when a person selects this item.

## See Also

### Related Documentation
- [convenience init(barButtonSystemItem: UIBarButtonItem.SystemItem, target: Any?, action: Selector?)](./init%28barbuttonsystemitem,target,action%29.md)
  Creates an item using the specified system item, target, and action.
### Creating items of a specific style
- [convenience init(title: String?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](./init%28title,style,target,action%29.md)
  Creates an item using the specified title, style, target, and action.
- [convenience init(image: UIImage?, landscapeImagePhone: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](./init%28image,landscapeimagephone,style,target,action%29.md)
  Creates an item using the specified images, style, target, and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(image:style:target:action:))*