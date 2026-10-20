# NSLinguisticTagger.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSLinguisticTaggerOptions : NSUInteger;
```

## Topics

### Constants
- [static var omitWords: NSLinguisticTagger.Options](./options/omitwords.md)
  Omit tokens of type [`word`](../nslinguistictag/word.md) (items considered to be words).
- [static var omitPunctuation: NSLinguisticTagger.Options](./options/omitpunctuation.md)
  Omit tokens of type [`punctuation`](../nslinguistictag/punctuation.md) (all punctuation).
- [static var omitWhitespace: NSLinguisticTagger.Options](./options/omitwhitespace.md)
  Omit tokens of type [`whitespace`](../nslinguistictag/whitespace.md) (whitespace of all sorts).
- [static var omitOther: NSLinguisticTagger.Options](./options/omitother.md)
  Omit tokens of type [`other`](../nslinguistictag/other.md) (non-linguistic items, such as symbols).
- [static var joinNames: NSLinguisticTagger.Options](./options/joinnames.md)
  Typically, multiple-word names will be returned as multiple tokens, following the standard tokenization practice of the tagger.  If this option is set, then multiple-word names will be joined together and returned as a single token.
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)

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

### Enumerating Linguistic Tags
- [Identifying Parts of Speech](../identifying-parts-of-speech.md)
  Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying People, Places, and Organizations](../identifying-people-places-and-organizations.md)
  Use a linguistic tagger to perform named entity recognition on a string.
- [func enumerateTags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratetags%28in,unit,scheme,options,using%29.md)
  Enumerates over a given range of the string for a particular unit and calls the specified block for each tag.
- [func enumerateTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratetags%28in,scheme,options,using%29.md)
  Enumerates over a given range of the string and calls the specified block for each tag.
- [class func enumerateTags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratetags%28for,range,unit,scheme,options,orthography,using%29.md)
  Enumerates over a given string and calls the specified block for each tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/options)*