# AVCaption.Ruby.Position

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate ruby text positions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum Position
```

```c
enum AVCaptionRubyPosition : NSInteger;
```

## Topics

### Ruby positions
- [AVCaption.Ruby.Position.before](./position-swift.enum/before.md)
  Display ruby text above horizontal text, or to the right of vertical text in a right-to-left block progression.
- [AVCaption.Ruby.Position.after](./position-swift.enum/after.md)
  Display ruby text below horizontal text, or to the left of vertical text in a right-to-left block progression.
### Initializers
- [init?(rawValue: Int)](./position-swift.enum/init%28rawvalue%29.md)

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
- [var alignment: AVCaption.Ruby.Alignment](./alignment-swift.property.md)
  The ruby text alignment.
- [AVCaption.Ruby.Alignment](./alignment-swift.enum.md)
  Constants that indicate ruby text alignments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/ruby/position-swift.enum)*