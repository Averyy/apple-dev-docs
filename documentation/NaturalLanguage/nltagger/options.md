# NLTagger.Options

**Framework**: Natural Language  
**Kind**: struct

Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.

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
struct Options
```

## Topics

### Constants
- [static var omitWords: NLTagger.Options](nltagger/options/omitwords.md)
  Omit tokens of type [`word`](nltag/word.md) (items considered to be words).
- [static var omitPunctuation: NLTagger.Options](nltagger/options/omitpunctuation.md)
  Omit tokens of type [`punctuation`](nltag/punctuation.md) (all punctuation).
- [static var omitWhitespace: NLTagger.Options](nltagger/options/omitwhitespace.md)
  Omit tokens of type [`whitespace`](nltag/whitespace.md) (whitespace of all sorts).
- [static var omitOther: NLTagger.Options](nltagger/options/omitother.md)
  Omit tokens of type [`other`](nltag/other.md) (non-linguistic items, such as symbols).
- [static var joinNames: NLTagger.Options](nltagger/options/joinnames.md)
  Typically, multiple-word names will be returned as multiple tokens, following the standard tokenization practice of the tagger.
- [static var joinContractions: NLTagger.Options](nltagger/options/joincontractions.md)
  Contractions will be returned as one token.
### Initializers
- [init(rawValue: UInt)](nltagger/options/init(rawvalue:).md)
  Creates the option with a raw value.

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

- [func enumerateTags(in: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options, using: (NLTag?, Range<String.Index>) -> Bool)](nltagger/enumeratetags(in:unit:scheme:options:using:).md)
  Enumerates a block over the tagger’s string, given a range, token unit, and tag scheme.
- [struct NLTag](nltag.md)
  A token type, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/options)*