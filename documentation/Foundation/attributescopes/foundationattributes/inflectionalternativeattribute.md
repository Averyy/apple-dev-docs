# AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

An attribute that provides an alternative inflection phrase when the system can’t achieve grammatical agreement.

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
@frozen
enum InflectionAlternativeAttribute
```

#### Overview

Use the `inflectionAlternativeAttribute` to provide an alternative phrase for cases where the system can’t achieve unambiguous grammatical agreement.

For example, suppose you want to inflect the masculine form for *welcome* in Spanish, *bienvenido*, but the system doesn’t know the person’s preferred terms of address. Add an `inflectionAlternative` to your [`LocalizedStringResource`](../../localizedstringresource.md), setting the alternative word or phrase in single quotation marks. The system uses the alternative when it can’t determine proper grammatical agreement.

```swift
// Define the resource with an inflection alternative.
let resource = LocalizedStringResource("^[Bienvenido](inflect: true, inflectionAlternative: 'Te damos la bienvenida').")

// Use the inflection alternative when the system can't determine agreement.
let result = AttributedString(localized: resource)
// result == "Te damos la bienvenida."
```

## Relationships

### Conforms To
- [AttributedStringKey](../../attributedstringkey.md)
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Copyable](../../../Swift/copyable.md)
- [DecodableAttributedStringKey](../../decodableattributedstringkey.md)
- [EncodableAttributedStringKey](../../encodableattributedstringkey.md)
- [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md)
- [ObjectiveCConvertibleAttributedStringKey](../../objectivecconvertibleattributedstringkey.md)
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
- [AttributeScopes.FoundationAttributes.ReferentConceptAttribute](./referentconceptattribute.md)
  An attribute that specifies a grammatical agreement concept for substituting pronouns in localized text.
- [let inflectionAlternative: AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute](./inflectionalternative.md)
  A scope for accessing an inflection alternative attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/inflectionalternativeattribute)*