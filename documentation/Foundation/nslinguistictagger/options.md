# NSLinguisticTagger.Options

**Framework**: Foundation  
**Kind**: struct

Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.

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
struct Options
```

## Topics

### Constants
- [static var omitWords: NSLinguisticTagger.Options](nslinguistictagger/options/omitwords.md)
  Omit tokens of type [`word`](nslinguistictag/word.md) (items considered to be words).
- [static var omitPunctuation: NSLinguisticTagger.Options](nslinguistictagger/options/omitpunctuation.md)
  Omit tokens of type [`punctuation`](nslinguistictag/punctuation.md) (all punctuation).
- [static var omitWhitespace: NSLinguisticTagger.Options](nslinguistictagger/options/omitwhitespace.md)
  Omit tokens of type [`whitespace`](nslinguistictag/whitespace.md) (whitespace of all sorts).
- [static var omitOther: NSLinguisticTagger.Options](nslinguistictagger/options/omitother.md)
  Omit tokens of type [`other`](nslinguistictag/other.md) (non-linguistic items, such as symbols).
- [static var joinNames: NSLinguisticTagger.Options](nslinguistictagger/options/joinnames.md)
  Typically, multiple-word names will be returned as multiple tokens, following the standard tokenization practice of the tagger.  If this option is set, then multiple-word names will be joined together and returned as a single token.
- [static var omitWords: NSLinguisticTagger.Options](nslinguistictagger/options/omitwords.md)
  Omit tokens of type [`word`](nslinguistictag/word.md) (items considered to be words).
- [static var omitPunctuation: NSLinguisticTagger.Options](nslinguistictagger/options/omitpunctuation.md)
  Omit tokens of type [`punctuation`](nslinguistictag/punctuation.md) (all punctuation).
- [static var omitWhitespace: NSLinguisticTagger.Options](nslinguistictagger/options/omitwhitespace.md)
  Omit tokens of type [`whitespace`](nslinguistictag/whitespace.md) (whitespace of all sorts).
- [static var omitOther: NSLinguisticTagger.Options](nslinguistictagger/options/omitother.md)
  Omit tokens of type [`other`](nslinguistictag/other.md) (non-linguistic items, such as symbols).
- [static var joinNames: NSLinguisticTagger.Options](nslinguistictagger/options/joinnames.md)
  Typically, multiple-word names will be returned as multiple tokens, following the standard tokenization practice of the tagger.  If this option is set, then multiple-word names will be joined together and returned as a single token.
### Initializers
- [init(rawValue: UInt)](nslinguistictagger/options/init(rawvalue:).md)

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

- [Identifying Parts of Speech](identifying-parts-of-speech.md)
  Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying People, Places, and Organizations](identifying-people-places-and-organizations.md)
  Use a linguistic tagger to perform named entity recognition on a string.
- [func enumerateTags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(in:unit:scheme:options:using:).md)
  Enumerates over a given range of the string for a particular unit and calls the specified block for each tag.
- [func enumerateTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(in:scheme:options:using:).md)
  Enumerates over a given range of the string and calls the specified block for each tag.
- [class func enumerateTags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(for:range:unit:scheme:options:orthography:using:).md)
  Enumerates over a given string and calls the specified block for each tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/options)*