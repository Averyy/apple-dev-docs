# init(title:style:target:action:)

**Framework**: UIKit  
**Kind**: init

Creates an item using the specified title, style, target, and action.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(title: String?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)
```

#### Return Value

A newly initialized [`UIBarButtonItem`](uibarbuttonitem.md).

## Parameters

- `title`: The item’s title. If  , a title doesn’t appear.
- `style`: The style of the item. For possible values, see  .
- `target`: The object that receives the   message.
- `action`: The action to send to   when a person selects this item.

## See Also

- [convenience init(barButtonSystemItem: UIBarButtonItem.SystemItem, target: Any?, action: Selector?)](uibarbuttonitem/init(barbuttonsystemitem:target:action:).md)
  Creates an item using the specified system item, target, and action.
- [convenience init(image: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](uibarbuttonitem/init(image:style:target:action:).md)
  Creates an item using the specified image, style, target, and action.
- [convenience init(image: UIImage?, landscapeImagePhone: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](uibarbuttonitem/init(image:landscapeimagephone:style:target:action:).md)
  Creates an item using the specified images, style, target, and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(title:style:target:action:))*