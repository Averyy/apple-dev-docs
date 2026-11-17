# init(thumbnail:title:subtitle:tintColor:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a card row element with a thumbnail image, text, and background color.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, tintColor: UIColor?)
```

```objc
- (instancetype) initWithThumbnail:(CPThumbnailImage *) thumbnail title:(NSString *) title subtitle:(NSString *) subtitle tintColor:(UIColor *) tintColor;
```

## Return Value

An initialized element you can add to a row.

## Discussion

CarPlay stores the `thumbnail` image in the [`thumbnail`](./thumbnail.md) property. This method also stores a version of the image in the inherited [`image`](../cplistimagerowitemelement/image.md) property.

When using this method to initialize the elements of a row, the aspect ratio of the first element you specify dictates the layout for the rest of the row. For example, if the first element contains a landscape image, the row lays out all other elements with the landscape aspect ratio.

## Parameters

- `thumbnail`: The thumbnail to display as the element’s primary content. If the image you used to create the thumbnail originates from an asset catalog, CarPlay manages the light and dark variants of the image and switches them when needed. Specify images with the dimensions listed in the [`maximumFullHeightImageSize`](./maximumfullheightimagesize.md) property. If your image is smaller or larger than the maximum dimensions, CarPlay scales the image as needed to fit the space. Don’t specify an image with an animated sequence.
- `title`: The primary text to display beneath the image. CarPlay displays this string with a visually prominent style.
- `subtitle`: The secondary text to display beneath the title. CarPlay displays this string less prominently than the title.
- `tintColor`: The color to apply to the card’s background. Specify `nil` to use the [`secondarySystemBackground`](../../UIKit/uicolor/secondarysystembackground.md) color.

## See Also

### Creating a card element
- [init(image: UIImage, showsImageFullHeight: Bool, title: String?, subtitle: String?, tintColor: UIColor?)](./init%28image,showsimagefullheight,title,subtitle,tintcolor%29.md)
  Creates a card row element with the specified image, text, and card background color.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/init(thumbnail:title:subtitle:tintcolor:))*