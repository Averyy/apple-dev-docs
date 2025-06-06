# nameType

**Framework**: Foundation  
**Kind**: property

Classifies tokens according to whether they are part of a named entity.

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
static let nameType: NSLinguisticTagScheme
```

## Mentions

- [Identifying People, Places, and Organizations](identifying-people-places-and-organizations.md)

#### Discussion

For possible values, see Name Types.

## See Also

- [static let tokenType: NSLinguisticTagScheme](nslinguistictagscheme/tokentype.md)
  Classifies tokens according to their broad type:  word, punctuation, or whitespace.
- [static let lexicalClass: NSLinguisticTagScheme](nslinguistictagscheme/lexicalclass.md)
  Classifies tokens according to class:  part of speech, type of punctuation, or whitespace.
- [static let nameTypeOrLexicalClass: NSLinguisticTagScheme](nslinguistictagscheme/nametypeorlexicalclass.md)
  Classifies tokens corresponding to names according to [`nameType`](nslinguistictagscheme/nametype.md), and classifies all other tokens according to [`lexicalClass`](nslinguistictagscheme/lexicalclass.md).
- [static let lemma: NSLinguisticTagScheme](nslinguistictagscheme/lemma.md)
  Supplies a stem form of a word token, if known.
- [static let language: NSLinguisticTagScheme](nslinguistictagscheme/language.md)
  Supplies the language for a token, if one can be determined.
- [static let script: NSLinguisticTagScheme](nslinguistictagscheme/script.md)
  Supplies the script for a token, if one can be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/nametype)*