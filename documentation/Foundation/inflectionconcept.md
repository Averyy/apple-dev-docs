# InflectionConcept

**Framework**: Foundation  
**Kind**: enum

An inflection method to use when localizing text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum InflectionConcept
```

#### Overview

Use `InflectionConcept` when you want to make a localizable string grammatically agree with a phrase or term of address that isn’t part of the text you’re localizing. Set [`InflectionConcept`](inflectionconcept.md) on the [`concepts`](attributedstring/localizationoptions/concepts.md) property of [`AttributedString.LocalizationOptions`](attributedstring/localizationoptions.md) to specify the inflection concepts to use while inflecting text.

For examples of how to use inflection concepts, see:

- [`AttributeScopes.FoundationAttributes.ReferentConceptAttribute`](attributescopes/foundationattributes/referentconceptattribute.md)
- [`AttributeScopes.FoundationAttributes.AgreementConceptAttribute`](attributescopes/foundationattributes/agreementconceptattribute.md)

## Topics

### Using inflection concepts
- [InflectionConcept.termsOfAddress(_:)](inflectionconcept/termsofaddress(_:).md)
  Indicates that the system uses the associated terms of address for grammatical agreement when localizing text.
- [InflectionConcept.localizedPhrase(_:)](inflectionconcept/localizedphrase(_:).md)
  Indicates that the system uses the associated string for grammatical agreement when localizing text.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum InflectionRule](inflectionrule.md)
  A rule that affects how an attributed string performs automatic grammatical agreement.
- [struct Morphology](morphology.md)
  A description of the grammatical properties of a string.
- [struct TermOfAddress](termofaddress.md)
  The type for representing grammatical gender in localized text.
- [Morphology.Pronoun](morphology/pronoun.md)
  A custom pronoun for referring to a third person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inflectionconcept)*