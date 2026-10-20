# lexicalClass

**Framework**: Natural Language  
**Kind**: property  
**Role**: Type Property

A scheme that classifies tokens according to class: part of speech, type of punctuation, or whitespace.

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
static let lexicalClass: NLTagScheme
```

```c
extern NLTagScheme const NLTagSchemeLexicalClass;
```

## Mentions

- [Identifying parts of speech](../identifying-parts-of-speech.md)

#### Discussion

For possible values, see Lexical classes in [`NLTag`](../nltag.md).

The lexical class of a tag is a further distinction of its token type. Token types and lexical classes have the following correspondence:

| Token Type | Lexical classes |
| --- | --- |
| [`word`](../nltag/word.md) | [`noun`](../nltag/noun.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`verb`](../nltag/verb.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`adjective`](../nltag/adjective.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`adverb`](../nltag/adverb.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`pronoun`](../nltag/pronoun.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`determiner`](../nltag/determiner.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`particle`](../nltag/particle.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`preposition`](../nltag/preposition.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`number`](../nltag/number.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`conjunction`](../nltag/conjunction.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`interjection`](../nltag/interjection.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`classifier`](../nltag/classifier.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`idiom`](../nltag/idiom.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`otherWord`](../nltag/otherword.md) |
| [`punctuation`](../nltag/punctuation.md) | [`sentenceTerminator`](../nltag/sentenceterminator.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`openQuote`](../nltag/openquote.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`closeQuote`](../nltag/closequote.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`openParenthesis`](../nltag/openparenthesis.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`closeParenthesis`](../nltag/closeparenthesis.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`wordJoiner`](../nltag/wordjoiner.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`dash`](../nltag/dash.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`otherPunctuation`](../nltag/otherpunctuation.md) |
| [`whitespace`](../nltag/whitespace.md) | [`paragraphBreak`](../nltag/paragraphbreak.md) ![](https://developer.apple.com/tutorials/images/com.apple.naturallanguage/spacer.png) [`otherWhitespace`](../nltag/otherwhitespace.md) |
| [`other`](../nltag/other.md) | *None* |

## See Also

### Schemes
- [static let tokenType: NLTagScheme](./tokentype.md)
  A scheme that classifies tokens according to their broad type: word, punctuation, or whitespace.
- [static let nameType: NLTagScheme](./nametype.md)
  A scheme that classifies tokens according to whether they are part of a named entity.
- [static let nameTypeOrLexicalClass: NLTagScheme](./nametypeorlexicalclass.md)
  A scheme that classifies tokens corresponding to names according to [`nameType`](./nametype.md), and classifies all other tokens according to [`lexicalClass`](./lexicalclass.md).
- [static let lemma: NLTagScheme](./lemma.md)
  A scheme that supplies a stem form of a word token, if known.
- [static let language: NLTagScheme](./language.md)
  A scheme that supplies the language for a token, if it can determine one.
- [static let script: NLTagScheme](./script.md)
  A scheme that supplies the script for a token, if it can determine one.
- [static let sentimentScore: NLTagScheme](./sentimentscore.md)
  A scheme that scores text as positive, negative, or neutral based on its sentiment polarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagscheme/lexicalclass)*