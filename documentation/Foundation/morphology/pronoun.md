# Morphology.Pronoun

**Framework**: Foundation  
**Kind**: struct

A custom pronoun for referring to a third person.

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
struct Pronoun
```

#### Overview

Create instances of [`Morphology.Pronoun`](morphology/pronoun.md) when you need to define custom pronouns for a localized term of address.

For examples of how to create custom pronouns, see [`TermOfAddress`](termofaddress.md).

## Topics

### Creating pronouns
- [init(pronoun: String, morphology: Morphology, dependentMorphology: Morphology?)](morphology/pronoun/init(pronoun:morphology:dependentmorphology:).md)
  Creates a pronoun with the specified name, morphology, and dependent morphology.
### Using pronouns
- [var pronoun: String](morphology/pronoun/pronoun.md)
  The string representation of the pronoun.
- [var morphology: Morphology](morphology/pronoun/morphology.md)
  The morphology of the pronoun form.
- [var dependentMorphology: Morphology?](morphology/pronoun/dependentmorphology.md)
  The dependent morphology of the pronoun form.

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
- [struct Morphology](morphology.md)
  A description of the grammatical properties of a string.
- [struct TermOfAddress](termofaddress.md)
  The type for representing grammatical gender in localized text.
- [enum InflectionConcept](inflectionconcept.md)
  An inflection method to use when localizing text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/pronoun)*