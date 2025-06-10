# AVCaption.TextCombine

**Framework**: AVFoundation  
**Kind**: enum

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

#### Overview

Text combine is a special rendering policy that combines multiple characters into one unit and presents it in upright position in a vertical text flow. This presentation achieves a horizontal-in-vertical layout (or Tate-Chu-Yoko layout), which lets the caption render a horizontal text string in vertical text.

## Topics

### Text Combine Options
- [AVCaption.TextCombine.all](avcaption/textcombine/all.md)
  An option that combines all of the characters.
- [AVCaption.TextCombine.none](avcaption/textcombine/none.md)
  An option that doesn’t combine text upright.
- [AVCaption.TextCombine.oneDigit](avcaption/textcombine/onedigit.md)
  An option that makes one digit upright.
- [AVCaption.TextCombine.twoDigits](avcaption/textcombine/twodigits.md)
  An option that combines two consecutive digits.
- [AVCaption.TextCombine.threeDigits](avcaption/textcombine/threedigits.md)
  An option that combines three consecutive digits.
- [AVCaption.TextCombine.fourDigits](avcaption/textcombine/fourdigits.md)
  An option that combines four consecutive digits.
### Initializers
- [init?(rawValue: Int)](avcaption/textcombine/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func ruby(at: String.Index) -> (AVCaption.Ruby?, Range<String.Index>)](avcaption/ruby(at:).md)
  Returns the ruby text at the index position.
- [AVCaption.Ruby](avcaption/ruby.md)
  An object that presents ruby characters.
- [func textCombine(at: String.Index) -> (AVCaption.TextCombine, Range<String.Index>)](avcaption/textcombine(at:).md)
  Returns the text combine at the index position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/textcombine)*