# NLTagger

**Framework**: Natural Language  
**Kind**: class  
**Role**: Class

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

```objc
@interface NLTagger : NSObject
```

## Mentions

- [Identifying people, places, and organizations](./identifying-people-places-and-organizations.md)
- [Identifying parts of speech](./identifying-parts-of-speech.md)

## Overview

[`NLTagger`](./nltagger.md) supports many different languages and scripts. Use it to segment natural language text into paragraph, sentence, or word units and to tag each unit with information like part of speech, lexical class, lemma, script, and language.

When you create a linguistic tagger, you specify what kind of information you’re interested in by passing one or more [`NLTagScheme`](./nltagscheme.md) values. Set the [`string`](./nltagger/string.md) property to the natural language text you want to analyze, and the linguistic tagger processes it according to the specified tag schemes. You can then enumerate over the tags in a specified range, using the methods described in Enumerating linguistic tags, to get the information requested for a given scheme and unit.

> ❗ **Important**: An [`NLTagger`](./nltagger.md) isn’t safe for concurrent use, including its read-looking query methods such as [`tags(in:unit:scheme:options:)`](./nltagger/tags%28in,unit,scheme,options%29.md), [`tag(at:unit:scheme:)`](./nltagger/tag%28at,unit,scheme%29.md), and the `enumerateTags` family, which mutate shared state. Use a given instance from only one thread or dispatch queue at a time: either serialize all calls to it, or create a separate tagger for each thread or dispatch queue.

## Topics

### Creating a tagger
- [init(tagSchemes: [NLTagScheme])](./nltagger/init%28tagschemes%29.md)
  Creates a linguistic tagger instance using the specified tag schemes and options.
- [var string: String?](./nltagger/string.md)
  The string being analyzed by the linguistic tagger.
### Getting the tag schemes
- [class func availableTagSchemes(for: NLTokenUnit, language: NLLanguage) -> [NLTagScheme]](./nltagger/availabletagschemes%28for,language%29.md)
  Retrieves the tag schemes available for a particular unit (like word or sentence) and language on the current device.
- [class func requestAssets(for: NLLanguage, tagScheme: NLTagScheme, completionHandler: (NLTagger.AssetsResult, (any Error)?) -> Void)](./nltagger/requestassets%28for,tagscheme,completionhandler%29.md)
  Asks the Natural Language framework to load any missing assets for a tag scheme onto the device for the given language.
- [NLTagger.AssetsResult](./nltagger/assetsresult.md)
  The response to an asset request.
- [var tagSchemes: [NLTagScheme]](./nltagger/tagschemes.md)
  The tag schemes configured for this linguistic tagger.
- [struct NLTagScheme](./nltagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.
### Determining the dominant language and orthography
- [var dominantLanguage: NLLanguage?](./nltagger/dominantlanguage.md)
  The dominant language of the string set for the linguistic tagger.
- [func setLanguage(NLLanguage, range: Range<String.Index>)](./nltagger/setlanguage%28_,range%29.md)
  Sets the language for a range of text within the tagger’s string.
- [func setOrthography(NSOrthography, range: Range<String.Index>)](./nltagger/setorthography%28_,range%29.md)
  Sets the orthography for the specified range.
- [- setLanguage:range:](./nltagger/setlanguage_range_.md)
  Sets the language for a range of text within the tagger’s string.
- [- setOrthography:range:](./nltagger/setorthography_range_.md)
  Sets the orthography for the specified range.
### Enumerating linguistic tags
- [func enumerateTags(in: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options, using: (NLTag?, Range<String.Index>) -> Bool)](./nltagger/enumeratetags%28in,unit,scheme,options,using%29.md)
  Enumerates a block over the tagger’s string, given a range, token unit, and tag scheme.
- [NLTagger.Options](./nltagger/options.md)
  Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.
- [struct NLTag](./nltag.md)
  A token type, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.
- [- enumerateTagsInRange:unit:scheme:options:usingBlock:](./nltagger/enumeratetagsinrange_unit_scheme_options_usingblock_.md)
  Enumerates a block over the tagger’s string, given a range, token unit, and tag scheme.
### Getting linguistic tags
- [func tags(in: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options) -> [(NLTag?, Range<String.Index>)]](./nltagger/tags%28in,unit,scheme,options%29.md)
  Finds an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [func tag(at: String.Index, unit: NLTokenUnit, scheme: NLTagScheme) -> (NLTag?, Range<String.Index>)](./nltagger/tag%28at,unit,scheme%29.md)
  Finds a tag for a given linguistic unit, for a single scheme, at the specified character position.
- [func tagHypotheses(at: String.Index, unit: NLTokenUnit, scheme: NLTagScheme, maximumCount: Int) -> ([String : Double], Range<String.Index>)](./nltagger/taghypotheses%28at,unit,scheme,maximumcount%29.md)
  Finds multiple possible tags for a given linguistic unit, for a single scheme, at the specified character position.
- [- tagsInRange:unit:scheme:options:tokenRanges:](./nltagger/tagsinrange_unit_scheme_options_tokenranges_.md)
  Finds an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [- tagAtIndex:unit:scheme:tokenRange:](./nltagger/tagatindex_unit_scheme_tokenrange_.md)
  Finds a tag for a given linguistic unit, for a single scheme, at the specified character position.
- [- tagHypothesesAtIndex:unit:scheme:maximumCount:tokenRange:](./nltagger/taghypothesesatindex_unit_scheme_maximumcount_tokenrange_.md)
  Finds multiple possible tags for a given linguistic unit, for a single scheme, at the specified character position.
### Determining the range of a unit token
- [func tokenRange(at: String.Index, unit: NLTokenUnit) -> Range<String.Index>](./nltagger/tokenrange%28at,unit%29.md)
  Returns the range of the linguistic unit containing the specified character index.
- [func tokenRange(for: Range<String.Index>, unit: NLTokenUnit) -> Range<String.Index>](./nltagger/tokenrange%28for,unit%29.md)
  Finds the entire range of all tokens of the specified linguistic unit contained completely or partially within the specified range.
- [enum NLTokenUnit](./nltokenunit.md)
  Constants representing linguistic units.
- [- tokenRangeAtIndex:unit:](./nltagger/tokenrangeatindex_unit_.md)
  Returns the range of the linguistic unit containing the specified character index.
- [- tokenRangeForRange:unit:](./nltagger/tokenrangeforrange_unit_.md)
  Finds the entire range of all tokens of the specified linguistic unit contained completely or partially within the specified range.
### Using models with a tagger
- [func setModels([NLModel], forTagScheme: NLTagScheme)](./nltagger/setmodels%28_,fortagscheme%29.md)
  Assigns models for a tag scheme.
- [func models(forTagScheme: NLTagScheme) -> [NLModel]](./nltagger/models%28fortagscheme%29.md)
  Returns the models that apply to the given tag scheme.
### Using gazetteers with a tagger
- [func setGazetteers([NLGazetteer], for: NLTagScheme)](./nltagger/setgazetteers%28_,for%29.md)
  Attaches gazetteers to a tag scheme, typically one gazetteer per language or one language-independent gazetteer.
- [func gazetteers(for: NLTagScheme) -> [NLGazetteer]](./nltagger/gazetteers%28for%29.md)
  Retrieves the gazetteers attached to a tag scheme.
- [class NLGazetteer](./nlgazetteer.md)
  A collection of terms and their labels, which take precedence over a word tagger.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Linguistic tags
- [Identifying parts of speech](./identifying-parts-of-speech.md)
  Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying people, places, and organizations](./identifying-people-places-and-organizations.md)
  Use a linguistic tagger to perform named entity recognition on a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger)*