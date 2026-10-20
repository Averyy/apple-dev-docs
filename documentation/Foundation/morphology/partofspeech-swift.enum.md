# Morphology.PartOfSpeech

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
enum PartOfSpeech
```

## Topics

### Determining Part of Speech
- [Morphology.PartOfSpeech.determiner](./partofspeech-swift.enum/determiner.md)
  A determiner, as used as a part of speech.
- [Morphology.PartOfSpeech.pronoun](./partofspeech-swift.enum/pronoun.md)
  A pronoun, as used as a part of speech.
- [Morphology.PartOfSpeech.letter](./partofspeech-swift.enum/letter.md)
  A letter, as used as a part of speech.
- [Morphology.PartOfSpeech.adverb](./partofspeech-swift.enum/adverb.md)
  An adverb, as used as a part of speech.
- [Morphology.PartOfSpeech.particle](./partofspeech-swift.enum/particle.md)
  A particle, as used as a part of speech.
- [Morphology.PartOfSpeech.adjective](./partofspeech-swift.enum/adjective.md)
  An adjective, as used as a part of speech.
- [Morphology.PartOfSpeech.adposition](./partofspeech-swift.enum/adposition.md)
  An adposition, as used as a part of speech.
- [Morphology.PartOfSpeech.verb](./partofspeech-swift.enum/verb.md)
  A verb, as used as a part of speech.
- [Morphology.PartOfSpeech.noun](./partofspeech-swift.enum/noun.md)
  A noun, as used as a part of speech.
- [Morphology.PartOfSpeech.conjunction](./partofspeech-swift.enum/conjunction.md)
  A conjunction, as used as a part of speech.
- [Morphology.PartOfSpeech.numeral](./partofspeech-swift.enum/numeral.md)
  A numeral, as used as a part of speech.
- [Morphology.PartOfSpeech.interjection](./partofspeech-swift.enum/interjection.md)
  An interjection, as used as a part of speech.
- [Morphology.PartOfSpeech.preposition](./partofspeech-swift.enum/preposition.md)
  A preposition, as used as a part of speech.
- [Morphology.PartOfSpeech.abbreviation](./partofspeech-swift.enum/abbreviation.md)
  An abbreviation, as used as a part of speech.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Grammatical Properties
- [var isUnspecified: Bool](./isunspecified.md)
  A Boolean value that indicates whether this instance specifies no particular grammar.
- [var grammaticalGender: Morphology.GrammaticalGender?](./grammaticalgender-swift.property.md)
  The grammatical gender used for inflecting strings with this morphology.
- [Morphology.GrammaticalGender](./grammaticalgender-swift.enum.md)
  A representation of grammatical gender, used for inflecting strings.
- [var number: Morphology.GrammaticalNumber?](./number.md)
  The grammatical number used for inflecting strings with this morphology.
- [Morphology.GrammaticalNumber](./grammaticalnumber.md)
  A representation of grammatical number, used for inflecting strings.
- [var partOfSpeech: Morphology.PartOfSpeech?](./partofspeech-swift.property.md)
  The grammatical part of speech used for inflecting strings with this morphology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/partofspeech-swift.enum)*