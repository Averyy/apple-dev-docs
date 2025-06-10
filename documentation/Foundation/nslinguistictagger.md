# NSLinguisticTagger

**Framework**: Foundation  
**Kind**: class

Analyze natural language text to tag part of speech and lexical class, identify names, perform lemmatization, and determine the language and script.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSLinguisticTagger
```

## Mentions

- [Tokenizing Natural Language Text](tokenizing-natural-language-text.md)
- [Identifying People, Places, and Organizations](identifying-people-places-and-organizations.md)
- [Identifying Parts of Speech](identifying-parts-of-speech.md)

#### Overview

[`NSLinguisticTagger`](nslinguistictagger.md) provides a uniform interface to a variety of natural language processing functionality with support for many different languages and scripts. You can use this class to segment natural language text into paragraphs, sentences, or words, and tag information about those segments, such as part of speech, lexical class, lemma, script, and language.

When you create a linguistic tagger, you specify what kind of information you’re interested in by passing one or more [`NSLinguisticTagScheme`](nslinguistictagscheme.md) values. Set the [`string`](nslinguistictagger/string.md) property to the natural language text you want to analyze, and the linguistic tagger processes it according to the specified tag schemes. You can then enumerate over the tags in a specified range, using the methods described in Enumerating Linguistic Tags, to get the information requested for a given scheme and unit.

##### Thread Safety

A single instance of [`NSLinguisticTagger`](nslinguistictagger.md) should not be used simultaneously from multiple threads.

## Topics

### First Steps
- [Tokenizing Natural Language Text](tokenizing-natural-language-text.md)
  Enumerate the words in a string.
- [init(tagSchemes: [NSLinguisticTagScheme], options: Int)](nslinguistictagger/init(tagschemes:options:).md)
  Creates a linguistic tagger instance using the specified tag schemes and options.
- [var string: String?](nslinguistictagger/string.md)
  The string being analyzed by the linguistic tagger.
### Getting the Tag Schemes
- [class func availableTagSchemes(for: NSLinguisticTaggerUnit, language: String) -> [NSLinguisticTagScheme]](nslinguistictagger/availabletagschemes(for:language:).md)
  Returns the tag schemes available for a particular unit and language on the current device.
- [class func availableTagSchemes(forLanguage: String) -> [NSLinguisticTagScheme]](nslinguistictagger/availabletagschemes(forlanguage:).md)
  Returns the tag schemes available for a particular language on the current device.
- [var tagSchemes: [NSLinguisticTagScheme]](nslinguistictagger/tagschemes.md)
  Returns the tag schemes configured for this linguistic tagger. For possible values, see [`NSLinguisticTagScheme`](nslinguistictagscheme.md).
### Determining the Dominant Language and Orthography
- [class func dominantLanguage(for: String) -> String?](nslinguistictagger/dominantlanguage(for:).md)
  Returns the dominant language for the specified string.
- [var dominantLanguage: String?](nslinguistictagger/dominantlanguage.md)
  Returns the dominant language of the string set for the linguistic tagger.
- [func orthography(at: Int, effectiveRange: NSRangePointer?) -> NSOrthography?](nslinguistictagger/orthography(at:effectiverange:).md)
  Returns the orthography at the index and also returns the effective range.
- [func setOrthography(NSOrthography?, range: NSRange)](nslinguistictagger/setorthography(_:range:).md)
  Sets the orthography for the specified range.
### Enumerating Linguistic Tags
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
- [NSLinguisticTagger.Options](nslinguistictagger/options.md)
  Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.
### Getting Linguistic Tags
- [func tag(at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(at:unit:scheme:tokenrange:).md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position.
- [func tag(at: Int, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(at:scheme:tokenrange:sentencerange:).md)
  Returns a tag for a single scheme at the specified character position.
- [class func tag(for: String, at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, orthography: NSOrthography?, tokenRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(for:at:unit:scheme:orthography:tokenrange:).md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string.
- [func tags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nslinguistictagger/tags(in:unit:scheme:options:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [func tags(in: NSRange, scheme: String, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]](nslinguistictagger/tags(in:scheme:options:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string range.
- [class func tags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nslinguistictagger/tags(for:range:unit:scheme:options:orthography:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string and linguistic unit.
### Determining the Range of a Unit Token
- [func tokenRange(at: Int, unit: NSLinguisticTaggerUnit) -> NSRange](nslinguistictagger/tokenrange(at:unit:).md)
  Returns the range of the linguistic unit containing the specified character index.
- [func sentenceRange(for: NSRange) -> NSRange](nslinguistictagger/sentencerange(for:).md)
  Returns the range of a sentence containing the specified range.
### Determining the Possible Tags
- [func possibleTags(at: Int, scheme: String, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?, scores: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]?](nslinguistictagger/possibletags(at:scheme:tokenrange:sentencerange:scores:).md)
  Returns an array of possible tags for the given scheme at the specified range, supplying matching scores.
### Notifying for Changes to the Analyzed String
- [func stringEdited(in: NSRange, changeInLength: Int)](nslinguistictagger/stringedited(in:changeinlength:).md)
  Notifies the linguistic tagger that the string (if mutable) has changed as specified by the parameters.
### Supporting Types
- [struct NSLinguisticTagScheme](nslinguistictagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.
- [enum NSLinguisticTaggerUnit](nslinguistictaggerunit.md)
  Constants representing linguistic units.
- [struct NSLinguisticTag](nslinguistictag.md)
  A token, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.

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

- [Deprecated String Encodings](1497268-deprecated-string-encodings.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger)*