# url

**Framework**: UIKit  
**Kind**: property

The URL object of the first pasteboard item.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var url: URL? { get set }
```

#### Discussion

The value stored in this property is an [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object. The associated array of representation types is [`typeListURL`](uipasteboard/typelisturl.md), which includes type `kUTTypeURL`. Setting this property replaces all current items in the pasteboard with the new item.  If the first item has no value of the indicated type, `nil` is returned.

> **Note**:  Do not use this property to determine if a pasteboard contains URL data. Instead, use the [`hasURLs`](uipasteboard/hasurls.md) property.

 Do not use this property to determine if a pasteboard contains URL data. Instead, use the [`hasURLs`](uipasteboard/hasurls.md) property.

## See Also

- [var string: String?](uipasteboard/string.md)
  The string value of the first pasteboard item.
- [var strings: [String]?](uipasteboard/strings.md)
  An array of strings in all pasteboard items.
- [var image: UIImage?](uipasteboard/image.md)
  The image object of the first pasteboard item.
- [var images: [UIImage]?](uipasteboard/images.md)
  An array of image objects in all pasteboard items.
- [var urls: [URL]?](uipasteboard/urls.md)
  An array of URL objects in all pasteboard items.
- [var color: UIColor?](uipasteboard/color.md)
  The color object of the first pasteboard item.
- [var colors: [UIColor]?](uipasteboard/colors.md)
  An array of color objects in all pasteboard items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/url)*