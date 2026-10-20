# setFontStyle(_:in:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the font style for a range of text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@nonobjc
func setFontStyle(_ fontStyle: AVCaption.FontStyle, in range: NSRange)
```

## Parameters

- `fontStyle`: The font style.
- `range`: The range to which this style applies.

## See Also

### Configuring font styles
- [AVCaption.FontStyle](../avcaption/fontstyle.md)
  Font styles for caption text.
- [func removeFontStyle(in: NSRange)](./removefontstyle%28in%29.md)
  Removes a font style from a range of text.
- [AVCaption.FontWeight](../avcaption/fontweight.md)
  Font weights for a caption.
- [func setFontWeight(AVCaption.FontWeight, in: NSRange)](./setfontweight%28_,in%29.md)
  Sets the font weight for a range of text.
- [func removeFontWeight(in: NSRange)](./removefontweight%28in%29.md)
  Removes a font weight from a range of text.
- [AVCaption.Decoration](../avcaption/decoration.md)
  Text decorations for caption text.
- [func setDecoration(AVCaption.Decoration, in: NSRange)](./setdecoration%28_,in%29.md)
  Sets a decoration for a range of text.
- [func removeDecoration(in: NSRange)](./removedecoration%28in%29.md)
  Removes a decoration from a range of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaption/setfontstyle(_:in:))*