# NLTag

**Framework**: Natural Language  
**Kind**: struct

A token type, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
struct NLTag
```

#### Overview

When you create a linguistic tagger, you specify one or more [`NLTagScheme`](nltagscheme.md) constants that correspond to the kind of information you want to know about a selection of natural language text. When working with linguistic tags using the methods described in Getting linguistic tags and Enumerating linguistic tags in [`NLTagger`](nltagger.md), the returned value depends on the specified scheme. The [`NLTag`](nltag.md) type represents the constant values that can be returned for certain [`NLTagScheme`](nltagscheme.md) values.

## Topics

### Token types
- [static let word: NLTag](nltag/word.md)
  A tag indicating that the token is a word.
- [static let punctuation: NLTag](nltag/punctuation.md)
  A tag indicating that the token is punctuation.
- [static let whitespace: NLTag](nltag/whitespace.md)
  A tag indicating that the token is white space of any sort.
- [static let other: NLTag](nltag/other.md)
  A tag indicating that the token is a non-linguistic item, such as a symbol.
### Lexical classes
- [static let noun: NLTag](nltag/noun.md)
  A tag indicating that the token is a noun.
- [static let verb: NLTag](nltag/verb.md)
  A tag indicating that the token is a verb.
- [static let adjective: NLTag](nltag/adjective.md)
  A tag indicating that the token is an adjective
- [static let adverb: NLTag](nltag/adverb.md)
  A tag indicating that the token is an adverb.
- [static let pronoun: NLTag](nltag/pronoun.md)
  A tag indicating that the token is a pronoun.
- [static let determiner: NLTag](nltag/determiner.md)
  A tag indicating that the token is a determiner.
- [static let particle: NLTag](nltag/particle.md)
  A tag indicating that the token is a particle.
- [static let preposition: NLTag](nltag/preposition.md)
  A tag indicating that the token is a preposition.
- [static let number: NLTag](nltag/number.md)
  A tag indicating that the token is a number.
- [static let conjunction: NLTag](nltag/conjunction.md)
  A tag indicating that the token is a conjunction.
- [static let interjection: NLTag](nltag/interjection.md)
  A tag indicating that the token is an interjection.
- [static let classifier: NLTag](nltag/classifier.md)
  A tag indicating that the token is a classifier.
- [static let idiom: NLTag](nltag/idiom.md)
  A tag indicating that the token is an idiom.
- [static let otherWord: NLTag](nltag/otherword.md)
  A tag indicating that the token is a word other than a kind described by other lexical classes (noun, verb, adjective, adverb, pronoun, determiner, particle, preposition, number, conjunction, interjection, classifier, and idiom).
- [static let sentenceTerminator: NLTag](nltag/sentenceterminator.md)
  A tag indicating that the token is punctuation at the end of a sentence.
- [static let openQuote: NLTag](nltag/openquote.md)
  A tag indicating that the token is an open quote.
- [static let closeQuote: NLTag](nltag/closequote.md)
  A tag indicating that the token is a close quote.
- [static let openParenthesis: NLTag](nltag/openparenthesis.md)
  A tag indicating that the token is an open parenthesis.
- [static let closeParenthesis: NLTag](nltag/closeparenthesis.md)
  A tag indicating that the token is a close parenthesis.
- [static let wordJoiner: NLTag](nltag/wordjoiner.md)
  A tag indicating that the token is a word joiner, signifying that two tokens on each side should not be broken up.
- [static let dash: NLTag](nltag/dash.md)
  A tag indicating that the token is a dash.
- [static let otherPunctuation: NLTag](nltag/otherpunctuation.md)
  A tag indicating that the token is punctuation other than a kind described by other lexical classes (sentence terminator, open or close quote, open or close parenthesis, word joiner, and dash).
- [static let paragraphBreak: NLTag](nltag/paragraphbreak.md)
  A tag indicating that the token is a paragraph break.
- [static let otherWhitespace: NLTag](nltag/otherwhitespace.md)
  A tag indicating that the token is whitespace other than a kind described by other lexical classes (paragraph break).
### Name types
- [static let personalName: NLTag](nltag/personalname.md)
  A tag indicating that the token is a personal name.
- [static let organizationName: NLTag](nltag/organizationname.md)
  A tag indicating that the token is an organization name.
- [static let placeName: NLTag](nltag/placename.md)
  A tag indicating that the token is a place name.
### Initializers
- [init(String)](nltag/init(_:).md)
  Creates a new tag.
- [init(rawValue: String)](nltag/init(rawvalue:).md)
  Creates a new tag from the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func enumerateTags(in: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options, using: (NLTag?, Range<String.Index>) -> Bool)](nltagger/enumeratetags(in:unit:scheme:options:using:).md)
  Enumerates a block over the tagger’s string, given a range, token unit, and tag scheme.
- [NLTagger.Options](nltagger/options.md)
  Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltag)*