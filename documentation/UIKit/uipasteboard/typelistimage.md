# typeListImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

An array of pasteboard-item representation types for image-type uniform type identifiers (UTIs), including `kUTTypePNG` and `kUTTypeJPEG`. Related [`UIPasteboard`](../uipasteboard.md) properties are [`image`](./image.md) and [`images`](./images.md).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
class var typeListImage: NSArray
```

```c
extern NSArray<NSString *> * UIPasteboardTypeListImage;
```

## See Also

### Constants
- [class var typeListString: NSArray](./typeliststring.md)
  An array of pasteboard-item representation types for string-type uniform type identifiers (UTIs), including the `kUTTypeUTF8PlainText` and `kUTTypeText` types. Related [`UIPasteboard`](../uipasteboard.md) properties are [`string`](./string.md) and [`strings`](./strings.md).
- [class var typeListURL: NSArray](./typelisturl.md)
  An array of pasteboard-item representation types for URL-type uniform type identifiers (UTIs), including `kUTTypeURL`. Related [`UIPasteboard`](../uipasteboard.md) properties are [`url`](./url.md) and [`urls`](./urls.md).
- [class var typeListColor: NSArray](./typelistcolor.md)
  An array of pasteboard-item representation types for colors. Related [`UIPasteboard`](../uipasteboard.md) properties are [`color`](./color.md) and [`colors`](./colors.md).
- [class let typeAutomatic: String](./typeautomatic.md)
  An array of pasteboard-item representation types with automatically-determined uniform type identifiers (UTIs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/typelistimage)*