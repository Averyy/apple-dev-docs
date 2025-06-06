# AVCaption.Decoration

**Framework**: AVFoundation  
**Kind**: struct

Text decorations for caption text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct Decoration
```

## Topics

### Decorations
- [static var underline: AVCaption.Decoration](avcaption/decoration/underline.md)
  A decoration representing a line under the text.
- [static var lineThrough: AVCaption.Decoration](avcaption/decoration/linethrough.md)
  A decoration representing a line through the text.
- [static var overline: AVCaption.Decoration](avcaption/decoration/overline.md)
  A decoration representing a line over the text.
### Initializers
- [init(rawValue: UInt)](avcaption/decoration/init(rawvalue:).md)
  Creates a caption decoration by using a string.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func fontStyle(at: String.Index) -> (AVCaption.FontStyle, Range<String.Index>)](avcaption/fontstyle(at:).md)
  Returns the font style and range at the index position.
- [AVCaption.FontStyle](avcaption/fontstyle.md)
  Font styles for caption text.
- [func fontWeight(at: String.Index) -> (AVCaption.FontWeight, Range<String.Index>)](avcaption/fontweight(at:).md)
  Returns the font weight and range at the index position.
- [AVCaption.FontWeight](avcaption/fontweight.md)
  Font weights for a caption.
- [func decoration(at: String.Index) -> (AVCaption.Decoration, Range<String.Index>)](avcaption/decoration(at:).md)
  Returns the text decoration at the index position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/decoration)*