# AVCaption.FontStyle

**Framework**: AVFoundation  
**Kind**: enum

Font styles for caption text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum FontStyle
```

## Topics

### Font Styles
- [AVCaption.FontStyle.unknown](avcaption/fontstyle/unknown.md)
  An unknown font style.
- [AVCaption.FontStyle.normal](avcaption/fontstyle/normal.md)
  A normal font style.
- [AVCaption.FontStyle.italic](avcaption/fontstyle/italic.md)
  An italic font style.
### Initializers
- [init?(rawValue: Int)](avcaption/fontstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func fontStyle(at: String.Index) -> (AVCaption.FontStyle, Range<String.Index>)](avcaption/fontstyle(at:).md)
  Returns the font style and range at the index position.
- [func fontWeight(at: String.Index) -> (AVCaption.FontWeight, Range<String.Index>)](avcaption/fontweight(at:).md)
  Returns the font weight and range at the index position.
- [AVCaption.FontWeight](avcaption/fontweight.md)
  Font weights for a caption.
- [func decoration(at: String.Index) -> (AVCaption.Decoration, Range<String.Index>)](avcaption/decoration(at:).md)
  Returns the text decoration at the index position.
- [AVCaption.Decoration](avcaption/decoration.md)
  Text decorations for caption text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/fontstyle)*