# makeAttributedString(font:foregroundColor:textAlignment:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Convenience method for configuring an attributed string given the specified attributes.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
func makeAttributedString(font: UIFont, foregroundColor: UIColor?, textAlignment alignment: NSTextAlignment) -> NSAttributedString
```

```objc
- (NSAttributedString *) attributedStringWithFont:(UIFont *) font foregroundColor:(UIColor *) foregroundColor textAlignment:(NSTextAlignment) alignment;
```

#### Return Value

An [`NSAttributedString`](../../Foundation/nsattributedstring.md) object with the applied attributes.

#### Discussion

Supply a font to this method to get the [`NSAttributedString`](../../Foundation/nsattributedstring.md) representation of the text contained within an element. Use the `foregroundColor` and `alignment` parameters to override the value specified in the text element.

## Parameters

- `font`: The font used for the attributed string. This can be any available font on the device.
- `foregroundColor`: The foreground color for the element.
- `alignment`: The alignment for the text contained within the element.

## See Also

### Creating Attributed Strings
- [func makeAttributedString(font: UIFont) -> NSAttributedString](./makeattributedstring%28font%29.md)
  Provides an attributed string for a given font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvtextelement/makeattributedstring(font:foregroundcolor:textalignment:))*