# AVCaption.FontWeight

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVCaptionFontWeight : NSInteger;
```

## Topics

### Font weights
- [AVCaption.FontWeight.unknown](./fontweight/unknown.md)
  An unknown font weight.
- [AVCaption.FontWeight.normal](./fontweight/normal.md)
  A normal font weight.
- [AVCaption.FontWeight.bold](./fontweight/bold.md)
  A bold font weight.
### Initializers
- [init?(rawValue: Int)](./fontweight/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing font styles
- [func fontStyle(at: String.Index) -> (AVCaption.FontStyle, Range<String.Index>)](./fontstyle%28at%29.md)
  Returns the font style and range at the index position.
- [AVCaption.FontStyle](./fontstyle.md)
  Font styles for caption text.
- [func fontWeight(at: String.Index) -> (AVCaption.FontWeight, Range<String.Index>)](./fontweight%28at%29.md)
  Returns the font weight and range at the index position.
- [func decoration(at: String.Index) -> (AVCaption.Decoration, Range<String.Index>)](./decoration%28at%29.md)
  Returns the text decoration at the index position.
- [AVCaption.Decoration](./decoration.md)
  Text decorations for caption text.
- [- fontStyleAtIndex:range:](./fontstyleatindex_range_.md)
  Returns the font style and range at the index position.
- [- fontWeightAtIndex:range:](./fontweightatindex_range_.md)
  Returns the font weight and range at the index position.
- [- decorationAtIndex:range:](./decorationatindex_range_.md)
  Returns the text decoration at the index position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/fontweight)*