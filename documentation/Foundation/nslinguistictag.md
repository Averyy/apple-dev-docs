# NSLinguisticTag

**Framework**: Foundation  
**Kind**: struct

A token, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSLinguisticTag
```

#### Overview

When you create a linguistic tagger, you specify one or more [`NSLinguisticTagScheme`](nslinguistictagscheme.md) constants that correspond to the kind of information you want to know about a selection of natural language text.  When working with linguistic tags using the methods described in Getting Linguistic Tags and Enumerating Linguistic Tags, the returned value depends on the specified scheme. The [`NSLinguisticTag`](nslinguistictag.md) type represents the constant values that can be returned for certain [`NSLinguisticTagScheme`](nslinguistictagscheme.md) values.

## Topics

### Token Types
- [static let word: NSLinguisticTag](nslinguistictag/word.md)
  The token indicates a word.
- [static let punctuation: NSLinguisticTag](nslinguistictag/punctuation.md)
  The token indicates punctuation.
- [static let whitespace: NSLinguisticTag](nslinguistictag/whitespace.md)
  The token indicates white space of any sort.
- [static let other: NSLinguisticTag](nslinguistictag/other.md)
  The token indicates a non-linguistic item, such as a symbol.
### Lexical Classes
- [static let noun: NSLinguisticTag](nslinguistictag/noun.md)
  The token is a noun.
- [static let verb: NSLinguisticTag](nslinguistictag/verb.md)
  This token is a verb.
- [static let adjective: NSLinguisticTag](nslinguistictag/adjective.md)
  This token is an adjective
- [static let adverb: NSLinguisticTag](nslinguistictag/adverb.md)
  This token is an adverb.
- [static let pronoun: NSLinguisticTag](nslinguistictag/pronoun.md)
  This token is a pronoun.
- [static let determiner: NSLinguisticTag](nslinguistictag/determiner.md)
  This token is a determiner.
- [static let particle: NSLinguisticTag](nslinguistictag/particle.md)
  This token is a particle.
- [static let preposition: NSLinguisticTag](nslinguistictag/preposition.md)
  This token is a preposition.
- [static let number: NSLinguisticTag](nslinguistictag/number.md)
  This token is a number.
- [static let conjunction: NSLinguisticTag](nslinguistictag/conjunction.md)
  This token is a conjunction.
- [static let interjection: NSLinguisticTag](nslinguistictag/interjection.md)
  This token is an interjection.
- [static let classifier: NSLinguisticTag](nslinguistictag/classifier.md)
  This token is a classifier.
- [static let idiom: NSLinguisticTag](nslinguistictag/idiom.md)
  This token is an idiom.
- [static let otherWord: NSLinguisticTag](nslinguistictag/otherword.md)
  This token is a word other than a kind described by other lexical classes (noun, verb, adjective, adverb, pronoun, determiner, particle, preposition, number, conjunction, interjection, classifier, and idiom).
- [static let sentenceTerminator: NSLinguisticTag](nslinguistictag/sentenceterminator.md)
  This token is a sentence terminator.
- [static let openQuote: NSLinguisticTag](nslinguistictag/openquote.md)
  This token is an open quote.
- [static let closeQuote: NSLinguisticTag](nslinguistictag/closequote.md)
  This token is a close quote.
- [static let openParenthesis: NSLinguisticTag](nslinguistictag/openparenthesis.md)
  This token is an open parenthesis.
- [static let closeParenthesis: NSLinguisticTag](nslinguistictag/closeparenthesis.md)
  This token is a close parenthesis.
- [static let wordJoiner: NSLinguisticTag](nslinguistictag/wordjoiner.md)
  This token is a word joiner.
- [static let dash: NSLinguisticTag](nslinguistictag/dash.md)
  This token is a dash.
- [static let otherPunctuation: NSLinguisticTag](nslinguistictag/otherpunctuation.md)
  This token is punctuation other than a kind described by other lexical classes (sentence terminator, open or close quote, open or close parenthesis, word joiner, and dash).
- [static let paragraphBreak: NSLinguisticTag](nslinguistictag/paragraphbreak.md)
  This token is a paragraph break.
- [static let otherWhitespace: NSLinguisticTag](nslinguistictag/otherwhitespace.md)
  This token is whitespace other than a kind described by other lexical classes (paragraph break).
### Name Types
- [static let personalName: NSLinguisticTag](nslinguistictag/personalname.md)
  This token is a personal name.
- [static let organizationName: NSLinguisticTag](nslinguistictag/organizationname.md)
  This token is an organization name.
- [static let placeName: NSLinguisticTag](nslinguistictag/placename.md)
  This token is a place name.
### Initializers
- [init(String)](nslinguistictag/init(_:).md)
- [init(rawValue: String)](nslinguistictag/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct NSLinguisticTagScheme](nslinguistictagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.
- [enum NSLinguisticTaggerUnit](nslinguistictaggerunit.md)
  Constants representing linguistic units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictag)*