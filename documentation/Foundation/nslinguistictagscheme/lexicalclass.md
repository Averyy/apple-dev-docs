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
| [`word`](nslinguistictag/word.md) | [`noun`](nslinguistictag/noun.md) ![None](/images/com.apple.foundation/spacer.png) [`verb`](nslinguistictag/verb.md) ![None](/images/com.apple.foundation/spacer.png) [`adjective`](nslinguistictag/adjective.md) ![None](/images/com.apple.foundation/spacer.png) [`adverb`](nslinguistictag/adverb.md) ![None](/images/com.apple.foundation/spacer.png) [`pronoun`](nslinguistictag/pronoun.md) ![None](/images/com.apple.foundation/spacer.png) [`determiner`](nslinguistictag/determiner.md) ![None](/images/com.apple.foundation/spacer.png) [`particle`](nslinguistictag/particle.md) ![None](/images/com.apple.foundation/spacer.png) [`preposition`](nslinguistictag/preposition.md) ![None](/images/com.apple.foundation/spacer.png) [`number`](nslinguistictag/number.md) ![None](/images/com.apple.foundation/spacer.png) [`conjunction`](nslinguistictag/conjunction.md) ![None](/images/com.apple.foundation/spacer.png) [`interjection`](nslinguistictag/interjection.md) ![None](/images/com.apple.foundation/spacer.png) [`classifier`](nslinguistictag/classifier.md) ![None](/images/com.apple.foundation/spacer.png) [`idiom`](nslinguistictag/idiom.md) ![None](/images/com.apple.foundation/spacer.png) [`otherWord`](nslinguistictag/otherword.md) |
| [`punctuation`](nslinguistictag/punctuation.md) | [`sentenceTerminator`](nslinguistictag/sentenceterminator.md) ![None](/images/com.apple.foundation/spacer.png) [`openQuote`](nslinguistictag/openquote.md) ![None](/images/com.apple.foundation/spacer.png) [`closeQuote`](nslinguistictag/closequote.md) ![None](/images/com.apple.foundation/spacer.png) [`openParenthesis`](nslinguistictag/openparenthesis.md) ![None](/images/com.apple.foundation/spacer.png) [`closeParenthesis`](nslinguistictag/closeparenthesis.md) ![None](/images/com.apple.foundation/spacer.png) [`wordJoiner`](nslinguistictag/wordjoiner.md) ![None](/images/com.apple.foundation/spacer.png) [`dash`](nslinguistictag/dash.md) ![None](/images/com.apple.foundation/spacer.png) [`otherPunctuation`](nslinguistictag/otherpunctuation.md) |
| [`whitespace`](nslinguistictag/whitespace.md) | [`paragraphBreak`](nslinguistictag/paragraphbreak.md) ![None](/images/com.apple.foundation/spacer.png) [`otherWhitespace`](nslinguistictag/otherwhitespace.md) |
| [`other`](nslinguistictag/other.md) | *None* |

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