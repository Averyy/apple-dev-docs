# AttributeScopes.FoundationAttributes.PossessorMorphologyAttribute

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

An attribute for specifying the morphology of a grammatical possessor. Use this in localized strings to specify that an argument needs to have a possessive suffix added.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
@frozen
enum PossessorMorphologyAttribute
```

## Overview

In Turkish, specify `gramamticalPerson` and `number` in the morphology. The localization engine will choose the correct suffix based on the possessor, and the preceding word. For example, the localized string

```
^[%@](possessorMorphology: {grammaticalPerson: 'second', number: 'one'})
```

will be formatted as *“iPhone’un”* (“your iPhone”), when the argument is “iPhone”, and as *“iPad’in”* (“your iPad”) when the argument is “iPad”.

This may be combined with the `inflect` attribute. For example:

```
^[%@](possessorMorphology: {grammaticalPerson: 'second', number: 'one'}, inflect: {grammaticalCase: 'locative'})
```

will be formatted as *“iPhone’unuzda”* (“on your iPhone”), when the argument is “iPhone”, and as *“iPad’inizde”* (“on your iPad”) when the argument is “iPad”.

## Relationships

### Conforms To
- [AttributedStringKey](../../attributedstringkey.md)
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Copyable](../../../Swift/copyable.md)
- [DecodableAttributedStringKey](../../decodableattributedstringkey.md)
- [EncodableAttributedStringKey](../../encodableattributedstringkey.md)
- [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/possessormorphologyattribute)*