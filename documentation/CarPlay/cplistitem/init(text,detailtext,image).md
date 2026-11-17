# init(text:detailText:image:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a list item with primary text, secondary text, and an image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(text: String?, detailText: String?, image: UIImage?)
```

```objc
- (instancetype) initWithText:(NSString *) text detailText:(NSString *) detailText image:(UIImage *) image;
```

## Return Value

A newly initialized list item.

## Parameters

- `text`: The primary text to show in the list item’s row.
- `detailText`: Secondary text to display below the primary text.
- `image`: An image to display on the leading edge of the list item’s row. If the image originates from an asset catalog, CarPlay manages light and dark variants of your image and switches them when needed. Specify images with the dimensions listed in the [`maximumImageSize`](./maximumimagesize.md) property. If your image is smaller or larger than the maximum dimensions, CarPlay scales the image as needed to fit the space. Don’t specify an image object with an animated sequence of images.

## See Also

### Creating a list item
- [init(text: String?, detailText: String?)](./init%28text,detailtext%29.md)
  Creates a list item with primary and secondary text.
- [init(text: String?, detailText: String?, image: UIImage?, accessoryImage: UIImage?, accessoryType: CPListItemAccessoryType)](./init%28text,detailtext,image,accessoryimage,accessorytype%29.md)
  Creates a list item that displays an accessory beside its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/init(text:detailtext:image:))*