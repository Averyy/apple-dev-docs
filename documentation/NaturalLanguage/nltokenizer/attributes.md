# NLTokenizer.Attributes

**Framework**: Natural Language  
**Kind**: struct  
**Role**: Structure

Hints about the contents of the string for the tokenizer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
struct Attributes
```

```c
enum NLTokenizerAttributes : NSUInteger;
```

## Topics

### Contents
- [static var emoji: NLTokenizer.Attributes](./attributes/emoji.md)
  The string contains emoji.
- [static var numeric: NLTokenizer.Attributes](./attributes/numeric.md)
  The string contains numbers.
- [static var symbolic: NLTokenizer.Attributes](./attributes/symbolic.md)
  The string contains symbols.
### Initializers
- [init(rawValue: UInt)](./attributes/init%28rawvalue%29.md)
  Creates an attribute with given value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Configuring a tokenizer
- [var string: String?](./string.md)
  The text to be tokenized.
- [func setLanguage(NLLanguage)](./setlanguage%28_%29.md)
  Sets the language of the text to be tokenized.
- [var unit: NLTokenUnit](./unit.md)
  The linguistic unit that this tokenizer uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/attributes)*