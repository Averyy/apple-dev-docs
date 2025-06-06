# init(text:detailText:image:)

**Framework**: CarPlay  
**Kind**: init

Creates a list item with primary text, secondary text, and an image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(text: String?, detailText: String?, image: UIImage?)
```

#### Return Value

A newly initialized list item.

## Parameters

- `text`: The primary text to show in the list item cell.
- `detailText`: Additional text to display below the primary text in the list item cell.
- `image`: The image to display on the leading edge of the list item cell. If the image is larger than  , the list item scales down the image to maximum size. If you provide an animated image, the list item uses the first image in the animation sequence.

## See Also

- [init(text: String?, detailText: String?)](cplistitem/init(text:detailtext:).md)
  Creates a list item with primary and secondary text.
- [init(text: String?, detailText: String?, image: UIImage?, accessoryImage: UIImage?, accessoryType: CPListItemAccessoryType)](cplistitem/init(text:detailtext:image:accessoryimage:accessorytype:).md)
  Creates a list item that displays an accessory beside its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/init(text:detailtext:image:))*