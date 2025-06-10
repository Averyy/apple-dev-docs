# AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute

**Framework**: Foundation  
**Kind**: enum

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

For example, suppose you want to inflect the masculine form for  in Spanish, , but the system doesn’t know the person’s preferred terms of address. Add an `inflectionAlternative` to your [`LocalizedStringResource`](localizedstringresource.md), setting the alternative word or phrase in single quotation marks. The system uses the alternative when it can’t determine proper grammatical agreement.

```swift
// Define the resource with an inflection alternative.
let resource = LocalizedStringResource("^[Bienvenido](inflect: true, inflectionAlternative: 'Te damos la bienvenida').")

// Use the inflection alternative when the system can't determine agreement.
let result = AttributedString(localized: resource)
// result == "Te damos la bienvenida."
```

## Relationships

### Conforms To
- [AttributedStringKey](attributedstringkey.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [DecodableAttributedStringKey](decodableattributedstringkey.md)
- [EncodableAttributedStringKey](encodableattributedstringkey.md)
- [MarkdownDecodableAttributedStringKey](markdowndecodableattributedstringkey.md)
- [ObjectiveCConvertibleAttributedStringKey](objectivecconvertibleattributedstringkey.md)

## See Also

- [let inflect: AttributeScopes.FoundationAttributes.InflectionRuleAttribute](attributescopes/foundationattributes/inflect.md)
  A scope for accessing an inflection rule attribute.
- [AttributeScopes.FoundationAttributes.InflectionRuleAttribute](attributescopes/foundationattributes/inflectionruleattribute.md)
  A type for using an inflection rule as an attribute.
- [let agreementArgument: AttributeScopes.FoundationAttributes.AgreementArgumentAttribute](attributescopes/foundationattributes/agreementargument.md)
  A scope for accessing an agreement argument attribute.
- [AttributeScopes.FoundationAttributes.AgreementArgumentAttribute](attributescopes/foundationattributes/agreementargumentattribute.md)
  An attribute that represents grammatical agreement with an argument in a localized string.
- [let agreementConcept: AttributeScopes.FoundationAttributes.AgreementConceptAttribute](attributescopes/foundationattributes/agreementconcept.md)
  A scope for accessing an agreement concept attribute.
- [AttributeScopes.FoundationAttributes.AgreementConceptAttribute](attributescopes/foundationattributes/agreementconceptattribute.md)
  An attribute that represents grammatical agreement for objects that aren’t part of the inflected text.
- [let morphology: AttributeScopes.FoundationAttributes.MorphologyAttribute](attributescopes/foundationattributes/morphology.md)
  A scope for accessing a morphology attribute.
- [AttributeScopes.FoundationAttributes.MorphologyAttribute](attributescopes/foundationattributes/morphologyattribute.md)
  A type for using a morphology as an attribute.
- [let referentConcept: AttributeScopes.FoundationAttributes.ReferentConceptAttribute](attributescopes/foundationattributes/referentconcept.md)
  A scope for accessing a referent concept attribute.
- [AttributeScopes.FoundationAttributes.ReferentConceptAttribute](attributescopes/foundationattributes/referentconceptattribute.md)
  An attribute that specifies a grammatical agreement concept for substituting pronouns in localized text.
- [let inflectionAlternative: AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute](attributescopes/foundationattributes/inflectionalternative.md)
  A scope for accessing an inflection alternative attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/inflectionalternativeattribute)*