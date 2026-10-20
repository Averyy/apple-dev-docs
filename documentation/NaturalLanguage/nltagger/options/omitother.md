# omitOther

**Framework**: Natural Language  
**Kind**: property  
**Role**: Type Property

Omit tokens of type [`other`](../../nltag/other.md) (non-linguistic items, such as symbols).

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
static var omitOther: NLTagger.Options { get }
```

```c
NLTaggerOmitOther
```

## See Also

### Constants
- [static var omitWords: NLTagger.Options](./omitwords.md)
  Omit tokens of type [`word`](../../nltag/word.md) (items considered to be words).
- [static var omitPunctuation: NLTagger.Options](./omitpunctuation.md)
  Omit tokens of type [`punctuation`](../../nltag/punctuation.md) (all punctuation).
- [static var omitWhitespace: NLTagger.Options](./omitwhitespace.md)
  Omit tokens of type [`whitespace`](../../nltag/whitespace.md) (whitespace of all sorts).
- [static var joinNames: NLTagger.Options](./joinnames.md)
  Typically, multiple-word names will be returned as multiple tokens, following the standard tokenization practice of the tagger.
- [static var joinContractions: NLTagger.Options](./joincontractions.md)
  Contractions will be returned as one token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/options/omitother)*