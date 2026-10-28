# maximumImageSize

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum size of an image that an image row can display.

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

At runtime, use this value to determine the maximum size that CarPlay allows for a single image in an image row.

## See Also

### Managing Content
- [var text: String?](./text.md)
  The list item’s primary text.
- [var gridImages: [UIImage]](./gridimages.md)
  The images that appear in the list item’s image row.
- [func update([UIImage])](./update%28_%29.md)
  Adds, removes, reorders, or updates the images in the list item’s image row.
- [let CPMaximumNumberOfGridImages: Int](../cpmaximumnumberofgridimages.md)
  The maximum number of images that an image row can contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/maximumimagesize)*