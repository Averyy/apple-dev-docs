# update(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Update the images displayed in this image row item. If this image row item is already displayed in a list template, this image row item will be automatically reloaded.

**Availability**:
- iOS 14.0+ - Deprecated in 26.0
- iPadOS 14.0+ - Deprecated in 26.0
- Mac Catalyst 14.0+ - Deprecated in 26.0

> **Deprecated**: No longer supported

## Declaration

```swift
func update(_ gridImages: [UIImage])
```

```objc
- (void) updateImages:(NSArray<UIImage *> *) gridImages;
```

## Discussion

When providing an image, your app should provide a @c UIImage that is display-ready. If necessary for the image, provide light and dark styles by using an asset from your asset catalog, prepared with light and dark styles or by using @c UIImageAsset to combine two @c UIImage instances into a single image with both styles.

UIImageAsset is used to combine multiple UIImages with different trait collections into a single UIImage.

the @c text property of the image row item.

the @c imageTitles property of the image row item.

## See Also

### Deprecated
- [init(text: String, images: [UIImage])](./init%28text,images%29.md)
  Initialize a list image row item with a text string and an array of @c UIImage for the grid of images.
- [init(text: String, images: [UIImage], imageTitles: [String])](./init%28text,images,imagetitles%29.md)
  Initialize a list image row item with a text string, an array of @c UIImage for the grid of images, and an array of @c NSString titles, one displayed below each image.
- [var gridImages: [UIImage]](./gridimages.md)
  Read-only access to the grid images shown in a row in the cell.
- [var imageTitles: [String]](./imagetitles.md)
  The titles displayed for each image in this image row item.
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The expected image size for the grid images in your @c CPListImageRowItem. Images provided will be resized to this size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/update(_:))*