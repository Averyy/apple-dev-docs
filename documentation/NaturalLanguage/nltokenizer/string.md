# string

**Framework**: Natural Language  
**Kind**: property  
**Role**: Instance Property

The text to be tokenized.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var string: String? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSString * string;
```

## Mentions

- [Tokenizing natural language text](../tokenizing-natural-language-text.md)

## See Also

### Configuring a tokenizer
- [func setLanguage(NLLanguage)](./setlanguage%28_%29.md)
  Sets the language of the text to be tokenized.
- [var unit: NLTokenUnit](./unit.md)
  The linguistic unit that this tokenizer uses.
- [NLTokenizer.Attributes](./attributes.md)
  Hints about the contents of the string for the tokenizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/string)*