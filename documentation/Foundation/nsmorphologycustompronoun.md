# NSMorphologyCustomPronoun

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A custom pronoun behavior for use in a specific langauge.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- tvOS 15.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 8.0+ - Deprecated in 10.0

## Declaration

```objc
@interface NSMorphologyCustomPronoun : NSObject
```

## Overview

Set a [`NSMorphologyCustomPronoun`](./nsmorphologycustompronoun.md) instance on a [`NSMorphology`](./nsmorphology.md) instance when you want to provide a langauge-specific customization of pronoun use in that language. Different languages have different requirements for the grammatical information needed to apply a custom pronoun, so you set custom pronoun behavior on a per-language basis.

The example below shows how to create English “ze” and “hir” custom pronouns:

```objc
let ze = [[NSMorphologyCustomPronoun alloc] init];
ze.subjectForm = "ze";
ze.objectForm = "hir";
ze.possessiveForm = "hir";
ze.possessiveAdjectiveForm = "hir";
ze.reflexiveForm = "hirself";
```

[`NSMorphologyCustomPronoun`](./nsmorphologycustompronoun.md) only supports third-person pronouns. Use this feature when your app needs to refer to third parties with a specific pronoun.

## Topics

### Assessing Custom Pronoun Support
- [+ isSupportedForLanguage:](./nsmorphologycustompronoun/issupportedforlanguage_.md)
  Returns a Boolean value that indicates whether the given language supports setting custom pronouns.
- [+ requiredKeysForLanguage:](./nsmorphologycustompronoun/requiredkeysforlanguage_.md)
  Returns a collection of the custom pronoun keys required by this language.
### Determining Pronoun Forms
- [subjectForm](./nsmorphologycustompronoun/subjectform.md)
  The subject pronoun form to apply when using this custom pronoun behavior.
- [objectForm](./nsmorphologycustompronoun/objectform.md)
  The object pronoun form to apply when using this custom pronoun behavior.
- [possessiveForm](./nsmorphologycustompronoun/possessiveform.md)
  The posessive pronoun form to apply when using this custom pronoun behavior.
- [possessiveAdjectiveForm](./nsmorphologycustompronoun/possessiveadjectiveform.md)
  The posessive adjective pronoun form to apply when using this custom pronoun behavior.
- [reflexiveForm](./nsmorphologycustompronoun/reflexiveform.md)
  The reflexive pronoun form to apply when using this custom pronoun behavior.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](./nscopying.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Accessing Per-Language Features
- [- setCustomPronoun:forLanguage:error:](./nsmorphology/setcustompronoun_forlanguage_error_.md)
  Sets a custom pronoun behavior for this morphology to apply to the given language.
- [- customPronounForLanguage:](./nsmorphology/custompronounforlanguage_.md)
  Returns any custom pronoun behavior this morphology applies to the given language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmorphologycustompronoun)*