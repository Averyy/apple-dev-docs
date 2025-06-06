# lexicalClass

**Framework**: Foundation  
**Kind**: property

Classifies tokens according to class:  part of speech, type of punctuation, or whitespace.

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
static let lexicalClass: NSLinguisticTagScheme
```

## Mentions

- [Identifying Parts of Speech](identifying-parts-of-speech.md)

#### Discussion

For possible values, see Lexical Classes.

The lexical class of a tag is a further distinction of its token type. Token types and lexical classes have the following correspondence:

| Token type | Lexical classes |
| --- | --- |
| [`word`](nslinguistictag/word.md) | [`noun`](nslinguistictag/noun.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`verb`](nslinguistictag/verb.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`adjective`](nslinguistictag/adjective.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`adverb`](nslinguistictag/adverb.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`pronoun`](nslinguistictag/pronoun.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`determiner`](nslinguistictag/determiner.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`particle`](nslinguistictag/particle.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`preposition`](nslinguistictag/preposition.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`number`](nslinguistictag/number.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`conjunction`](nslinguistictag/conjunction.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`interjection`](nslinguistictag/interjection.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`classifier`](nslinguistictag/classifier.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`idiom`](nslinguistictag/idiom.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`otherWord`](nslinguistictag/otherword.md) |
| [`punctuation`](nslinguistictag/punctuation.md) | [`sentenceTerminator`](nslinguistictag/sentenceterminator.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`openQuote`](nslinguistictag/openquote.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`closeQuote`](nslinguistictag/closequote.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`openParenthesis`](nslinguistictag/openparenthesis.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`closeParenthesis`](nslinguistictag/closeparenthesis.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`wordJoiner`](nslinguistictag/wordjoiner.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`dash`](nslinguistictag/dash.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`otherPunctuation`](nslinguistictag/otherpunctuation.md) |
| [`whitespace`](nslinguistictag/whitespace.md) | [`paragraphBreak`](nslinguistictag/paragraphbreak.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`otherWhitespace`](nslinguistictag/otherwhitespace.md) |
| [`other`](nslinguistictag/other.md) |  |

## See Also

- [static let tokenType: NSLinguisticTagScheme](nslinguistictagscheme/tokentype.md)
  Classifies tokens according to their broad type:  word, punctuation, or whitespace.
- [static let nameType: NSLinguisticTagScheme](nslinguistictagscheme/nametype.md)
  Classifies tokens according to whether they are part of a named entity.
- [static let nameTypeOrLexicalClass: NSLinguisticTagScheme](nslinguistictagscheme/nametypeorlexicalclass.md)
  Classifies tokens corresponding to names according to [`nameType`](nslinguistictagscheme/nametype.md), and classifies all other tokens according to [`lexicalClass`](nslinguistictagscheme/lexicalclass.md).
- [static let lemma: NSLinguisticTagScheme](nslinguistictagscheme/lemma.md)
  Supplies a stem form of a word token, if known.
- [static let language: NSLinguisticTagScheme](nslinguistictagscheme/language.md)
  Supplies the language for a token, if one can be determined.
- [static let script: NSLinguisticTagScheme](nslinguistictagscheme/script.md)
  Supplies the script for a token, if one can be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagscheme/lexicalclass)*