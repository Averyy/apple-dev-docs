# lexicalClass

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Classifies tokens according to class:  part of speech, type of punctuation, or whitespace.

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
static let lexicalClass: NSLinguisticTagScheme
```

```c
extern NSLinguisticTagScheme const NSLinguisticTagSchemeLexicalClass;
```

## Mentions

- [Identifying Parts of Speech](../identifying-parts-of-speech.md)

## Discussion

For possible values, see Lexical Classes.

The lexical class of a tag is a further distinction of its token type. Token types and lexical classes have the following correspondence:

| Token type | Lexical classes |
| --- | --- |
| [`word`](../nslinguistictag/word.md) | [`noun`](../nslinguistictag/noun.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`verb`](../nslinguistictag/verb.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`adjective`](../nslinguistictag/adjective.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`adverb`](../nslinguistictag/adverb.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`pronoun`](../nslinguistictag/pronoun.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`determiner`](../nslinguistictag/determiner.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`particle`](../nslinguistictag/particle.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`preposition`](../nslinguistictag/preposition.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`number`](../nslinguistictag/number.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`conjunction`](../nslinguistictag/conjunction.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`interjection`](../nslinguistictag/interjection.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`classifier`](../nslinguistictag/classifier.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`idiom`](../nslinguistictag/idiom.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`otherWord`](../nslinguistictag/otherword.md) |
| [`punctuation`](../nslinguistictag/punctuation.md) | [`sentenceTerminator`](../nslinguistictag/sentenceterminator.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`openQuote`](../nslinguistictag/openquote.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`closeQuote`](../nslinguistictag/closequote.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`openParenthesis`](../nslinguistictag/openparenthesis.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`closeParenthesis`](../nslinguistictag/closeparenthesis.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`wordJoiner`](../nslinguistictag/wordjoiner.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`dash`](../nslinguistictag/dash.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`otherPunctuation`](../nslinguistictag/otherpunctuation.md) |
| [`whitespace`](../nslinguistictag/whitespace.md) | [`paragraphBreak`](../nslinguistictag/paragraphbreak.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`otherWhitespace`](../nslinguistictag/otherwhitespace.md) |
| [`other`](../nslinguistictag/other.md) | *None* |

## See Also

### Schemes
- [static let tokenType: NSLinguisticTagScheme](./tokentype.md)
  Classifies tokens according to their broad type:  word, punctuation, or whitespace.
- [static let nameType: NSLinguisticTagScheme](./nametype.md)
  Classifies tokens according to whether they are part of a named entity.
- [static let nameTypeOrLexicalClass: NSLinguisticTagScheme](./nametypeorlexicalclass.md)
  Classifies tokens corresponding to names according to [`nameType`](./nametype.md), and classifies all other tokens according to [`lexicalClass`](./lexicalclass.md).
- [static let lemma: NSLinguisticTagScheme](./lemma.md)
  Supplies a stem form of a word token, if known.
- [static let language: NSLinguisticTagScheme](./language.md)
  Supplies the language for a token, if one can be determined.
- [static let script: NSLinguisticTagScheme](./script.md)
  Supplies the script for a token, if one can be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/lexicalclass)*