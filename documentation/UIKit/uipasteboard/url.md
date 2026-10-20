# url

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) NSURL * URL;
```

#### Discussion

The value stored in this property is an [`NSURL`](../../Foundation/nsurl.md) object. The associated array of representation types is [`typeListURL`](./typelisturl.md), which includes type `kUTTypeURL`. Setting this property replaces all current items in the pasteboard with the new item.  If the first item has no value of the indicated type, `nil` is returned.

> **Note**:  Do not use this property to determine if a pasteboard contains URL data. Instead, use the [`hasURLs`](./hasurls.md) property.

## See Also

### Getting and setting pasteboard items of standard data types
- [var string: String?](./string.md)
  The string value of the first pasteboard item.
- [var strings: [String]?](./strings.md)
  An array of strings in all pasteboard items.
- [var image: UIImage?](./image.md)
  The image object of the first pasteboard item.
- [var images: [UIImage]?](./images.md)
  An array of image objects in all pasteboard items.
- [var urls: [URL]?](./urls.md)
  An array of URL objects in all pasteboard items.
- [var color: UIColor?](./color.md)
  The color object of the first pasteboard item.
- [var colors: [UIColor]?](./colors.md)
  An array of color objects in all pasteboard items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/url)*