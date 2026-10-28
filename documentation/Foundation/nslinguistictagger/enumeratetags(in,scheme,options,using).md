# enumerateTags(in:scheme:options:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Enumerates over a given range of the string and calls the specified block for each tag.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.7+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

## Declaration

```swift
func enumerateTags(in range: NSRange, scheme tagScheme: NSLinguisticTagScheme, options opts: NSLinguisticTagger.Options = [], using block: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateTagsInRange:(NSRange) range scheme:(NSLinguisticTagScheme) tagScheme options:(NSLinguisticTaggerOptions) opts usingBlock:(void (^)(NSLinguisticTag tag, NSRange tokenRange, NSRange sentenceRange, BOOL *stop)) block;
```

## Discussion

This method’s block is called for all tokens intersecting a given range, supplying tags and ranges. The tagger segments the string into sentences and tokens as necessary, and return those ranges along with a tag for any scheme in its array of tag schemes. For example, if the tag scheme is [`lexicalClass`](../nslinguistictagscheme/lexicalclass.md), the tags specify the part of speech (for word tokens) or the type of whitespace or punctuation (for whitespace or punctuation tokens).  If the tag scheme is [`lemma`](../nslinguistictagscheme/lemma.md), the tags specify the stem form of the word (if known) for each word token.

> ❗ **Important**:  This method enumerates over the ranges of all tokens that intersect the specified range.

This is a convenience method for calling the [`enumerateTags(in:unit:scheme:options:using:)`](./enumeratetags%28in,unit,scheme,options,using%29.md) method, passing [`NSLinguisticTaggerUnit.word`](../nslinguistictaggerunit/word.md) as the linguistic unit.

## Parameters

- `range`: The range to analyze.
- `tagScheme`: The tag scheme. For possible values, see [`NSLinguisticTagScheme`](../nslinguistictagscheme.md).
- `opts`: The linguistic tagger options to use. See [`NSLinguisticTagger.Options`](./options.md) for possible values.
- `block`: The block to apply to ranges of the string.

  The block takes the following arguments:

  - **tag**: The located linguistic tag.
  - **tokenRange**: The range of the linguistic tag.
  - **sentenceRange**: The range of the sentence in which the tag occurs.
  - **stop**: A reference to a Boolean value. The block can set the value to [`true`](../../Swift/true.md) to stop further processing of the set. The `stop` argument is an out-only argument. You should only ever set this Boolean to [`true`](../../Swift/true.md) within the block.

## See Also

### Enumerating Linguistic Tags
- [Identifying Parts of Speech](../identifying-parts-of-speech.md)
  Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying People, Places, and Organizations](../identifying-people-places-and-organizations.md)
  Use a linguistic tagger to perform named entity recognition on a string.
- [func enumerateTags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratetags%28in,unit,scheme,options,using%29.md)
  Enumerates over a given range of the string for a particular unit and calls the specified block for each tag.
- [class func enumerateTags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratetags%28for,range,unit,scheme,options,orthography,using%29.md)
  Enumerates over a given string and calls the specified block for each tag.
- [NSLinguisticTagger.Options](./options.md)
  Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/enumeratetags(in:scheme:options:using:))*