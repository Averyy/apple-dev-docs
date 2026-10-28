# Morphology.CustomPronoun

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A custom pronoun behavior for use in a specific langauge.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- tvOS 15.0+ - Deprecated in 17.0
- visionOS 1.0+
- watchOS 8.0+ - Deprecated in 10.0

> **Deprecated**: Use TermOfAddress instead

## Declaration

```swift
struct CustomPronoun
```

## Overview

Set a [`Morphology.CustomPronoun`](./custompronoun.md) instance on a [`Morphology`](../morphology.md) instance when you want to provide a langauge-specific customization of pronoun use in that language. Different languages have different requirements for the grammatical information needed to apply a custom pronoun, so you set custom pronoun behavior on a per-language basis.

The example below shows how to create English “ze” and “hir” custom pronouns:

```swift
let ze = Morphology.CustomPronoun()
ze.subjectForm = "ze"
ze.objectForm = "hir"
ze.possessiveForm = "hir"
ze.possessiveAdjectiveForm = "hir"
ze.reflexiveForm = "hirself"
```

[`Morphology.CustomPronoun`](./custompronoun.md) only supports third-person pronouns. Use this feature when your app needs to refer to third parties with a specific pronoun.

## Topics

### Creating a Custom Pronoun
- [init()](./custompronoun/init%28%29.md)
  Creates an empty custom pronoun.
### Assessing Custom Pronoun Support
- [static func isSupported(forLanguage: String) -> Bool](./custompronoun/issupported%28forlanguage%29.md)
  Returns a Boolean value that indicates whether the given language supports setting custom pronouns.
- [static func requiredKeys(forLanguage: String) -> [PartialKeyPath<Morphology.CustomPronoun>]](./custompronoun/requiredkeys%28forlanguage%29.md)
  Returns a collection of the custom pronoun keys required by this language.
### Determining Pronoun Forms
- [var subjectForm: String?](./custompronoun/subjectform.md)
  The subject pronoun form to apply when using this custom pronoun behavior.
- [var objectForm: String?](./custompronoun/objectform.md)
  The object pronoun form to apply when using this custom pronoun behavior.
- [var possessiveForm: String?](./custompronoun/possessiveform.md)
  The posessive pronoun form to apply when using this custom pronoun behavior.
- [var possessiveAdjectiveForm: String?](./custompronoun/possessiveadjectiveform.md)
  The posessive adjective pronoun form to apply when using this custom pronoun behavior.
- [var reflexiveForm: String?](./custompronoun/reflexiveform.md)
  The reflexive pronoun form to apply when using this custom pronoun behavior.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Per-Language Features
- [func setCustomPronoun(Morphology.CustomPronoun?, forLanguage: String) throws](./setcustompronoun%28_,forlanguage%29.md)
  Sets a custom pronoun behavior for this morphology to apply to the given language.
- [func customPronoun(forLanguage: String) -> Morphology.CustomPronoun?](./custompronoun%28forlanguage%29.md)
  Returns any custom pronoun behavior this morphology applies to the given language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/custompronoun)*