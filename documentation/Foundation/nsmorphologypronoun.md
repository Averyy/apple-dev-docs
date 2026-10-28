# NSMorphologyPronoun

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSMorphologyPronoun : NSObject
```

## Overview

Create instances of [`NSMorphologyPronoun`](./nsmorphologypronoun.md) when you need to define custom pronouns for a localized term of address.

For examples of how to create custom pronouns, see [`TermOfAddress`](./termofaddress.md).

## Topics

### Using pronouns
- [pronoun](./nsmorphologypronoun/pronoun.md)
- [morphology](./nsmorphologypronoun/morphology.md)
- [dependentMorphology](./nsmorphologypronoun/dependentmorphology.md)
### Instance Methods
- [- initWithPronoun:morphology:dependentMorphology:](./nsmorphologypronoun/initwithpronoun_morphology_dependentmorphology_.md)

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
- [NSTermOfAddress](./nstermofaddress.md)
  The type for representing grammatical gender in localized text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmorphologypronoun)*