# CPMaximumNumberOfGridImages

**Framework**: CarPlay  
**Kind**: var  
**Role**: Global Variable

The maximum number of images that an image row can contain.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
let CPMaximumNumberOfGridImages: Int
```

```c
extern const NSUInteger CPMaximumNumberOfGridImages;
```

#### Discussion

At runtime, use this value to determine the total number of images that CarPlay allows in an image row. The list item may display fewer images, depending on the width of the vehicle’s primary screen.

## See Also

### Managing Content
- [var text: String?](./cplistimagerowitem/text.md)
  The list item’s primary text.
- [var gridImages: [UIImage]](./cplistimagerowitem/gridimages.md)
  The images that appear in the list item’s image row.
- [func update([UIImage])](./cplistimagerowitem/update%28_%29.md)
  Adds, removes, reorders, or updates the images in the list item’s image row.
- [class var maximumImageSize: CGSize](./cplistimagerowitem/maximumimagesize.md)
  The maximum size of an image that an image row can display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaximumnumberofgridimages)*