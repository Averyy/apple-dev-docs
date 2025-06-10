# AVCaption.FontWeight

**Framework**: AVFoundation  
**Kind**: enum

Font weights for a caption.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum FontWeight
```

## Topics

### Font Weights
- [AVCaption.FontWeight.unknown](avcaption/fontweight/unknown.md)
  An unknown font weight.
- [AVCaption.FontWeight.normal](avcaption/fontweight/normal.md)
  A normal font weight.
- [AVCaption.FontWeight.bold](avcaption/fontweight/bold.md)
  A bold font weight.
### Initializers
- [init?(rawValue: Int)](avcaption/fontweight/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func fontStyle(at: String.Index) -> (AVCaption.FontStyle, Range<String.Index>)](avcaption/fontstyle(at:).md)
  Returns the font style and range at the index position.
- [AVCaption.FontStyle](avcaption/fontstyle.md)
  Font styles for caption text.
- [func fontWeight(at: String.Index) -> (AVCaption.FontWeight, Range<String.Index>)](avcaption/fontweight(at:).md)
  Returns the font weight and range at the index position.
- [func decoration(at: String.Index) -> (AVCaption.Decoration, Range<String.Index>)](avcaption/decoration(at:).md)
  Returns the text decoration at the index position.
- [AVCaption.Decoration](avcaption/decoration.md)
  Text decorations for caption text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/fontweight)*