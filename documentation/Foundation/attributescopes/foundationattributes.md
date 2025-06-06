# AttributeScopes.FoundationAttributes

**Framework**: Foundation  
**Kind**: struct

Attribute scopes that Foundation defines.

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
struct FoundationAttributes
```

## Topics

### Using date attributes
- [let dateField: AttributeScopes.FoundationAttributes.DateFieldAttribute](attributescopes/foundationattributes/datefield.md)
  A property for accessing a date field attribute.
- [AttributeScopes.FoundationAttributes.DateFieldAttribute](attributescopes/foundationattributes/datefieldattribute.md)
  A type for using a date field as an attribute.
### Using language attributes
- [let languageIdentifier: AttributeScopes.FoundationAttributes.LanguageIdentifierAttribute](attributescopes/foundationattributes/languageidentifier.md)
  A property for accessing a language identifier attribute.
- [AttributeScopes.FoundationAttributes.LanguageIdentifierAttribute](attributescopes/foundationattributes/languageidentifierattribute.md)
  A type for using a language identifier as an attribute.
### Using URL attributes
- [let imageURL: AttributeScopes.FoundationAttributes.ImageURLAttribute](attributescopes/foundationattributes/imageurl.md)
  A property for accessing an image URL attribute.
- [AttributeScopes.FoundationAttributes.ImageURLAttribute](attributescopes/foundationattributes/imageurlattribute.md)
  A type for using an image URL as an attribute.
- [let link: AttributeScopes.FoundationAttributes.LinkAttribute](attributescopes/foundationattributes/link.md)
  A property for accessing the link attribute.
- [AttributeScopes.FoundationAttributes.LinkAttribute](attributescopes/foundationattributes/linkattribute.md)
  A type for using a link as an attribute.
### Using presentation intent attributes
- [let inlinePresentationIntent: AttributeScopes.FoundationAttributes.InlinePresentationIntentAttribute](attributescopes/foundationattributes/inlinepresentationintent.md)
  A property for accessing an inline presentation intent attribute.
- [AttributeScopes.FoundationAttributes.InlinePresentationIntentAttribute](attributescopes/foundationattributes/inlinepresentationintentattribute.md)
  A type for using an inline presentation intent as an attribute.
- [struct InlinePresentationIntent](inlinepresentationintent.md)
  A type that defines presentation intent for runs of characters for traits like emphasis, strikethrough, and code voice.
- [let presentationIntent: AttributeScopes.FoundationAttributes.PresentationIntentAttribute](attributescopes/foundationattributes/presentationintent.md)
  A property for accessing a presentation intent attribute.
- [AttributeScopes.FoundationAttributes.PresentationIntentAttribute](attributescopes/foundationattributes/presentationintentattribute.md)
  A type for using a presentation intent as an attribute.
- [struct PresentationIntent](presentationintent.md)
  A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.
### Using alternative description attributes
- [let alternateDescription: AttributeScopes.FoundationAttributes.AlternateDescriptionAttribute](attributescopes/foundationattributes/alternatedescription.md)
  A property for accessing an alternative presentation attribute.
- [AttributeScopes.FoundationAttributes.AlternateDescriptionAttribute](attributescopes/foundationattributes/alternatedescriptionattribute.md)
  A type for using an alternative description as an attribute.
### Using string formatting attributes
- [let replacementIndex: AttributeScopes.FoundationAttributes.ReplacementIndexAttribute](attributescopes/foundationattributes/replacementindex.md)
  A property for accessing a replacement index attribute.
- [AttributeScopes.FoundationAttributes.ReplacementIndexAttribute](attributescopes/foundationattributes/replacementindexattribute.md)
  A type for using a replacement index as an attribute.
### Using string localization attributes
- [let localizedStringArgumentAttributes: AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes](attributescopes/foundationattributes/localizedstringargumentattributes-swift.property.md)
  A property for accessing a localized string argument attribute.
- [AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct.md)
  A type for using a localized string argument as an attribute.
### Using automatic grammar agreement attributes
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
- [AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute](attributescopes/foundationattributes/inflectionalternativeattribute.md)
  An attribute that provides an alternative inflection phrase when the system can’t achieve grammatical agreement.
### Using number formatting attributes
- [let numberFormat: AttributeScopes.FoundationAttributes.NumberFormatAttributes](attributescopes/foundationattributes/numberformat.md)
  A property for accessing a number format attribute.
- [AttributeScopes.FoundationAttributes.NumberFormatAttributes](attributescopes/foundationattributes/numberformatattributes.md)
  A type for using a number format as an attribute.
### Using person name component attributes
- [let personNameComponent: AttributeScopes.FoundationAttributes.PersonNameComponentAttribute](attributescopes/foundationattributes/personnamecomponent.md)
  A property for accessing a person name component attribute.
- [AttributeScopes.FoundationAttributes.PersonNameComponentAttribute](attributescopes/foundationattributes/personnamecomponentattribute.md)
  A type for using a person name component as an attribute.
### Using Markdown source position attributes
- [let markdownSourcePosition: AttributeScopes.FoundationAttributes.MarkdownSourcePositionAttribute](attributescopes/foundationattributes/markdownsourceposition.md)
  A property for accessing a Markdown source position attribute.
- [AttributeScopes.FoundationAttributes.MarkdownSourcePositionAttribute](attributescopes/foundationattributes/markdownsourcepositionattribute.md)
  A type for using a markdown source position as an attribute.
### Structures
- [AttributeScopes.FoundationAttributes.MeasurementAttribute](attributescopes/foundationattributes/measurementattribute.md)
### Instance Properties
- [let byteCount: AttributeScopes.FoundationAttributes.ByteCountAttribute](attributescopes/foundationattributes/bytecount.md)
- [let durationField: AttributeScopes.FoundationAttributes.DurationFieldAttribute](attributescopes/foundationattributes/durationfield.md)
- [let localizedNumberFormat: AttributeScopes.FoundationAttributes.LocalizedNumberFormatAttribute](attributescopes/foundationattributes/localizednumberformat.md)
- [let measurement: AttributeScopes.FoundationAttributes.MeasurementAttribute](attributescopes/foundationattributes/measurement.md)
### Enumerations
- [AttributeScopes.FoundationAttributes.ByteCountAttribute](attributescopes/foundationattributes/bytecountattribute.md)
- [AttributeScopes.FoundationAttributes.DurationFieldAttribute](attributescopes/foundationattributes/durationfieldattribute.md)
- [AttributeScopes.FoundationAttributes.LocalizedNumberFormatAttribute](attributescopes/foundationattributes/localizednumberformatattribute.md)

## Relationships

### Conforms To
- [AttributeScope](attributescope.md)
- [DecodingConfigurationProviding](decodingconfigurationproviding.md)
- [EncodingConfigurationProviding](encodingconfigurationproviding.md)

## See Also

- [var foundation: AttributeScopes.FoundationAttributes.Type](attributescopes/foundation.md)
  A property for accessing the attribute scopes that Foundation defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes)*