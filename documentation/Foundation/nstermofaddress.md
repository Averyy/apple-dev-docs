# NSTermOfAddress

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

The type for representing grammatical gender in localized text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface NSTermOfAddress : NSObject
```

#### Overview

Many languages rely on gender for their grammar. Without knowing the subject’s gender or pronoun preferences, some localized strings may have grammatical errors, resulting in a poor user experience.

`TermOfAddress` is a type that enables the system to make pronoun substitutions in localized text based on gender. You don’t create instances of this type directly. Instead, use the predefined types to specify the gender to use when referring to people in translated text. Or define your own pronoun terms for a specific language when the predefined types are insufficient.

> **Note**:  Not all terms of address exist in all languages.

For example, to substitute the masculine pronoun *He*, for the neutral pronoun *They*, do the following:

```swift
// Define the resource you want to apply grammatical agreement to.
let resource = LocalizedStringResource("^[They](referentConcept: 1) liked your post.")

// Set the inflection concept to use a term of address.
var options = AttributedString.LocalizationOptions()
options.concepts = [.termsOfAddress([.masculine])]

// Make a new string imposing grammatical agreement on the resource from the term of address.
let result = AttributedString(localized: resource, options: options)
// result == "He liked your post."
```

If the [`masculine`](./nstermofaddress/masculine.md), [`feminine`](./nstermofaddress/feminine.md), and [`neutral`](./nstermofaddress/neutral.md) terms of address are insufficient, create your own term of address specifying the pronouns and language.

```swift
// Define the various morphologies.
var nominativeMorphology = Morphology()
var accusativeMorphology = Morphology()
var genitiveMorphology = Morphology()
var genetiveIndependent = Morphology()
var reflexive = Morphology()

nominativeMorphology.grammaticalCase = .nominative
accusativeMorphology.grammaticalCase = .accusative
genitiveMorphology.grammaticalCase = .genitive
genitiveMorphology.determination = .dependent
genetiveIndependent.grammaticalCase = .genitive
genetiveIndependent.determination = .independent
reflexive.pronounType = .reflexive

// Define the pronouns.
let xey  = Morphology.Pronoun(pronoun:"xey", morphology: nominativeMorphology)
let xem  = Morphology.Pronoun(pronoun:"xem", morphology: accusativeMorphology)
let xeir = Morphology.Pronoun(pronoun:"xeir", morphology: genitiveMorphology)
let xeirs = Morphology.Pronoun(pronoun: "xeirs", morphology: genetiveIndependent)
let xemself = Morphology.Pronoun(pronoun: "xemself", morphology: reflexive)
        
// Create the localized term of address.
let xemTermOfAddress = TermOfAddress.localized(language: .init(identifier: "en"), pronouns: [xey, xem, xeir, xeirs, xemself])

// Define the resources you want to apply gender agreement to.
let resources = [
    LocalizedStringResource("^[They](referentConcept: 1) liked your post."),
    LocalizedStringResource("Anne read the post to ^[them](referentConcept: 1)."),
    LocalizedStringResource("You liked ^[their](referentConcept: 1) post."),
    LocalizedStringResource("The post was ^[theirs](referentConcept: 1)."),
    LocalizedStringResource("^[They](referentConcept: 1) posted it ^[themselves](referentConcept: 1)."),
]
var options = AttributedString.LocalizationOptions()

// Set the inflection concept to use the new term of address.
options.concepts = [.termsOfAddress([xemTermOfAddress])]

let results = [
    AttributedString(localized: resources[0], options: options), // "Xey liked your post."
    AttributedString(localized: resources[1], options: options), // "Anne read the post to xem."
    AttributedString(localized: resources[2], options: options), // "You liked xeir post."
    AttributedString(localized: resources[3], options: options), // "The post was xeirs."
    AttributedString(localized: resources[4], options: options), // "Xey posted it xemself."
]
```

For examples of how to use terms of address, see:

- [`AttributeScopes.FoundationAttributes.ReferentConceptAttribute`](./attributescopes/foundationattributes/referentconceptattribute.md)
- [`AttributeScopes.FoundationAttributes.AgreementConceptAttribute`](./attributescopes/foundationattributes/agreementconceptattribute.md)

## Topics

### Using predefined terms of address
- [+ feminine](./nstermofaddress/feminine.md)
  Term of address that uses feminine pronouns (e.g. she/her/hers in English), and a feminine grammatical gender when inflecting verbs and adjectives referring to the person
- [+ masculine](./nstermofaddress/masculine.md)
  Term of address that uses masculine pronouns (e.g. he/him/his in English), and a masculine grammatical gender when inflecting verbs and adjectives referring to the person
- [+ neutral](./nstermofaddress/neutral.md)
  Term of address that uses gender-neutral pronouns (e.g. they/them/theirs in English), and an epicene grammatical gender when inflecting verbs and adjectives referring to the person
### Defining your own terms of address
- [pronouns](./nstermofaddress/pronouns.md)
  A list of pronouns for a localized term of address
### Instance Properties
- [languageIdentifier](./nstermofaddress/languageidentifier.md)
  The ISO language code if this is a localized term of address
### Type Methods
- [+ currentUser](./nstermofaddress/currentuser.md)
  The term of address that should be used for addressing the user
- [+ localizedForLanguageIdentifier:withPronouns:](./nstermofaddress/localizedforlanguageidentifier_withpronouns_.md)
  A term of address restricted to a given language

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
- [NSMorphology](./nsmorphology.md)
  A description of the grammatical properties of a string.
- [NSMorphologyPronoun](./nsmorphologypronoun.md)
  A custom pronoun for referring to a third person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstermofaddress)*