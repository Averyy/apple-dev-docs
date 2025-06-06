# script

**Framework**: Foundation  
**Kind**: property

Supplies the script for a token, if one can be determined.

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
static let script: NSLinguisticTagScheme
```

#### Discussion

Each value for this tag scheme is an ISO 15924 script identifier. For example,  the identifier for Latin script is “Latn” and the identifier for Simplified Chinese script is “Hans”. The identifier “Zyyy” is used if a specific script cannot be determined.

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
- [static let language: NSLinguisticTagScheme](nslinguistictagscheme/language.md)
  Supplies the language for a token, if one can be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/script)*