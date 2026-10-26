# NSGrammaticalPartOfSpeech

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A representation of grammatical parts of speech, used for inflecting strings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum NSGrammaticalPartOfSpeech
```

```c
enum NSGrammaticalPartOfSpeech : NSInteger;
```

## Topics

### Determining Part of Speech
- [NSGrammaticalPartOfSpeech.determiner](./nsgrammaticalpartofspeech/determiner.md)
  A determiner, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.pronoun](./nsgrammaticalpartofspeech/pronoun.md)
  A pronoun, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.letter](./nsgrammaticalpartofspeech/letter.md)
  A letter, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.adverb](./nsgrammaticalpartofspeech/adverb.md)
  An adverb, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.particle](./nsgrammaticalpartofspeech/particle.md)
  A particle, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.adjective](./nsgrammaticalpartofspeech/adjective.md)
  An adjective, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.adposition](./nsgrammaticalpartofspeech/adposition.md)
  An adposition, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.verb](./nsgrammaticalpartofspeech/verb.md)
  A verb, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.noun](./nsgrammaticalpartofspeech/noun.md)
  A noun, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.conjunction](./nsgrammaticalpartofspeech/conjunction.md)
  A conjunction, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.numeral](./nsgrammaticalpartofspeech/numeral.md)
  A numeral, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.interjection](./nsgrammaticalpartofspeech/interjection.md)
  An interjection, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.preposition](./nsgrammaticalpartofspeech/preposition.md)
  A preposition, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.abbreviation](./nsgrammaticalpartofspeech/abbreviation.md)
  An abbreviation, as used as a part of speech.
- [NSGrammaticalPartOfSpeech.notSet](./nsgrammaticalpartofspeech/notset.md)
  A value that indicates the part of speech is unset.
### Initializers
- [init?(rawValue: Int)](./nsgrammaticalpartofspeech/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Grammatical Properties
- [enum NSGrammaticalGender](./nsgrammaticalgender.md)
  A representation of grammatical gender, used for inflecting strings.
- [enum NSGrammaticalNumber](./nsgrammaticalnumber.md)
  A representation of grammatical number, used for inflecting strings.
- [unspecified](./nsmorphology/unspecified.md)
  A Boolean value that indicates whether this instance specifies no particular grammar.
- [grammaticalGender](./nsmorphology/grammaticalgender.md)
  The grammatical gender used for inflecting strings with this morphology.
- [number](./nsmorphology/number.md)
  The grammatical number used for inflecting strings with this morphology.
- [partOfSpeech](./nsmorphology/partofspeech.md)
  The grammatical part of speech used for inflecting strings with this morphology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgrammaticalpartofspeech)*