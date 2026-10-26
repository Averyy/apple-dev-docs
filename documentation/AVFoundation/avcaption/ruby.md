# AVCaption.Ruby

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptionRuby : NSObject
```

#### Overview

Ruby characters are small annotations, typically used in Japanese content, that render alongside the base text.

## Topics

### Creating Ruby text
- [init(text: String)](./ruby/init%28text%29.md)
  Creates ruby text.
- [convenience init(text: String, position: AVCaption.Ruby.Position, alignment: AVCaption.Ruby.Alignment)](./ruby/init%28text,position,alignment%29.md)
  Creates ruby text with position and alignment.
### Accessing text properties
- [var text: String](./ruby/text.md)
  The ruby text.
- [var position: AVCaption.Ruby.Position](./ruby/position-swift.property.md)
  The ruby text position.
- [AVCaption.Ruby.Position](./ruby/position-swift.enum.md)
  Constants that indicate ruby text positions.
- [var alignment: AVCaption.Ruby.Alignment](./ruby/alignment-swift.property.md)
  The ruby text alignment.
- [AVCaption.Ruby.Alignment](./ruby/alignment-swift.enum.md)
  Constants that indicate ruby text alignments.
### Initializers
- [init?(coder: NSCoder)](./ruby/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing advanced typography
- [func ruby(at: String.Index) -> (AVCaption.Ruby?, Range<String.Index>)](./ruby%28at%29.md)
  Returns the ruby text at the index position.
- [func textCombine(at: String.Index) -> (AVCaption.TextCombine, Range<String.Index>)](./textcombine%28at%29.md)
  Returns the text combine at the index position.
- [AVCaption.TextCombine](./textcombine.md)
  The caption’s supported rendering policy options.
- [- rubyAtIndex:range:](./rubyatindex_range_.md)
  Returns the ruby text at the index position.
- [- textCombineAtIndex:range:](./textcombineatindex_range_.md)
  Returns the text combine at the index position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/ruby)*