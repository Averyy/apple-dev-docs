# fontStyleAtIndex:range:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the font style and range at the index position.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS

## Declaration

```objc
- (AVCaptionFontStyle) fontStyleAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

## Return Value

The font style.

## Parameters

- `index`: A character position in the caption text.
- `outRange`: A pointer that stores the range to which the returned style applies.

## See Also

### Accessing font styles
- [AVCaption.FontStyle](./fontstyle.md)
  Font styles for caption text.
- [- fontWeightAtIndex:range:](./fontweightatindex_range_.md)
  Returns the font weight and range at the index position.
- [AVCaption.FontWeight](./fontweight.md)
  Font weights for a caption.
- [- decorationAtIndex:range:](./decorationatindex_range_.md)
  Returns the text decoration at the index position.
- [AVCaption.Decoration](./decoration.md)
  Text decorations for caption text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/fontstyleatindex:range:)*