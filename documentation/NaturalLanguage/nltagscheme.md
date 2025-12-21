# NLTagScheme

**Framework**: Natural Language  
**Kind**: struct

Constants for the tag schemes specified when initializing a linguistic tagger.

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
struct NLTagScheme
```

#### Overview

When initializing a linguistic tagger with [`init(_:)`](nltagscheme/init(_:).md), you specify one or more tag schemes that correspond to the kind of information you’re interested in for a selection of natural language text. To ensure optimal performance, avoid specifying tag schemes that you won’t use.

Some tag schemes are only available for certain units and languages. Use [`availableTagSchemes(for:language:)`](nltagger/availabletagschemes(for:language:).md) to determine the possible values for a specified language and linguistic unit.

When working with linguistic tags using the methods described in Getting linguistic tags and Enumerating linguistic tags in [`NLTagger`](nltagger.md), the returned tag value depends on the specified scheme. For example, given the token “Überraschung”, the returned tag is [`noun`](nltag/noun.md) when using the [`lexicalClass`](nltagscheme/lexicalclass.md) tag scheme, [`german`](nllanguage/german.md) (German language) when using the [`language`](nltagscheme/language.md) tag scheme, and “Latn” (Latin script) when using the [`script`](nltagscheme/script.md) tag scheme, as shown in the following code.

```swift
let tagger = NLTagger(tagSchemes: [.lexicalClass, .language, .script], options: 0)
tagger.string = "Überraschung"

tagger.tag(at: 0, unit: .word, scheme: .lexicalClass, tokenRange: nil) // Noun
tagger.tag(at: 0, unit: .word, scheme: .language, tokenRange: nil) // german
tagger.tag(at: 0, unit: .word, scheme: .script, tokenRange: nil) // Latn
```

## Topics

### Schemes
- [static let tokenType: NLTagScheme](nltagscheme/tokentype.md)
  A scheme that classifies tokens according to their broad type: word, punctuation, or whitespace.
- [static let lexicalClass: NLTagScheme](nltagscheme/lexicalclass.md)
  A scheme that classifies tokens according to class: part of speech, type of punctuation, or whitespace.
- [static let nameType: NLTagScheme](nltagscheme/nametype.md)
  A scheme that classifies tokens according to whether they are part of a named entity.
- [static let nameTypeOrLexicalClass: NLTagScheme](nltagscheme/nametypeorlexicalclass.md)
  A scheme that classifies tokens corresponding to names according to [`nameType`](nltagscheme/nametype.md), and classifies all other tokens according to [`lexicalClass`](nltagscheme/lexicalclass.md).
- [static let lemma: NLTagScheme](nltagscheme/lemma.md)
  A scheme that supplies a stem form of a word token, if known.
- [static let language: NLTagScheme](nltagscheme/language.md)
  A scheme that supplies the language for a token, if it can determine one.
- [static let script: NLTagScheme](nltagscheme/script.md)
  A scheme that supplies the script for a token, if it can determine one.
- [static let sentimentScore: NLTagScheme](nltagscheme/sentimentscore.md)
  A scheme that scores text as positive, negative, or neutral based on its sentiment polarity.
### Initializers
- [init(String)](nltagscheme/init(_:).md)
  Creates a tag scheme.
- [init(rawValue: String)](nltagscheme/init(rawvalue:).md)
  Creates a tag scheme with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func availableTagSchemes(for: NLTokenUnit, language: NLLanguage) -> [NLTagScheme]](nltagger/availabletagschemes(for:language:).md)
  Retrieves the tag schemes available for a particular unit (like word or sentence) and language on the current device.
- [class func requestAssets(for: NLLanguage, tagScheme: NLTagScheme, completionHandler: (NLTagger.AssetsResult, (any Error)?) -> Void)](nltagger/requestassets(for:tagscheme:completionhandler:).md)
  Asks the Natural Language framework to load any missing assets for a tag scheme onto the device for the given language.
- [NLTagger.AssetsResult](nltagger/assetsresult.md)
  The response to an asset request.
- [var tagSchemes: [NLTagScheme]](nltagger/tagschemes.md)
  The tag schemes configured for this linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagscheme)*