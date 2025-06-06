# init(image:style:target:action:)

**Framework**: UIKit  
**Kind**: init

Creates an item using the specified image, style, target, and action.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(image: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)
```

#### Return Value

A newly initialized [`UIBarButtonItem`](uibarbuttonitem.md).

## Parameters

- `image`: The images displayed on the bar derive from this image. If this image is too large to fit on the bar, it’s scaled to fit. Typically, the size of a toolbar and navigation bar image is   x   points. The system uses the alpha values in the source image to create the images, ignoring opaque values.
- `style`: The style of the item. For possible values, see  .
- `target`: The object that receives the   message.
- `action`: The action to send to   when a person selects this item.

## See Also

- [convenience init(barButtonSystemItem: UIBarButtonItem.SystemItem, target: Any?, action: Selector?)](uibarbuttonitem/init(barbuttonsystemitem:target:action:).md)
  Creates an item using the specified system item, target, and action.
- [convenience init(title: String?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](uibarbuttonitem/init(title:style:target:action:).md)
  Creates an item using the specified title, style, target, and action.
- [convenience init(image: UIImage?, landscapeImagePhone: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](uibarbuttonitem/init(image:landscapeimagephone:style:target:action:).md)
  Creates an item using the specified images, style, target, and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(image:style:target:action:))*