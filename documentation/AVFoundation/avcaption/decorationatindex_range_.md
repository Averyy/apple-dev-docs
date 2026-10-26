# decorationAtIndex:range:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the text decoration at the index position.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS

## Declaration

```objc
- (AVCaptionDecoration) decorationAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

#### Return Value

The text decoration.

## Parameters

- `index`: A character position in the caption text.
- `outRange`: A pointer to store the range to which the returned decoration applies.

## See Also

### Accessing font styles
- [- fontStyleAtIndex:range:](./fontstyleatindex_range_.md)
  Returns the font style and range at the index position.
- [AVCaption.FontStyle](./fontstyle.md)
  Font styles for caption text.
- [- fontWeightAtIndex:range:](./fontweightatindex_range_.md)
  Returns the font weight and range at the index position.
- [AVCaption.FontWeight](./fontweight.md)
  Font weights for a caption.
- [AVCaption.Decoration](./decoration.md)
  Text decorations for caption text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/decorationatindex:range:)*