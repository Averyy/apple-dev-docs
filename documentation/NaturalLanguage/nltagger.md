# NLTagger

**Framework**: Natural Language  
**Kind**: class

A tagger that analyzes natural language text.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class NLTagger
```

## Mentions

- [Identifying people, places, and organizations](identifying-people-places-and-organizations.md)
- [Creating a word tagger model](creating-a-word-tagger-model.md)
- [Identifying parts of speech](identifying-parts-of-speech.md)

#### Overview

[`NLTagger`](nltagger.md) supports many different languages and scripts. Use it to segment natural language text into paragraph, sentence, or word units and to tag each unit with information like part of speech, lexical class, lemma, script, and language.

When you create a linguistic tagger, you specify what kind of information you’re interested in by passing one or more [`NLTagScheme`](nltagscheme.md) values. Set the [`string`](nltagger/string.md) property to the natural language text you want to analyze, and the linguistic tagger processes it according to the specified tag schemes. You can then enumerate over the tags in a specified range, using the methods described in Enumerating linguistic tags, to get the information requested for a given scheme and unit.

> ❗ **Important**:  Don’t use an instance of [`NLTagger`](nltagger.md) simultaneously from multiple threads.

## Topics

### Creating a tagger
- [init(tagSchemes: [NLTagScheme])](nltagger/init(tagschemes:).md)
  Creates a linguistic tagger instance using the specified tag schemes and options.
- [var string: String?](nltagger/string.md)
  The string being analyzed by the linguistic tagger.
### Getting the tag schemes
- [class func availableTagSchemes(for: NLTokenUnit, language: NLLanguage) -> [NLTagScheme]](nltagger/availabletagschemes(for:language:).md)
  Retrieves the tag schemes available for a particular unit (like word or sentence) and language on the current device.
- [class func requestAssets(for: NLLanguage, tagScheme: NLTagScheme, completionHandler: (NLTagger.AssetsResult, (any Error)?) -> Void)](nltagger/requestassets(for:tagscheme:completionhandler:).md)
  Asks the Natural Language framework to load any missing assets for a tag scheme onto the device for the given language.
- [NLTagger.AssetsResult](nltagger/assetsresult.md)
  The response to an asset request.
- [var tagSchemes: [NLTagScheme]](nltagger/tagschemes.md)
  The tag schemes configured for this linguistic tagger.
- [struct NLTagScheme](nltagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.
### Determining the dominant language and orthography
- [var dominantLanguage: NLLanguage?](nltagger/dominantlanguage.md)
  The dominant language of the string set for the linguistic tagger.
- [func setLanguage(NLLanguage, range: Range<String.Index>)](nltagger/setlanguage(_:range:).md)
  Sets the language for a range of text within the tagger’s string.
- [func setOrthography(NSOrthography, range: Range<String.Index>)](nltagger/setorthography(_:range:).md)
  Sets the orthography for the specified range.
### Enumerating linguistic tags
- [func enumerateTags(in: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options, using: (NLTag?, Range<String.Index>) -> Bool)](nltagger/enumeratetags(in:unit:scheme:options:using:).md)
  Enumerates a block over the tagger’s string, given a range, token unit, and tag scheme.
- [NLTagger.Options](nltagger/options.md)
  Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.
- [struct NLTag](nltag.md)
  A token type, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.
### Getting linguistic tags
- [func tags(in: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options) -> [(NLTag?, Range<String.Index>)]](nltagger/tags(in:unit:scheme:options:).md)
  Finds an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [func tag(at: String.Index, unit: NLTokenUnit, scheme: NLTagScheme) -> (NLTag?, Range<String.Index>)](nltagger/tag(at:unit:scheme:).md)
  Finds a tag for a given linguistic unit, for a single scheme, at the specified character position.
- [func tagHypotheses(at: String.Index, unit: NLTokenUnit, scheme: NLTagScheme, maximumCount: Int) -> ([String : Double], Range<String.Index>)](nltagger/taghypotheses(at:unit:scheme:maximumcount:).md)
  Finds multiple possible tags for a given linguistic unit, for a single scheme, at the specified character position.
### Determining the range of a unit token
- [func tokenRange(at: String.Index, unit: NLTokenUnit) -> Range<String.Index>](nltagger/tokenrange(at:unit:).md)
  Returns the range of the linguistic unit containing the specified character index.
- [func tokenRange(for: Range<String.Index>, unit: NLTokenUnit) -> Range<String.Index>](nltagger/tokenrange(for:unit:).md)
  Finds the entire range of all tokens of the specified linguistic unit contained completely or partially within the specified range.
- [enum NLTokenUnit](nltokenunit.md)
  Constants representing linguistic units.
### Using models with a tagger
- [func setModels([NLModel], forTagScheme: NLTagScheme)](nltagger/setmodels(_:fortagscheme:).md)
  Assigns models for a tag scheme.
- [func models(forTagScheme: NLTagScheme) -> [NLModel]](nltagger/models(fortagscheme:).md)
  Returns the models that apply to the given tag scheme.
### Using gazetteers with a tagger
- [func setGazetteers([NLGazetteer], for: NLTagScheme)](nltagger/setgazetteers(_:for:).md)
  Attaches gazetteers to a tag scheme, typically one gazetteer per language or one language-independent gazetteer.
- [func gazetteers(for: NLTagScheme) -> [NLGazetteer]](nltagger/gazetteers(for:).md)
  Retrieves the gazetteers attached to a tag scheme.
- [class NLGazetteer](nlgazetteer.md)
  A collection of terms and their labels, which take precedence over a word tagger.

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

- [Identifying parts of speech](identifying-parts-of-speech.md)
  Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying people, places, and organizations](identifying-people-places-and-organizations.md)
  Use a linguistic tagger to perform named entity recognition on a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger)*