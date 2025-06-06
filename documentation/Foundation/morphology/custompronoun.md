# Morphology.CustomPronoun

**Framework**: Foundation  
**Kind**: struct

A custom pronoun behavior for use in a specific langauge.

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
struct CustomPronoun
```

#### Overview

Set a [`Morphology.CustomPronoun`](morphology/custompronoun.md) instance on a [`Morphology`](morphology.md) instance when you want to provide a langauge-specific customization of pronoun use in that language. Different languages have different requirements for the grammatical information needed to apply a custom pronoun, so you set custom pronoun behavior on a per-language basis.

The example below shows how to create English “ze” and “hir” custom pronouns:

```swift
let ze = Morphology.CustomPronoun()
ze.subjectForm = "ze"
ze.objectForm = "hir"
ze.possessiveForm = "hir"
ze.possessiveAdjectiveForm = "hir"
ze.reflexiveForm = "hirself"
```

[`Morphology.CustomPronoun`](morphology/custompronoun.md) only supports third-person pronouns. Use this feature when your app needs to refer to third parties with a specific pronoun.

## Topics

### Creating a Custom Pronoun
- [init()](morphology/custompronoun/init.md)
  Creates an empty custom pronoun.
### Assessing Custom Pronoun Support
- [static func isSupported(forLanguage: String) -> Bool](morphology/custompronoun/issupported(forlanguage:).md)
  Returns a Boolean value that indicates whether the given language supports setting custom pronouns.
- [static func requiredKeys(forLanguage: String) -> [PartialKeyPath<Morphology.CustomPronoun>]](morphology/custompronoun/requiredkeys(forlanguage:).md)
  Returns a collection of the custom pronoun keys required by this language.
### Determining Pronoun Forms
- [var subjectForm: String?](morphology/custompronoun/subjectform.md)
  The subject pronoun form to apply when using this custom pronoun behavior.
- [var objectForm: String?](morphology/custompronoun/objectform.md)
  The object pronoun form to apply when using this custom pronoun behavior.
- [var possessiveForm: String?](morphology/custompronoun/possessiveform.md)
  The posessive pronoun form to apply when using this custom pronoun behavior.
- [var possessiveAdjectiveForm: String?](morphology/custompronoun/possessiveadjectiveform.md)
  The posessive adjective pronoun form to apply when using this custom pronoun behavior.
- [var reflexiveForm: String?](morphology/custompronoun/reflexiveform.md)
  The reflexive pronoun form to apply when using this custom pronoun behavior.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setCustomPronoun(Morphology.CustomPronoun?, forLanguage: String) throws](morphology/setcustompronoun(_:forlanguage:).md)
  Sets a custom pronoun behavior for this morphology to apply to the given language.
- [func customPronoun(forLanguage: String) -> Morphology.CustomPronoun?](morphology/custompronoun(forlanguage:).md)
  Returns any custom pronoun behavior this morphology applies to the given language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/custompronoun)*