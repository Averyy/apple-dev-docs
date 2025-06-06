# setFontWeight(_:in:)

**Framework**: AVFoundation  
**Kind**: method

Sets the font weight for a range of text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@nonobjc
func setFontWeight(_ fontWeight: AVCaption.FontWeight, in range: NSRange)
```

## Parameters

- `fontWeight`: The font weight.
- `range`: The range to which this font weight applies.

## See Also

- [AVCaption.FontStyle](avcaption/fontstyle.md)
  Font styles for caption text.
- [func setFontStyle(AVCaption.FontStyle, in: NSRange)](avmutablecaption/setfontstyle(_:in:).md)
  Sets the font style for a range of text.
- [func removeFontStyle(in: NSRange)](avmutablecaption/removefontstyle(in:).md)
  Removes a font style from a range of text.
- [AVCaption.FontWeight](avcaption/fontweight.md)
  Font weights for a caption.
- [func removeFontWeight(in: NSRange)](avmutablecaption/removefontweight(in:).md)
  Removes a font weight from a range of text.
- [AVCaption.Decoration](avcaption/decoration.md)
  Text decorations for caption text.
- [func setDecoration(AVCaption.Decoration, in: NSRange)](avmutablecaption/setdecoration(_:in:).md)
  Sets a decoration for a range of text.
- [func removeDecoration(in: NSRange)](avmutablecaption/removedecoration(in:).md)
  Removes a decoration from a range of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaption/setfontweight(_:in:))*