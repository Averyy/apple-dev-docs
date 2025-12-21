# AVCaption.Ruby

**Framework**: AVFoundation  
**Kind**: class

An object that presents ruby characters.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class Ruby
```

#### Overview

Ruby characters are small annotations, typically used in Japanese content, that render alongside the base text.

## Topics

### Creating Ruby text
- [init(text: String)](avcaption/ruby/init(text:).md)
  Creates ruby text.
- [convenience init(text: String, position: AVCaptionRubyPosition, alignment: AVCaptionRubyAlignment)](avcaption/ruby/init(text:position:alignment:).md)
  Creates ruby text with position and alignment.
### Accessing text properties
- [var text: String](avcaption/ruby/text.md)
  The ruby text.
- [var position: AVCaptionRubyPosition](avcaption/ruby/position.md)
  The ruby text position.
- [enum AVCaptionRubyPosition](avcaptionrubyposition.md)
  Constants that indicate ruby text positions.
- [var alignment: AVCaptionRubyAlignment](avcaption/ruby/alignment.md)
  The ruby text alignment.
- [enum AVCaptionRubyAlignment](avcaptionrubyalignment.md)
  Constants that indicate ruby text alignments.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func ruby(at: String.Index) -> (AVCaption.Ruby?, Range<String.Index>)](avcaption/ruby(at:).md)
  Returns the ruby text at the index position.
- [func textCombine(at: String.Index) -> (AVCaption.TextCombine, Range<String.Index>)](avcaption/textcombine(at:).md)
  Returns the text combine at the index position.
- [AVCaption.TextCombine](avcaption/textcombine.md)
  The caption’s supported rendering policy options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/ruby)*