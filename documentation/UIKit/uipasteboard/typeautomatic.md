# typeAutomatic

**Framework**: UIKit  
**Kind**: property

An array of pasteboard-item representation types with automatically-determined uniform type identifiers (UTIs).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class let typeAutomatic: String
```

#### Discussion

Use this type in the [`setItems(_:options:)`](uipasteboard/setitems(_:options:).md) method to automatically insert appropriate UTIs for supported types. In iOS 10, supported types are [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString), [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL), [`UIImage`](uiimage.md), and [`UIColor`](uicolor.md).

## See Also

- [class var typeListString: NSArray](uipasteboard/typeliststring.md)
  An array of pasteboard-item representation types for string-type uniform type identifiers (UTIs), including the `kUTTypeUTF8PlainText` and `kUTTypeText` types. Related [`UIPasteboard`](uipasteboard.md) properties are [`string`](uipasteboard/string.md) and [`strings`](uipasteboard/strings.md).
- [class var typeListURL: NSArray](uipasteboard/typelisturl.md)
  An array of pasteboard-item representation types for URL-type uniform type identifiers (UTIs), including `kUTTypeURL`. Related [`UIPasteboard`](uipasteboard.md) properties are [`url`](uipasteboard/url.md) and [`urls`](uipasteboard/urls.md).
- [class var typeListImage: NSArray](uipasteboard/typelistimage.md)
  An array of pasteboard-item representation types for image-type uniform type identifiers (UTIs), including `kUTTypePNG` and `kUTTypeJPEG`. Related [`UIPasteboard`](uipasteboard.md) properties are [`image`](uipasteboard/image.md) and [`images`](uipasteboard/images.md).
- [class var typeListColor: NSArray](uipasteboard/typelistcolor.md)
  An array of pasteboard-item representation types for colors. Related [`UIPasteboard`](uipasteboard.md) properties are [`color`](uipasteboard/color.md) and [`colors`](uipasteboard/colors.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/typeautomatic)*