# AVCaption.FontStyle

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVCaptionFontStyle : NSInteger;
```

## Topics

### Font styles
- [AVCaption.FontStyle.unknown](./fontstyle/unknown.md)
  An unknown font style.
- [AVCaption.FontStyle.normal](./fontstyle/normal.md)
  A normal font style.
- [AVCaption.FontStyle.italic](./fontstyle/italic.md)
  An italic font style.
### Initializers
- [init?(rawValue: Int)](./fontstyle/init%28rawvalue%29.md)

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
- [func fontWeight(at: String.Index) -> (AVCaption.FontWeight, Range<String.Index>)](./fontweight%28at%29.md)
  Returns the font weight and range at the index position.
- [AVCaption.FontWeight](./fontweight.md)
  Font weights for a caption.
- [func decoration(at: String.Index) -> (AVCaption.Decoration, Range<String.Index>)](./decoration%28at%29.md)
  Returns the text decoration at the index position.
- [AVCaption.Decoration](./decoration.md)
  Text decorations for caption text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/fontstyle)*