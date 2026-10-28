# AttributeScopes.FoundationAttributes.ReferentConceptAttribute

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

An attribute that specifies a grammatical agreement concept for substituting pronouns in localized text.

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
@frozen
enum ReferentConceptAttribute
```

## Overview

Use the [`referentConcept`](./referentconcept.md) formatting attribute for cases where you need to refer to a person using their preferred pronoun in a string.

For an example of how to use a `referentConcept`, see [`TermOfAddress`](../../termofaddress.md).

## Relationships

### Conforms To
- [AttributedStringKey](../../attributedstringkey.md)
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Copyable](../../../Swift/copyable.md)
- [DecodableAttributedStringKey](../../decodableattributedstringkey.md)
- [EncodableAttributedStringKey](../../encodableattributedstringkey.md)
- [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Using automatic grammar agreement attributes
- [let inflect: AttributeScopes.FoundationAttributes.InflectionRuleAttribute](./inflect.md)
  A scope for accessing an inflection rule attribute.
- [AttributeScopes.FoundationAttributes.InflectionRuleAttribute](./inflectionruleattribute.md)
  A type for using an inflection rule as an attribute.
- [let agreementArgument: AttributeScopes.FoundationAttributes.AgreementArgumentAttribute](./agreementargument.md)
  A scope for accessing an agreement argument attribute.
- [AttributeScopes.FoundationAttributes.AgreementArgumentAttribute](./agreementargumentattribute.md)
  An attribute that represents grammatical agreement with an argument in a localized string.
- [let agreementConcept: AttributeScopes.FoundationAttributes.AgreementConceptAttribute](./agreementconcept.md)
  A scope for accessing an agreement concept attribute.
- [AttributeScopes.FoundationAttributes.AgreementConceptAttribute](./agreementconceptattribute.md)
  An attribute that represents grammatical agreement for objects that aren’t part of the inflected text.
- [let morphology: AttributeScopes.FoundationAttributes.MorphologyAttribute](./morphology.md)
  A scope for accessing a morphology attribute.
- [AttributeScopes.FoundationAttributes.MorphologyAttribute](./morphologyattribute.md)
  A type for using a morphology as an attribute.
- [let referentConcept: AttributeScopes.FoundationAttributes.ReferentConceptAttribute](./referentconcept.md)
  A scope for accessing a referent concept attribute.
- [let inflectionAlternative: AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute](./inflectionalternative.md)
  A scope for accessing an inflection alternative attribute.
- [AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute](./inflectionalternativeattribute.md)
  An attribute that provides an alternative inflection phrase when the system can’t achieve grammatical agreement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/referentconceptattribute)*