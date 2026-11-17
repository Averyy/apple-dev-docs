# maximumImageSize

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The expected image size for the grid images in your @c CPListImageRowItem. Images provided will be resized to this size.

**Availability**:
- iOS 14.0+ - Deprecated in 26.0
- iPadOS 14.0+ - Deprecated in 26.0
- Mac Catalyst 14.0+ - Deprecated in 26.0

> **Deprecated**: Use +[CPListImageRowItemElement maximumImageSize] on an appropriate element

## Declaration

```swift
class var maximumImageSize: CGSize { get }
```

```objc
@property (class, nonatomic, readonly) CGSize maximumImageSize;
```

## Discussion

To properly size your images, your app should size them to the display scale of the car screen. See -[CPInterfaceController carTraitCollection].

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
- [func update([UIImage])](./update%28_%29.md)
  Update the images displayed in this image row item. If this image row item is already displayed in a list template, this image row item will be automatically reloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/maximumimagesize)*