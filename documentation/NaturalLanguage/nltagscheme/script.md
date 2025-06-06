# script

**Framework**: Natural Language  
**Kind**: property

A scheme that supplies the script for a token, if it can determine one.

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
static let script: NLTagScheme
```

#### Discussion

Each value for this tag scheme is an ISO 15924 script identifier. For example, the identifier for Latin script is “Latn” and the identifier for Simplified Chinese script is “Hans”. The identifier “Zyyy” is used if a specific script cannot be determined.

## See Also

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
- [static let sentimentScore: NLTagScheme](nltagscheme/sentimentscore.md)
  A scheme that scores text as positive, negative, or neutral based on its sentiment polarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagscheme/script)*