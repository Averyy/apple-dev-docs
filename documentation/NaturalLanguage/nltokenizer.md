# NLTokenizer

**Framework**: Natural Language  
**Kind**: class

A tokenizer that segments natural language text into semantic units.

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
class NLTokenizer
```

## Mentions

- [Tokenizing natural language text](tokenizing-natural-language-text.md)

#### Overview

[`NLTokenizer`](nltokenizer.md) creates individual units from natural language text. Define the desired unit (word, sentence, paragraph, or document as declared in the [`NLTokenUnit`](nltokenunit.md)) for tokenization, and then assign a string to tokenize. The [`enumerateTokensInRange:usingBlock:`](nltokenizer/enumeratetokensinrange:usingblock:.md) method provides the ranges of the tokens in the string based on the tokenization unit.

For more information, see [`Tokenizing natural language text`](tokenizing-natural-language-text.md).

> ❗ **Important**:  Use an [`NLTokenizer`](nltokenizer.md) instance on one thread or one dispatch queue at a time. You do this by either serializing method calls to the tokenizer, or by creating a separate tokenizer instance for each thread and dispatch queue.

## Topics

### Creating a tokenizer
- [init(unit: NLTokenUnit)](nltokenizer/init(unit:).md)
  Creates a tokenizer with the specified unit.
### Configuring a tokenizer
- [var string: String?](nltokenizer/string.md)
  The text to be tokenized.
- [func setLanguage(NLLanguage)](nltokenizer/setlanguage(_:).md)
  Sets the language of the text to be tokenized.
- [var unit: NLTokenUnit](nltokenizer/unit.md)
  The linguistic unit that this tokenizer uses.
- [NLTokenizer.Attributes](nltokenizer/attributes.md)
  Hints about the contents of the string for the tokenizer.
### Enumerating the tokens
- [func enumerateTokens(in: Range<String.Index>, using: (Range<String.Index>, NLTokenizer.Attributes) -> Bool)](nltokenizer/enumeratetokens(in:using:).md)
  Enumerates over a given range of the string and calls the specified block for each token.
- [func tokens(for: Range<String.Index>) -> [Range<String.Index>]](nltokenizer/tokens(for:).md)
  Tokenizes the string within the provided range.
- [func tokenRange(at: String.Index) -> Range<String.Index>](nltokenizer/tokenrange(at:).md)
  Finds the range of the token at the given index.
- [func tokenRange(for: Range<String.Index>) -> Range<String.Index>](nltokenizer/tokenrange(for:).md)
  Finds the entire range of all tokens contained completely or partially within the specified range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Tokenizing natural language text](tokenizing-natural-language-text.md)
  Enumerate the words in a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer)*