# urls

**Framework**: Uikit  
**Kind**: property

An array of URL objects in all pasteboard items.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var urls: [URL]? { get set }
```

#### Discussion

The value stored in this property is an array of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects. The associated array of representation types is [`typeListURL`](uipasteboard/typelisturl.md), which includes type `kUTTypeURL`. Setting this property replaces all current items in the pasteboard with the new items. The returned array may have fewer objects than the number of pasteboard items; this happens if a pasteboard item does not have a value of the indicated type.

> **Note**:  Do not use this property to determine if a pasteboard contains URL data. Instead, use the [`hasURLs`](uipasteboard/hasurls.md) property.

## See Also

- [var string: String?](uipasteboard/string.md)
  The string value of the first pasteboard item.
- [var strings: [String]?](uipasteboard/strings.md)
  An array of strings in all pasteboard items.
- [var image: UIImage?](uipasteboard/image.md)
  The image object of the first pasteboard item.
- [var images: [UIImage]?](uipasteboard/images.md)
  An array of image objects in all pasteboard items.
- [var url: URL?](uipasteboard/url.md)
  The URL object of the first pasteboard item.
- [var color: UIColor?](uipasteboard/color.md)
  The color object of the first pasteboard item.
- [var colors: [UIColor]?](uipasteboard/colors.md)
  An array of color objects in all pasteboard items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/urls)*