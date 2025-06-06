# enumerateTags(for:range:unit:scheme:options:orthography:using:)

**Framework**: Foundation  
**Kind**: method

Enumerates over a given string and calls the specified block for each tag.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func enumerateTags(for string: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options = [], orthography: NSOrthography?, using block: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

This method’s block is called for all tokens intersecting a given range, supplying tags and ranges. The tagger segments the string into sentences and tokens as necessary, and return those ranges along with a tag for any scheme in its array of tag schemes. For example, if the tag scheme is [`lexicalClass`](nslinguistictagscheme/lexicalclass.md), the tags specify the part of speech (for word tokens) or the type of whitespace or punctuation (for whitespace or punctuation tokens).  If the tag scheme is [`lemma`](nslinguistictagscheme/lemma.md), the tags specify the stem form of the word (if known) for each word token.

> ❗ **Important**:  This method enumerates over the ranges of all tokens that intersect the specified range.

 This method enumerates over the ranges of all tokens that intersect the specified range.

This is a convenience method for initializing a linguistic tagger, setting the [`string`](nslinguistictagger/string.md) property, and calling the [`enumerateTags(in:unit:scheme:options:using:)`](nslinguistictagger/enumeratetags(in:unit:scheme:options:using:).md) method. If you analyze the same string more than once, you should create a linguistic tagger object instead of calling this method.

## Parameters

- `string`: The string to enumerate over.
- `range`: The range to analyze.
- `unit`: The linguistic unit. For possible values, see 
- `scheme`: The tag scheme. For possible values, see  .
- `options`: The linguistic tagger options to use. See   for possible values.
- `orthography`: The orthography of the string. If unspecified, the orthography is automatically detected.
- `block`: The block takes the following arguments:

## See Also

- [Identifying Parts of Speech](identifying-parts-of-speech.md)
  Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying People, Places, and Organizations](identifying-people-places-and-organizations.md)
  Use a linguistic tagger to perform named entity recognition on a string.
- [func enumerateTags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(in:unit:scheme:options:using:).md)
  Enumerates over a given range of the string for a particular unit and calls the specified block for each tag.
- [func enumerateTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(in:scheme:options:using:).md)
  Enumerates over a given range of the string and calls the specified block for each tag.
- [NSLinguisticTagger.Options](nslinguistictagger/options.md)
  Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/enumeratetags(for:range:unit:scheme:options:orthography:using:))*