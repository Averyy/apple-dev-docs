# gridImages

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Read-only access to the grid images shown in a row in the cell.

**Availability**:
- iOS 14.0+ - Deprecated in 26.0
- iPadOS 14.0+ - Deprecated in 26.0
- Mac Catalyst 14.0+ - Deprecated in 26.0

> **Deprecated**: No longer supported

## Declaration

```swift
var gridImages: [UIImage] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<UIImage *> * gridImages;
```

## Discussion

> **Note**: The maximum number of images shown is @c CPMaximumNumberOfGridImages. If you supply more images, only the first @c CPMaximumNumberOfGridImages will be used.

## See Also

### Deprecated
- [init(text: String, images: [UIImage])](./init%28text,images%29.md)
  Initialize a list image row item with a text string and an array of @c UIImage for the grid of images.
- [init(text: String, images: [UIImage], imageTitles: [String])](./init%28text,images,imagetitles%29.md)
  Initialize a list image row item with a text string, an array of @c UIImage for the grid of images, and an array of @c NSString titles, one displayed below each image.
- [var imageTitles: [String]](./imagetitles.md)
  The titles displayed for each image in this image row item.
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The expected image size for the grid images in your @c CPListImageRowItem. Images provided will be resized to this size.
- [func update([UIImage])](./update%28_%29.md)
  Update the images displayed in this image row item. If this image row item is already displayed in a list template, this image row item will be automatically reloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/gridimages)*