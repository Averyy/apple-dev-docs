# AVCaption.Ruby.Alignment

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate ruby text alignments.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum Alignment
```

```c
enum AVCaptionRubyAlignment : NSInteger;
```

## Topics

### Text alignments
- [AVCaption.Ruby.Alignment.start](./alignment-swift.enum/start.md)
  An alignment with the ruby base and text at the left edge of horizontal text in a left-to-right inline progression, or at top of the vertical text in a top-to-bottom inline progression.
- [AVCaption.Ruby.Alignment.center](./alignment-swift.enum/center.md)
  An alignment with the ruby text at the center of ruby base.
- [AVCaption.Ruby.Alignment.distributeSpaceBetween](./alignment-swift.enum/distributespacebetween.md)
  An alignment with the ruby text so the spaces between the ruby text characters are equal.
- [AVCaption.Ruby.Alignment.distributeSpaceAround](./alignment-swift.enum/distributespacearound.md)
  An alignment with the ruby text so the spaces around each ruby text character are equal.
### Initializers
- [init?(rawValue: Int)](./alignment-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing text properties
- [var text: String](./text.md)
  The ruby text.
- [var position: AVCaption.Ruby.Position](./position-swift.property.md)
  The ruby text position.
- [AVCaption.Ruby.Position](./position-swift.enum.md)
  Constants that indicate ruby text positions.
- [var alignment: AVCaption.Ruby.Alignment](./alignment-swift.property.md)
  The ruby text alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/ruby/alignment-swift.enum)*