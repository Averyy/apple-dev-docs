# makeAttributedString(font:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Provides an attributed string for a given font.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
func makeAttributedString(font: UIFont) -> NSAttributedString
```

```objc
- (NSAttributedString *) attributedStringWithFont:(UIFont *) font;
```

#### Return Value

An [`NSAttributedString`](../../Foundation/nsattributedstring.md) object with the supplied font.

#### Discussion

Supply a font to this method to get the [`NSAttributedString`](../../Foundation/nsattributedstring.md) representation of the text contained within an element.

## Parameters

- `font`: The font used for the attributed string. This can be any available font on the device.

## See Also

### Creating Attributed Strings
- [func makeAttributedString(font: UIFont, foregroundColor: UIColor?, textAlignment: NSTextAlignment) -> NSAttributedString](./makeattributedstring%28font,foregroundcolor,textalignment%29.md)
  Convenience method for configuring an attributed string given the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvtextelement/makeattributedstring(font:))*