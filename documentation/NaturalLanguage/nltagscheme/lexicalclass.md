# lexicalClass

**Framework**: Natural Language  
**Kind**: property

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

## Mentions

- [Identifying parts of speech](identifying-parts-of-speech.md)

#### Discussion

For possible values, see Lexical classes in [`NLTag`](nltag.md).

The lexical class of a tag is a further distinction of its token type. Token types and lexical classes have the following correspondence:

| Token Type | Lexical classes |
| --- | --- |
| [`word`](nltag/word.md) | [`noun`](nltag/noun.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`verb`](nltag/verb.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`adjective`](nltag/adjective.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`adverb`](nltag/adverb.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`pronoun`](nltag/pronoun.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`determiner`](nltag/determiner.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`particle`](nltag/particle.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`preposition`](nltag/preposition.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`number`](nltag/number.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`conjunction`](nltag/conjunction.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`interjection`](nltag/interjection.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`classifier`](nltag/classifier.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`idiom`](nltag/idiom.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`otherWord`](nltag/otherword.md) |
| [`punctuation`](nltag/punctuation.md) | [`sentenceTerminator`](nltag/sentenceterminator.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`openQuote`](nltag/openquote.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`closeQuote`](nltag/closequote.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`openParenthesis`](nltag/openparenthesis.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`closeParenthesis`](nltag/closeparenthesis.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`wordJoiner`](nltag/wordjoiner.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`dash`](nltag/dash.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`otherPunctuation`](nltag/otherpunctuation.md) |
| [`whitespace`](nltag/whitespace.md) | [`paragraphBreak`](nltag/paragraphbreak.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`otherWhitespace`](nltag/otherwhitespace.md) |
| [`other`](nltag/other.md) |  |

## See Also

- [static let tokenType: NLTagScheme](nltagscheme/tokentype.md)
  A scheme that classifies tokens according to their broad type: word, punctuation, or whitespace.
- [static let nameType: NLTagScheme](nltagscheme/nametype.md)
  A scheme that classifies tokens according to whether they are part of a named entity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagscheme/lexicalclass)*