# NSMorphology

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSMorphology : NSObject
```

## Overview

Use a morphology with an [`NSInflectionRule`](./nsinflectionrule.md) to specify how to interpret a specific word when inflecting an [`NSAttributedString`](./nsattributedstring.md). This affects grammatical agreement with traits like number and gender, as well as declaring the word’s part of speech.

The [`NSMorphology`](./nsmorphology.md) type’s design is language-independent; the concepts it can specify encompass the spectrum of what languages can do. Even for languages that don’t have one or more of those properties benefit the system as hints to make appropriate choices even when an exact inflection isn’t possible. Examples of properties absent from languages include Spanish’s lack of a grammatical gender of neuter, or the nonexistence of a paucal (plural few) pronoun in English.

## Topics

### Accessing the User’s Morphology
- [userMorphology](./nsmorphology/usermorphology.md)
  The addressing preferences of the current user.
### Accessing Grammatical Properties
- [unspecified](./nsmorphology/unspecified.md)
  A Boolean value that indicates whether this instance specifies no particular grammar.
- [grammaticalGender](./nsmorphology/grammaticalgender.md)
  The grammatical gender used for inflecting strings with this morphology.
- [enum NSGrammaticalGender](./nsgrammaticalgender.md)
  A representation of grammatical gender, used for inflecting strings.
- [number](./nsmorphology/number.md)
  The grammatical number used for inflecting strings with this morphology.
- [enum NSGrammaticalNumber](./nsgrammaticalnumber.md)
  A representation of grammatical number, used for inflecting strings.
- [partOfSpeech](./nsmorphology/partofspeech.md)
  The grammatical part of speech used for inflecting strings with this morphology.
- [enum NSGrammaticalPartOfSpeech](./nsgrammaticalpartofspeech.md)
  A representation of grammatical parts of speech, used for inflecting strings.
### Accessing Per-Language Features
- [- setCustomPronoun:forLanguage:error:](./nsmorphology/setcustompronoun_forlanguage_error_.md)
  Sets a custom pronoun behavior for this morphology to apply to the given language.
- [- customPronounForLanguage:](./nsmorphology/custompronounforlanguage_.md)
  Returns any custom pronoun behavior this morphology applies to the given language.
- [NSMorphologyCustomPronoun](./nsmorphologycustompronoun.md)
  A custom pronoun behavior for use in a specific langauge.
### Instance Properties
- [definiteness](./nsmorphology/definiteness.md)
- [determination](./nsmorphology/determination.md)
- [grammaticalCase](./nsmorphology/grammaticalcase.md)
- [grammaticalPerson](./nsmorphology/grammaticalperson.md)
- [pronounType](./nsmorphology/pronountype.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](./nscopying.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Automatic grammar agreement
- [NSInflectionRule](./nsinflectionrule.md)
  A rule that affects how an attributed string performs automatic grammatical agreement.
- [NSInflectionRuleExplicit](./nsinflectionruleexplicit.md)
  An inflection rule that uses a morphology instance to determine how to inflect attribued strings.
- [NSTermOfAddress](./nstermofaddress.md)
  The type for representing grammatical gender in localized text.
- [NSMorphologyPronoun](./nsmorphologypronoun.md)
  A custom pronoun for referring to a third person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmorphology)*