# init(image:landscapeImagePhone:style:target:action:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an item using the specified images, style, target, and action.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
convenience init(image: UIImage?, landscapeImagePhone: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)
```

```objc
- (instancetype) initWithImage:(UIImage *) image landscapeImagePhone:(UIImage *) landscapeImagePhone style:(UIBarButtonItemStyle) style target:(id) target action:(SEL) action;
```

#### Return Value

A newly initialized [`UIBarButtonItem`](../uibarbuttonitem.md).

## Parameters

- `image`: The item’s image. If `nil`, an image doesn’t appear.
- `landscapeImagePhone`: The image to use for the item in landscape bars in the [`UIUserInterfaceIdiom.phone`](../uiuserinterfaceidiom/phone.md) idiom.
- `style`: The style of the item. For possible values, see [`UIBarButtonItem.Style`](./style-swift.enum.md).
- `target`: The object that receives the `action` message.
- `action`: The action to send to `target` when a person selects this item.

## See Also

### Creating items of a specific style
- [convenience init(title: String?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](./init%28title,style,target,action%29.md)
  Creates an item using the specified title, style, target, and action.
- [convenience init(image: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](./init%28image,style,target,action%29.md)
  Creates an item using the specified image, style, target, and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(image:landscapeimagephone:style:target:action:))*