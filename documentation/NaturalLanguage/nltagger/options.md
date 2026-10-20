# NLTagger.Options

**Framework**: Natural Language  
**Kind**: struct  
**Role**: Structure

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

```c
enum NLTaggerOptions : NSUInteger;
```

## Topics

### Constants
- [static var omitWords: NLTagger.Options](./options/omitwords.md)
  Omit tokens of type [`word`](../nltag/word.md) (items considered to be words).
- [static var omitPunctuation: NLTagger.Options](./options/omitpunctuation.md)
  Omit tokens of type [`punctuation`](../nltag/punctuation.md) (all punctuation).
- [static var omitWhitespace: NLTagger.Options](./options/omitwhitespace.md)
  Omit tokens of type [`whitespace`](../nltag/whitespace.md) (whitespace of all sorts).
- [static var omitOther: NLTagger.Options](./options/omitother.md)
  Omit tokens of type [`other`](../nltag/other.md) (non-linguistic items, such as symbols).
- [static var joinNames: NLTagger.Options](./options/joinnames.md)
  Typically, multiple-word names will be returned as multiple tokens, following the standard tokenization practice of the tagger.
- [static var joinContractions: NLTagger.Options](./options/joincontractions.md)
  Contractions will be returned as one token.
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)
  Creates the option with a raw value.

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

### Enumerating linguistic tags
- [func enumerateTags(in: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options, using: (NLTag?, Range<String.Index>) -> Bool)](./enumeratetags%28in,unit,scheme,options,using%29.md)
  Enumerates a block over the tagger’s string, given a range, token unit, and tag scheme.
- [struct NLTag](../nltag.md)
  A token type, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/options)*