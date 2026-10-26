# NSInflectionRule

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A rule that affects how an attributed string performs automatic grammatical agreement.

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
@interface NSInflectionRule : NSObject
```

#### Overview

Most apps can rely on loading localized strings to perform automatic grammar agreement. Typically, your app’s strings files use the Markdown extension syntax to indicate portions of the string that may require inflection to agree grammatically. This transformation occurs when you load the attributed string with methods like `NSLocalizedAttributedString`.

However, if the system lacks information about the words in the string, you may need to apply an inflection rule programmatically. For example, a social networking app may have gender information about other users that you want to apply at runtime. When performing manual inflection at runtime, you use an inflection rule to indicate to the system what portions of a string should be automatically edited, and what to match. Add the attribute [`inflectionRule`](./nsattributedstring/key/inflectionrule.md) with an [`NSInflectionRule`](./nsinflectionrule.md) on an [`NSAttributedString`](./nsattributedstring.md), then call [`inflecting()`](./nsattributedstring/inflecting%28%29.md) to perform the grammar agreement and produce an edited string.

## Topics

### Performing Automatic Inflection
- [automaticRule](./nsinflectionrule/automaticrule.md)
  An inflection rule that performs automatic grammar agreement with default transformations.
### Determining Availability
- [+ canInflectLanguage:](./nsinflectionrule/caninflectlanguage_.md)
  Returns a Boolean value that indicates whether the rule can inflect a given language.
- [canInflectPreferredLocalization](./nsinflectionrule/caninflectpreferredlocalization.md)
  A Boolean value that indicates whether the rule can inflect the user’s current preferred localization.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSInflectionRuleExplicit](./nsinflectionruleexplicit.md)
### Conforms To
- [NSCopying](./nscopying.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Automatic grammar agreement
- [NSInflectionRuleExplicit](./nsinflectionruleexplicit.md)
  An inflection rule that uses a morphology instance to determine how to inflect attribued strings.
- [NSMorphology](./nsmorphology.md)
  A description of the grammatical properties of a string.
- [NSTermOfAddress](./nstermofaddress.md)
  The type for representing grammatical gender in localized text.
- [NSMorphologyPronoun](./nsmorphologypronoun.md)
  A custom pronoun for referring to a third person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinflectionrule)*