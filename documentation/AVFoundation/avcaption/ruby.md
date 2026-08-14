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
- [convenience init(text: String, position: AVCaption.Ruby.Position, alignment: AVCaption.Ruby.Alignment)](avcaption/ruby/init(text:position:alignment:).md)
  Creates ruby text with position and alignment.
### Accessing text properties
- [var text: String](avcaption/ruby/text.md)
  The ruby text.
- [var position: AVCaption.Ruby.Position](avcaption/ruby/position-swift.property.md)
  The ruby text position.
- [AVCaption.Ruby.Position](avcaption/ruby/position-swift.enum.md)
  Constants that indicate ruby text positions.
- [var alignment: AVCaption.Ruby.Alignment](avcaption/ruby/alignment-swift.property.md)
  The ruby text alignment.
- [AVCaption.Ruby.Alignment](avcaption/ruby/alignment-swift.enum.md)
  Constants that indicate ruby text alignments.
### Initializers
- [init?(coder: NSCoder)](avcaption/ruby/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func ruby(at: String.Index) -> (AVCaption.Ruby?, Range<String.Index>)](avcaption/ruby(at:).md)
  Returns the ruby text at the index position.
- [func textCombine(at: String.Index) -> (AVCaption.TextCombine, Range<String.Index>)](avcaption/textcombine(at:).md)
  Returns the text combine at the index position.
- [AVCaption.TextCombine](avcaption/textcombine.md)
  The caption’s supported rendering policy options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/ruby)*