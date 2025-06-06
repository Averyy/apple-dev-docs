# nameType

**Framework**: Natural Language  
**Kind**: property

A scheme that classifies tokens according to whether they are part of a named entity.

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
static let nameType: NLTagScheme
```

## Mentions

- [Identifying people, places, and organizations](identifying-people-places-and-organizations.md)

#### Discussion

For possible values, see Name types in [`NLTag`](nltag.md).

## See Also

- [static let tokenType: NLTagScheme](nltagscheme/tokentype.md)
  A scheme that classifies tokens according to their broad type: word, punctuation, or whitespace.
- [static let lexicalClass: NLTagScheme](nltagscheme/lexicalclass.md)
  A scheme that classifies tokens according to class: part of speech, type of punctuation, or whitespace.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagscheme/nametype)*