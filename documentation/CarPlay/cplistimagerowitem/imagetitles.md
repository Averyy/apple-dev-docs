# imageTitles

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The titles displayed for each image in this image row item.

**Availability**:
- iOS 17.4+ - Deprecated in 26.0
- iPadOS 17.4+ - Deprecated in 26.0
- Mac Catalyst 17.4+ - Deprecated in 26.0

> **Deprecated**: No longer supported

## Declaration

```swift
var imageTitles: [String] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * imageTitles;
```

## Discussion

The @c text property of the image row item.

## See Also

### Deprecated
- [init(text: String, images: [UIImage])](./init%28text,images%29.md)
  Initialize a list image row item with a text string and an array of @c UIImage for the grid of images.
- [init(text: String, images: [UIImage], imageTitles: [String])](./init%28text,images,imagetitles%29.md)
  Initialize a list image row item with a text string, an array of @c UIImage for the grid of images, and an array of @c NSString titles, one displayed below each image.
- [var gridImages: [UIImage]](./gridimages.md)
  Read-only access to the grid images shown in a row in the cell.
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The expected image size for the grid images in your @c CPListImageRowItem. Images provided will be resized to this size.
- [func update([UIImage])](./update%28_%29.md)
  Update the images displayed in this image row item. If this image row item is already displayed in a list template, this image row item will be automatically reloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/imagetitles)*