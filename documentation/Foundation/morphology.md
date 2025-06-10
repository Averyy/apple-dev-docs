# Morphology

**Framework**: Foundation  
**Kind**: struct

A description of the grammatical properties of a string.

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
struct Morphology
```

#### Overview

Use a morphology with an [`InflectionRule`](inflectionrule.md) to specify how to interpret a specific word when inflecting an [`AttributedString`](attributedstring.md). This affects grammatical agreement with traits like number and gender, as well as declaring the word’s part of speech.

The [`Morphology`](morphology.md) type’s design is language-independent; the concepts it can specify encompass the spectrum of what languages can do. Even for languages that don’t have one or more of those properties benefit the system as hints to make appropriate choices even when an exact inflection isn’t possible. Examples of properties absent from languages include Spanish’s lack of a grammatical gender of neuter, or the nonexistence of a paucal (plural few) pronoun in English.

## Topics

### Creating a Morphology Instance
- [init()](morphology/init.md)
  Creates an empty morphology instance.
### Accessing the User’s Morphology
- [static let user: Morphology](morphology/user.md)
  The addressing preferences of the current user.
### Accessing Grammatical Properties
- [var isUnspecified: Bool](morphology/isunspecified.md)
  A Boolean value that indicates whether this instance specifies no particular grammar.
- [var grammaticalGender: Morphology.GrammaticalGender?](morphology/grammaticalgender-swift.property.md)
  The grammatical gender used for inflecting strings with this morphology.
- [Morphology.GrammaticalGender](morphology/grammaticalgender-swift.enum.md)
  A representation of grammatical gender, used for inflecting strings.
- [var number: Morphology.GrammaticalNumber?](morphology/number.md)
  The grammatical number used for inflecting strings with this morphology.
- [Morphology.GrammaticalNumber](morphology/grammaticalnumber.md)
  A representation of grammatical number, used for inflecting strings.
- [var partOfSpeech: Morphology.PartOfSpeech?](morphology/partofspeech-swift.property.md)
  The grammatical part of speech used for inflecting strings with this morphology.
- [Morphology.PartOfSpeech](morphology/partofspeech-swift.enum.md)
  A representation of grammatical parts of speech, used for inflecting strings.
### Accessing Per-Language Features
- [func setCustomPronoun(Morphology.CustomPronoun?, forLanguage: String) throws](morphology/setcustompronoun(_:forlanguage:).md)
  Sets a custom pronoun behavior for this morphology to apply to the given language.
- [func customPronoun(forLanguage: String) -> Morphology.CustomPronoun?](morphology/custompronoun(forlanguage:).md)
  Returns any custom pronoun behavior this morphology applies to the given language.
- [Morphology.CustomPronoun](morphology/custompronoun.md)
  A custom pronoun behavior for use in a specific langauge.
### Structures
- [Morphology.Pronoun](morphology/pronoun.md)
  A custom pronoun for referring to a third person.
### Instance Properties
- [var definiteness: Morphology.Definiteness?](morphology/definiteness-swift.property.md)
- [var determination: Morphology.Determination?](morphology/determination-swift.property.md)
- [var grammaticalCase: Morphology.GrammaticalCase?](morphology/grammaticalcase-swift.property.md)
- [var grammaticalPerson: Morphology.GrammaticalPerson?](morphology/grammaticalperson-swift.property.md)
- [var pronounType: Morphology.PronounType?](morphology/pronountype-swift.property.md)
### Enumerations
- [Morphology.Definiteness](morphology/definiteness-swift.enum.md)
- [Morphology.Determination](morphology/determination-swift.enum.md)
- [Morphology.GrammaticalCase](morphology/grammaticalcase-swift.enum.md)
- [Morphology.GrammaticalPerson](morphology/grammaticalperson-swift.enum.md)
- [Morphology.PronounType](morphology/pronountype-swift.enum.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum InflectionRule](inflectionrule.md)
  A rule that affects how an attributed string performs automatic grammatical agreement.
- [struct TermOfAddress](termofaddress.md)
  The type for representing grammatical gender in localized text.
- [enum InflectionConcept](inflectionconcept.md)
  An inflection method to use when localizing text.
- [Morphology.Pronoun](morphology/pronoun.md)
  A custom pronoun for referring to a third person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology)*