# decoration(at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the text decoration at the index position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@nonobjc
func decoration(at index: String.Index) -> (AVCaption.Decoration, Range<String.Index>)
```

## Return Value

A tuple that contains the text decoration and range to which it applies.

## Parameters

- `index`: A character position in the caption text.

## See Also

### Accessing font styles
- [func fontStyle(at: String.Index) -> (AVCaption.FontStyle, Range<String.Index>)](./fontstyle%28at%29.md)
  Returns the font style and range at the index position.
- [AVCaption.FontStyle](./fontstyle.md)
  Font styles for caption text.
- [func fontWeight(at: String.Index) -> (AVCaption.FontWeight, Range<String.Index>)](./fontweight%28at%29.md)
  Returns the font weight and range at the index position.
- [AVCaption.FontWeight](./fontweight.md)
  Font weights for a caption.
- [AVCaption.Decoration](./decoration.md)
  Text decorations for caption text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/decoration(at:))*