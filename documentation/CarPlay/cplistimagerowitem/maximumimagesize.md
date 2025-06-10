# maximumImageSize

**Framework**: CarPlay  
**Kind**: property

The maximum size of an image that an image row can display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class var maximumImageSize: CGSize { get }
```

#### Discussion

At runtime, use this value to determine the maximum size that CarPlay allows for a single image in an image row.

## See Also

- [var text: String?](cplistimagerowitem/text.md)
  The list item’s primary text.
- [var gridImages: [UIImage]](cplistimagerowitem/gridimages.md)
  The images that appear in the list item’s image row.
- [func update([UIImage])](cplistimagerowitem/update(_:).md)
  Adds, removes, reorders, or updates the images in the list item’s image row.
- [let CPMaximumNumberOfGridImages: Int](cpmaximumnumberofgridimages.md)
  The maximum number of images that an image row can contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/maximumimagesize)*