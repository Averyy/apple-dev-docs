# language

**Framework**: Foundation  
**Kind**: property

Supplies the language for a token, if one can be determined.

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
static let language: NSLinguisticTagScheme
```

#### Discussion

Each value for this tag scheme is a BCP-47 language identifier. For example, the language identifier for English is “en” and the identifier for Chinese written using the Simplified Chinese script is “zh-Hans”. The identifier “und” is used if a specific language cannot be determined.

The tagger generally attempts to determine the language of text at the level of an entire sentence, paragraph, or document, rather than word by word.

## See Also

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
- [static let script: NSLinguisticTagScheme](nslinguistictagscheme/script.md)
  Supplies the script for a token, if one can be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/language)*