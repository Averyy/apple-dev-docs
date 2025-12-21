# AttributeScopes.FoundationAttributes.AgreementArgumentAttribute

**Framework**: Foundation  
**Kind**: enum

An attribute that represents grammatical agreement with an argument in a localized string.

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
enum AgreementArgumentAttribute
```

#### Overview

Many languages require grammatical agreement in their sentences. In Spanish, for example, the adjectives and verbs need to agree with the gender of the subject they refer to in the sentence. For example, suppose you need to translate the following sentence into Spanish:  The correct translation is: 

The challenge is that, most often, the localization file only contains masculine forms of translated words. So, in this sentence, the masculine words for  and ,  and , need to inflect and become  and  to agree with the feminine subject of the sentence ().

You can make the first part of the sentence grammatically agree by inflecting the words  and  together using the `inflect` attribute. Because  is the feminine subject of the sentence, masculine  inflects to feminine .

The second part of the sentence, however, requires the `agreeWithArgument` attribute. Although  is at the end of the sentence, it needs to inflect on the subject, , which is at the beginning. By wrapping  in an `agreeWithArgument` attribute and pointing it to the feminine word , masculine  inflects to feminine , making the entire sentence agree.

Using `agreeWithArgument` this way eliminates the need for the localization file to include both the masculine and the feminine forms of each word. By wrapping the words needing inflection, and then pointing them to the words they need to agree with, the system achieves agreement in the localized text for you.

The following steps ensure proper gender agreement in the translation:

1. Create a type containing all the words you need for translation. For example, create an `Order` structure containing two localizable string properties for `item` and `size`.
2. Add the necessary translations for the food items and the sizes into the Spanish localization file.
3. Create a [`LocalizedStringResource`](localizedstringresource.md) containing the English key phrase from the Spanish localization file to translate, along with placeholder variables representing the words to inflect ( and ).
4. In the Spanish localization file, add `%@` placeholders for the words you want to substitute as part of the translation. Make the Spanish words for the size and the item grammatically agree using the `inflect` attribute with a value of [`true`](https://developer.apple.com/documentation/Swift/true). Then make the masculine Spanish word for  () agree with the feminine word for  () by wrapping  in an `agreeWithArgument` attribute, pointing to the second replacement in the sentence (). Note how the placeholder attributes for , `%1@` and `%2@`, reverse order in the code example below when translating from English to Spanish.
5. Inflect the entire sentence by passing the [`LocalizedStringResource`](localizedstringresource.md) instance into a new instance of [`AttributedString`](attributedstring.md).

```swift
struct Order {
    let item: String
    let size: String
}

let order = Order(item: String(localized: "salad"), size: String(localized: "small"))

// ____________
// In the Spanish localization file:
// "salad" = "ensalada"
// "small" = "pequeño"
// ____________

// Define the resource you want to apply grammatical agreement to.
let resource = LocalizedStringResource("Your \(order.size) \(order.item) is ready.")

// ____________
// In the Spanish localization file:
// "Your %1@ %2@ is ready." = "Tu ^[%2$@ %1$@](inflect: true) está ^[listo](agreeWithArgument: 2)."
// ____________

// Make a new string imposing grammatical agreement on the resource from the localized phrase.
let result = AttributedString(localized: resource)
// result == "Tu ensalada pequeña está lista."

```

## Relationships

### Conforms To
- [AttributedStringKey](attributedstringkey.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [DecodableAttributedStringKey](decodableattributedstringkey.md)
- [EncodableAttributedStringKey](encodableattributedstringkey.md)
- [MarkdownDecodableAttributedStringKey](markdowndecodableattributedstringkey.md)

## See Also

- [let inflect: AttributeScopes.FoundationAttributes.InflectionRuleAttribute](attributescopes/foundationattributes/inflect.md)
  A scope for accessing an inflection rule attribute.
- [AttributeScopes.FoundationAttributes.InflectionRuleAttribute](attributescopes/foundationattributes/inflectionruleattribute.md)
  A type for using an inflection rule as an attribute.
- [let agreementArgument: AttributeScopes.FoundationAttributes.AgreementArgumentAttribute](attributescopes/foundationattributes/agreementargument.md)
  A scope for accessing an agreement argument attribute.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/agreementargumentattribute)*