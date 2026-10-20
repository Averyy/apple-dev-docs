# fontWeight(at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the font weight and range at the index position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@nonobjc
func fontWeight(at index: String.Index) -> (AVCaption.FontWeight, Range<String.Index>)
```

#### Return Value

A tuple that contains the font weight and range to which it applies.

## Parameters

- `index`: A character position in the caption text.

## See Also

### Accessing font styles
- [func fontStyle(at: String.Index) -> (AVCaption.FontStyle, Range<String.Index>)](./fontstyle%28at%29.md)
  Returns the font style and range at the index position.
- [AVCaption.FontStyle](./fontstyle.md)
  Font styles for caption text.
- [AVCaption.FontWeight](./fontweight.md)
  Font weights for a caption.
- [func decoration(at: String.Index) -> (AVCaption.Decoration, Range<String.Index>)](./decoration%28at%29.md)
  Returns the text decoration at the index position.
- [AVCaption.Decoration](./decoration.md)
  Text decorations for caption text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/fontweight(at:))*