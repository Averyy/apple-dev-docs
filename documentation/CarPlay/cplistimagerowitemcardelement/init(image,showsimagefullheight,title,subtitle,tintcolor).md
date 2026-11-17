# init(image:showsImageFullHeight:title:subtitle:tintColor:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a card row element with the specified image, text, and card background color.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(image: UIImage, showsImageFullHeight: Bool, title: String?, subtitle: String?, tintColor: UIColor?)
```

```objc
- (instancetype) initWithImage:(UIImage *) image showsImageFullHeight:(BOOL) showsImageFullHeight title:(NSString *) title subtitle:(NSString *) subtitle tintColor:(UIColor *) tintColor;
```

## Return Value

An initialized element you can add to a row.

## Discussion

This method stores the provided image in the inherited [`image`](../cplistimagerowitemelement/image.md) property and doesn’t populate the [`thumbnail`](./thumbnail.md) property. If `showsImageFullHeight` is true, the [`maximumFullHeightImageSize`](./maximumfullheightimagesize.md) property species the expected dimensions of your image; otherwise, use the value in the [`maximumImageSize`](./maximumimagesize.md) property.

## Parameters

- `image`: The image to display as the element’s primary content. If the image originates from an asset catalog, CarPlay manages the light and dark variants of your image and switches them when needed. Specify images at the expected maximum dimensions. If your image is smaller or larger than the maximum dimensions, CarPlay scales the image as needed to fit the space. If the image contains an animated sequence, CarPlay shows only the first image in the sequence. -showsImageFullHeight: When`true`, the element displays the image as the card background instead of the tint color. Specify `false` to display a background color with the image on top.
- `title`: The primary text to display beneath the image. CarPlay displays this string with a visually prominent style.
- `subtitle`: The secondary text to display beneath the title. CarPlay displays this string less prominently than the title.
- `tintColor`: The color to apply to the card’s background.

## See Also

### Creating a card element
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, tintColor: UIColor?)](./init%28thumbnail,title,subtitle,tintcolor%29.md)
  Creates a card row element with a thumbnail image, text, and background color.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/init(image:showsimagefullheight:title:subtitle:tintcolor:))*