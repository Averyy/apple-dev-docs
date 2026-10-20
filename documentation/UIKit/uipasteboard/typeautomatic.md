# typeAutomatic

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

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

```c
extern NSString * const UIPasteboardTypeAutomatic;
```

#### Discussion

Use this type in the [`setItems(_:options:)`](./setitems%28_,options%29.md) method to automatically insert appropriate UTIs for supported types. In iOS 10, supported types are [`NSString`](../../Foundation/nsstring.md), [`NSAttributedString`](../../Foundation/nsattributedstring.md), [`NSURL`](../../Foundation/nsurl.md), [`UIImage`](../uiimage.md), and [`UIColor`](../uicolor.md).

## See Also

### Constants
- [class var typeListString: NSArray](./typeliststring.md)
  An array of pasteboard-item representation types for string-type uniform type identifiers (UTIs), including the `kUTTypeUTF8PlainText` and `kUTTypeText` types. Related [`UIPasteboard`](../uipasteboard.md) properties are [`string`](./string.md) and [`strings`](./strings.md).
- [class var typeListURL: NSArray](./typelisturl.md)
  An array of pasteboard-item representation types for URL-type uniform type identifiers (UTIs), including `kUTTypeURL`. Related [`UIPasteboard`](../uipasteboard.md) properties are [`url`](./url.md) and [`urls`](./urls.md).
- [class var typeListImage: NSArray](./typelistimage.md)
  An array of pasteboard-item representation types for image-type uniform type identifiers (UTIs), including `kUTTypePNG` and `kUTTypeJPEG`. Related [`UIPasteboard`](../uipasteboard.md) properties are [`image`](./image.md) and [`images`](./images.md).
- [class var typeListColor: NSArray](./typelistcolor.md)
  An array of pasteboard-item representation types for colors. Related [`UIPasteboard`](../uipasteboard.md) properties are [`color`](./color.md) and [`colors`](./colors.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/typeautomatic)*