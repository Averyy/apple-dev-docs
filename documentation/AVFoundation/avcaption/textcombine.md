# AVCaption.TextCombine

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

The caption’s supported rendering policy options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum TextCombine
```

```c
enum AVCaptionTextCombine : NSInteger;
```

## Overview

Text combine is a special rendering policy that combines multiple characters into one unit and presents it in upright position in a vertical text flow. This presentation achieves a horizontal-in-vertical layout (or Tate-Chu-Yoko layout), which lets the caption render a horizontal text string in vertical text.

## Topics

### Text combine options
- [AVCaption.TextCombine.all](./textcombine/all.md)
  An option that combines all of the characters.
- [AVCaption.TextCombine.none](./textcombine/none.md)
  An option that doesn’t combine text upright.
- [AVCaption.TextCombine.oneDigit](./textcombine/onedigit.md)
  An option that makes one digit upright.
- [AVCaption.TextCombine.twoDigits](./textcombine/twodigits.md)
  An option that combines two consecutive digits.
- [AVCaption.TextCombine.threeDigits](./textcombine/threedigits.md)
  An option that combines three consecutive digits.
- [AVCaption.TextCombine.fourDigits](./textcombine/fourdigits.md)
  An option that combines four consecutive digits.
### Initializers
- [init?(rawValue: Int)](./textcombine/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing advanced typography
- [func ruby(at: String.Index) -> (AVCaption.Ruby?, Range<String.Index>)](./ruby%28at%29.md)
  Returns the ruby text at the index position.
- [AVCaption.Ruby](./ruby.md)
  An object that presents ruby characters.
- [func textCombine(at: String.Index) -> (AVCaption.TextCombine, Range<String.Index>)](./textcombine%28at%29.md)
  Returns the text combine at the index position.
- [- rubyAtIndex:range:](./rubyatindex_range_.md)
  Returns the ruby text at the index position.
- [- textCombineAtIndex:range:](./textcombineatindex_range_.md)
  Returns the text combine at the index position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/textcombine)*