# NSLinguisticTagScheme

**Framework**: Foundation  
**Kind**: struct

Constants for the tag schemes specified when initializing a linguistic tagger.

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
struct NSLinguisticTagScheme
```

#### Discussion

When initializing a linguistic tagger with [`init(tagSchemes:options:)`](nslinguistictagger/init(tagschemes:options:).md), you specify one or more tag schemes that correspond to the kind of information you’re interested in for a selection of natural language text. To ensure optimal performance, avoid specifying tag schemes that you won’t use.

Some tag schemes are only available for certain units and languages. Use the [`availableTagSchemes(for:language:)`](nslinguistictagger/availabletagschemes(for:language:).md) or [`availableTagSchemes(forLanguage:)`](nslinguistictagger/availabletagschemes(forlanguage:).md) methods to determine the possible values for a specified language and linguistic unit.

When working with linguistic tags using the methods described in Getting Linguistic Tags and Enumerating Linguistic Tags, the returned tag value depends on the specified scheme. For example, given the token “Überraschung”, the returned tag is [`noun`](nslinguistictag/noun.md) when using the [`lexicalClass`](nslinguistictagscheme/lexicalclass.md) tag scheme, “de” (German language) when using the [`language`](nslinguistictagscheme/language.md) tag scheme, and “Latn” (Latin script) when using the [`script`](nslinguistictagscheme/script.md) tag scheme, as shown in the following code.

```swift
let tagger = NSLinguisticTagger(tagSchemes: [.lexicalClass, .language, .script], options: 0)
tagger.string = "Überraschung"

tagger.tag(at: 0, unit: .word, scheme: .lexicalClass, tokenRange: nil) // Noun
tagger.tag(at: 0, unit: .word, scheme: .language, tokenRange: nil) // de
tagger.tag(at: 0, unit: .word, scheme: .script, tokenRange: nil) // Latn
```

The following table lists the available tag schemes, their applicable linguistic units, and possible tag values.

| Linguistic tag scheme | Applicable linguistic units | Possible tag values |
| --- | --- | --- |
| [`tokenType`](nslinguistictagscheme/tokentype.md) | [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) | See Token Types |
| [`lexicalClass`](nslinguistictagscheme/lexicalclass.md) | [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) | See Lexical Classes |
| [`nameType`](nslinguistictagscheme/nametype.md) | [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) | See Name Types |
| [`nameTypeOrLexicalClass`](nslinguistictagscheme/nametypeorlexicalclass.md) | [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) | See Name Types and Lexical Classes |
| [`lemma`](nslinguistictagscheme/lemma.md) | [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) | A stem of the word |
| [`language`](nslinguistictagscheme/language.md) | [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md), [`NSLinguisticTaggerUnit.sentence`](nslinguistictaggerunit/sentence.md), [`NSLinguisticTaggerUnit.paragraph`](nslinguistictaggerunit/paragraph.md), [`NSLinguisticTaggerUnit.document`](nslinguistictaggerunit/document.md) | A BCP-47 language tag |
| [`script`](nslinguistictagscheme/script.md) | [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md), [`NSLinguisticTaggerUnit.sentence`](nslinguistictaggerunit/sentence.md), [`NSLinguisticTaggerUnit.paragraph`](nslinguistictaggerunit/paragraph.md), [`NSLinguisticTaggerUnit.document`](nslinguistictaggerunit/document.md) | An ISO 15924 script code |

## Topics

### Schemes
- [static let tokenType: NSLinguisticTagScheme](nslinguistictagscheme/tokentype.md)
  Classifies tokens according to their broad type:  word, punctuation, or whitespace.
- [static let lexicalClass: NSLinguisticTagScheme](nslinguistictagscheme/lexicalclass.md)
  Classifies tokens according to class:  part of speech, type of punctuation, or whitespace.
- [static let nameType: NSLinguisticTagScheme](nslinguistictagscheme/nametype.md)
  Classifies tokens according to whether they are part of a named entity.
- [static let nameTypeOrLexicalClass: NSLinguisticTagScheme](nslinguistictagscheme/nametypeorlexicalclass.md)
  Classifies tokens corresponding to names according to [`nameType`](nslinguistictagscheme/nametype.md), and classifies all other tokens according to [`lexicalClass`](nslinguistictagscheme/lexicalclass.md).
- [static let lemma: NSLinguisticTagScheme](nslinguistictagscheme/lemma.md)
  Supplies a stem form of a word token, if known.
- [static let language: NSLinguisticTagScheme](nslinguistictagscheme/language.md)
  Supplies the language for a token, if one can be determined.
- [static let script: NSLinguisticTagScheme](nslinguistictagscheme/script.md)
  Supplies the script for a token, if one can be determined.
### Initializers
- [init(String)](nslinguistictagscheme/init(_:).md)
- [init(rawValue: String)](nslinguistictagscheme/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum NSLinguisticTaggerUnit](nslinguistictaggerunit.md)
  Constants representing linguistic units.
- [struct NSLinguisticTag](nslinguistictag.md)
  A token, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagscheme)*