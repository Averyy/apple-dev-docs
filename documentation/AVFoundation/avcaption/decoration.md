# AVCaption.Decoration

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum AVCaptionDecoration : NSUInteger;
```

## Topics

### Decorations
- [static var underline: AVCaption.Decoration](./decoration/underline.md)
  A decoration representing a line under the text.
- [static var lineThrough: AVCaption.Decoration](./decoration/linethrough.md)
  A decoration representing a line through the text.
- [static var overline: AVCaption.Decoration](./decoration/overline.md)
  A decoration representing a line over the text.
- [AVCaptionDecorationNone](../avcaptiondecoration/avcaptiondecorationnone.md)
  No text decoration.
### Initializers
- [init(rawValue: UInt)](./decoration/init%28rawvalue%29.md)
  Creates a caption decoration by using a string.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

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
- [func decoration(at: String.Index) -> (AVCaption.Decoration, Range<String.Index>)](./decoration%28at%29.md)
  Returns the text decoration at the index position.
- [- fontStyleAtIndex:range:](./fontstyleatindex_range_.md)
  Returns the font style and range at the index position.
- [- fontWeightAtIndex:range:](./fontweightatindex_range_.md)
  Returns the font weight and range at the index position.
- [- decorationAtIndex:range:](./decorationatindex_range_.md)
  Returns the text decoration at the index position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/decoration)*