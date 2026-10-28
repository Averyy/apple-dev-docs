# nameTypeOrLexicalClass

**Framework**: Natural Language  
**Kind**: property  
**Role**: Type Property

A scheme that classifies tokens corresponding to names according to [`nameType`](./nametype.md), and classifies all other tokens according to [`lexicalClass`](./lexicalclass.md).

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
static let nameTypeOrLexicalClass: NLTagScheme
```

```c
extern NLTagScheme const NLTagSchemeNameTypeOrLexicalClass;
```

## Discussion

For possible values, see Name types and Lexical classes in [`NLTag`](../nltag.md).

## See Also

### Schemes
- [static let tokenType: NLTagScheme](./tokentype.md)
  A scheme that classifies tokens according to their broad type: word, punctuation, or whitespace.
- [static let lexicalClass: NLTagScheme](./lexicalclass.md)
  A scheme that classifies tokens according to class: part of speech, type of punctuation, or whitespace.
- [static let nameType: NLTagScheme](./nametype.md)
  A scheme that classifies tokens according to whether they are part of a named entity.
- [static let lemma: NLTagScheme](./lemma.md)
  A scheme that supplies a stem form of a word token, if known.
- [static let language: NLTagScheme](./language.md)
  A scheme that supplies the language for a token, if it can determine one.
- [static let script: NLTagScheme](./script.md)
  A scheme that supplies the script for a token, if it can determine one.
- [static let sentimentScore: NLTagScheme](./sentimentscore.md)
  A scheme that scores text as positive, negative, or neutral based on its sentiment polarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagscheme/nametypeorlexicalclass)*