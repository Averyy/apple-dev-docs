# Pasteboard Data Type Representations

**Framework**: UIKit

Pasteboard-item representation types, as for a given object value.

## Topics

### Constants
- [class var typeListString: NSArray](uipasteboard/typeliststring.md)
  An array of pasteboard-item representation types for string-type uniform type identifiers (UTIs), including the `kUTTypeUTF8PlainText` and `kUTTypeText` types. Related [`UIPasteboard`](uipasteboard.md) properties are [`string`](uipasteboard/string.md) and [`strings`](uipasteboard/strings.md).
- [class var typeListURL: NSArray](uipasteboard/typelisturl.md)
  An array of pasteboard-item representation types for URL-type uniform type identifiers (UTIs), including `kUTTypeURL`. Related [`UIPasteboard`](uipasteboard.md) properties are [`url`](uipasteboard/url.md) and [`urls`](uipasteboard/urls.md).
- [class var typeListImage: NSArray](uipasteboard/typelistimage.md)
  An array of pasteboard-item representation types for image-type uniform type identifiers (UTIs), including `kUTTypePNG` and `kUTTypeJPEG`. Related [`UIPasteboard`](uipasteboard.md) properties are [`image`](uipasteboard/image.md) and [`images`](uipasteboard/images.md).
- [class var typeListColor: NSArray](uipasteboard/typelistcolor.md)
  An array of pasteboard-item representation types for colors. Related [`UIPasteboard`](uipasteboard.md) properties are [`color`](uipasteboard/color.md) and [`colors`](uipasteboard/colors.md).
- [class let typeAutomatic: String](uipasteboard/typeautomatic.md)
  An array of pasteboard-item representation types with automatically-determined uniform type identifiers (UTIs).

## See Also

- [UIPasteboard.Name](uipasteboard/name-swift.struct.md)
  Constants that identify the name of a pasteboard.
- [Pasteboard Names](pasteboard-names.md)
  Names identifying the system pasteboards.
- [UIPasteboard.OptionsKey](uipasteboard/optionskey.md)
  Options for describing pasteboard privacy.
- [UserInfo Dictionary Keys](userinfo-dictionary-keys.md)
  Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/pasteboard-data-type-representations)*