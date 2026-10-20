# omitWords

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Omit tokens of type [`word`](../../nslinguistictag/word.md) (items considered to be words).

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
static var omitWords: NSLinguisticTagger.Options { get }
```

```c
NSLinguisticTaggerOmitWords
```

## See Also

### Constants
- [static var omitPunctuation: NSLinguisticTagger.Options](./omitpunctuation.md)
  Omit tokens of type [`punctuation`](../../nslinguistictag/punctuation.md) (all punctuation).
- [static var omitWhitespace: NSLinguisticTagger.Options](./omitwhitespace.md)
  Omit tokens of type [`whitespace`](../../nslinguistictag/whitespace.md) (whitespace of all sorts).
- [static var omitOther: NSLinguisticTagger.Options](./omitother.md)
  Omit tokens of type [`other`](../../nslinguistictag/other.md) (non-linguistic items, such as symbols).
- [static var joinNames: NSLinguisticTagger.Options](./joinnames.md)
  Typically, multiple-word names will be returned as multiple tokens, following the standard tokenization practice of the tagger.  If this option is set, then multiple-word names will be joined together and returned as a single token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/options/omitwords)*