# lemma

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Supplies a stem form of a word token, if known.

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
static let lemma: NSLinguisticTagScheme
```

```c
extern NSLinguisticTagScheme const NSLinguisticTagSchemeLemma;
```

## Discussion

For example, the stem of the English word “reading” is “read”.

## See Also

### Schemes
- [static let tokenType: NSLinguisticTagScheme](./tokentype.md)
  Classifies tokens according to their broad type:  word, punctuation, or whitespace.
- [static let lexicalClass: NSLinguisticTagScheme](./lexicalclass.md)
  Classifies tokens according to class:  part of speech, type of punctuation, or whitespace.
- [static let nameType: NSLinguisticTagScheme](./nametype.md)
  Classifies tokens according to whether they are part of a named entity.
- [static let nameTypeOrLexicalClass: NSLinguisticTagScheme](./nametypeorlexicalclass.md)
  Classifies tokens corresponding to names according to [`nameType`](./nametype.md), and classifies all other tokens according to [`lexicalClass`](./lexicalclass.md).
- [static let language: NSLinguisticTagScheme](./language.md)
  Supplies the language for a token, if one can be determined.
- [static let script: NSLinguisticTagScheme](./script.md)
  Supplies the script for a token, if one can be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/lemma)*