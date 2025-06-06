# NLTokenizer.Attributes

**Framework**: Natural Language  
**Kind**: struct

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

## Topics

### Contents
- [static var emoji: NLTokenizer.Attributes](nltokenizer/attributes/emoji.md)
  The string contains emoji.
- [static var numeric: NLTokenizer.Attributes](nltokenizer/attributes/numeric.md)
  The string contains numbers.
- [static var symbolic: NLTokenizer.Attributes](nltokenizer/attributes/symbolic.md)
  The string contains symbols.
### Initializers
- [init(rawValue: UInt)](nltokenizer/attributes/init(rawvalue:).md)
  Creates an attribute with given value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var string: String?](nltokenizer/string.md)
  The text to be tokenized.
- [func setLanguage(NLLanguage)](nltokenizer/setlanguage(_:).md)
  Sets the language of the text to be tokenized.
- [var unit: NLTokenUnit](nltokenizer/unit.md)
  The linguistic unit that this tokenizer uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/attributes)*