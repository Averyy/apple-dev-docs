# init(text:detailText:image:accessoryImage:accessoryType:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a list item that displays an accessory beside its content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(text: String?, detailText: String?, image: UIImage?, accessoryImage: UIImage?, accessoryType: CPListItemAccessoryType)
```

```objc
- (instancetype) initWithText:(NSString *) text detailText:(NSString *) detailText image:(UIImage *) image accessoryImage:(UIImage *) accessoryImage accessoryType:(CPListItemAccessoryType) accessoryType;
```

## Discussion

If you create the images for the `image` and `accessoryImage` parameters from an asset catalog resource, CarPlay manages light and dark variants of your image and switches them when needed. Specify images with the dimensions listed in the [`maximumImageSize`](./maximumimagesize.md) property. If your image is smaller or larger than the maximum dimensions, CarPlay scales the image as needed to fit the space. If the image contains an animated sequence, CarPlay shows only the first image in the sequence.

To determine the maximum pixel dimensions for images, multiply the value in the [`maximumImageSize`](./maximumimagesize.md) property by the current scale factor for your CarPlay interface. Get the interface scale factor from the traits in the [`carTraitCollection`](../cpinterfacecontroller/cartraitcollection.md) property of your interface controller.

## Parameters

- `text`: The primary text to show in the list item’s row.
- `detailText`: Secondary text to display below the primary text.
- `image`: An image to display on the leading edge of the list item’s row. If the image originates from an asset catalog, CarPlay manages light and dark variants of your image and switches them when needed.
- `accessoryImage`: An image to display on the trailing edge of the item’s row. Use this parameter to specify a custom accessory image. If you specify a value for the `accessoryType` parameter, set this parameter to `nil`.
- `accessoryType`: The accessory that the list item displays in its trailing region. If you specify an image in the `accessoryImage` parameter, CarPlay ignores the value in this parameter and sets the [`accessoryType`](./accessorytype.md) property to [`CPListItemAccessoryType.none`](../cplistitemaccessorytype/none.md).

## See Also

### Creating a list item
- [init(text: String?, detailText: String?)](./init%28text,detailtext%29.md)
  Creates a list item with primary and secondary text.
- [init(text: String?, detailText: String?, image: UIImage?)](./init%28text,detailtext,image%29.md)
  Creates a list item with primary text, secondary text, and an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/init(text:detailtext:image:accessoryimage:accessorytype:))*