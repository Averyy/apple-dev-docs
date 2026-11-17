# init(text:images:imageTitles:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Initialize a list image row item with a text string, an array of @c UIImage for the grid of images, and an array of @c NSString titles, one displayed below each image.

**Availability**:
- iOS 17.4+ - Deprecated in 26.0
- iPadOS 17.4+ - Deprecated in 26.0
- Mac Catalyst 17.4+ - Deprecated in 26.0

> **Deprecated**: Use initWithText:elements:allowsMultipleLines:

## Declaration

```swift
init(text: String, images: [UIImage], imageTitles: [String])
```

```objc
- (instancetype) initWithText:(NSString *) text images:(NSArray<UIImage *> *) images imageTitles:(NSArray<NSString *> *) imageTitles;
```

## Discussion

The number of titles in the @c imageTitles list should be equal to the number of images in the

When providing an image, your app should provide a @c UIImage that is display-ready. If necessary for the image, provide light and dark styles by using an asset from your asset catalog, prepared with light and dark styles or by using @c UIImageAsset to combine two @c UIImage instances into a single image with both styles.

UIImageAsset is used to combine multiple UIImages with different trait collections into a single UIImage.

> **Note**: The expected image size is given by +[CPListImageRowItem maximumImageSize]. Images provided will be resized to this size if necessary.

To properly size your images, your app should size them to the display scale of the car screen. See -[CPInterfaceController carTraitCollection].

## See Also

### Deprecated
- [init(text: String, images: [UIImage])](./init%28text,images%29.md)
  Initialize a list image row item with a text string and an array of @c UIImage for the grid of images.
- [var gridImages: [UIImage]](./gridimages.md)
  Read-only access to the grid images shown in a row in the cell.
- [var imageTitles: [String]](./imagetitles.md)
  The titles displayed for each image in this image row item.
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The expected image size for the grid images in your @c CPListImageRowItem. Images provided will be resized to this size.
- [func update([UIImage])](./update%28_%29.md)
  Update the images displayed in this image row item. If this image row item is already displayed in a list template, this image row item will be automatically reloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/init(text:images:imagetitles:))*