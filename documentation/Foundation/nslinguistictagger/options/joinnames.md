# joinNames

**Framework**: Foundation  
**Kind**: property

Typically, multiple-word names will be returned as multiple tokens, following the standard tokenization practice of the tagger.  If this option is set, then multiple-word names will be joined together and returned as a single token.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var joinNames: NSLinguisticTagger.Options { get }
```

## See Also

- [static var omitWords: NSLinguisticTagger.Options](nslinguistictagger/options/omitwords.md)
  Omit tokens of type [`word`](nslinguistictag/word.md) (items considered to be words).
- [static var omitPunctuation: NSLinguisticTagger.Options](nslinguistictagger/options/omitpunctuation.md)
  Omit tokens of type [`punctuation`](nslinguistictag/punctuation.md) (all punctuation).
- [static var omitWhitespace: NSLinguisticTagger.Options](nslinguistictagger/options/omitwhitespace.md)
  Omit tokens of type [`whitespace`](nslinguistictag/whitespace.md) (whitespace of all sorts).
- [static var omitOther: NSLinguisticTagger.Options](nslinguistictagger/options/omitother.md)
  Omit tokens of type [`other`](nslinguistictag/other.md) (non-linguistic items, such as symbols).
- [static var omitWords: NSLinguisticTagger.Options](nslinguistictagger/options/omitwords.md)
  Omit tokens of type [`word`](nslinguistictag/word.md) (items considered to be words).
- [static var omitPunctuation: NSLinguisticTagger.Options](nslinguistictagger/options/omitpunctuation.md)
  Omit tokens of type [`punctuation`](nslinguistictag/punctuation.md) (all punctuation).
- [static var omitWhitespace: NSLinguisticTagger.Options](nslinguistictagger/options/omitwhitespace.md)
  Omit tokens of type [`whitespace`](nslinguistictag/whitespace.md) (whitespace of all sorts).
- [static var omitOther: NSLinguisticTagger.Options](nslinguistictagger/options/omitother.md)
  Omit tokens of type [`other`](nslinguistictag/other.md) (non-linguistic items, such as symbols).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/options/joinnames)*