# AVCaptionRubyAlignment

**Framework**: AVFoundation  
**Kind**: enum

Constants that indicate ruby text alignments.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum AVCaptionRubyAlignment
```

## Topics

### Text Alignments
- [AVCaptionRubyAlignment.start](avcaptionrubyalignment/start.md)
  An alignment with the ruby base and text at the left edge of horizontal text in a left-to-right inline progression, or at top of the vertical text in a top-to-bottom inline progression.
- [AVCaptionRubyAlignment.center](avcaptionrubyalignment/center.md)
  An alignment with the ruby text at the center of ruby base.
- [AVCaptionRubyAlignment.distributeSpaceBetween](avcaptionrubyalignment/distributespacebetween.md)
  An alignment with the ruby text so the spaces between the ruby text characters are equal.
- [AVCaptionRubyAlignment.distributeSpaceAround](avcaptionrubyalignment/distributespacearound.md)
  An alignment with the ruby text so the spaces around each ruby text character are equal.
### Initializers
- [init?(rawValue: Int)](avcaptionrubyalignment/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var text: String](avcaption/ruby/text.md)
  The ruby text.
- [var position: AVCaptionRubyPosition](avcaption/ruby/position.md)
  The ruby text position.
- [enum AVCaptionRubyPosition](avcaptionrubyposition.md)
  Constants that indicate ruby text positions.
- [var alignment: AVCaptionRubyAlignment](avcaption/ruby/alignment.md)
  The ruby text alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrubyalignment)*