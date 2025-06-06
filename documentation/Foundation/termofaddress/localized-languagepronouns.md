# localized(language:pronouns:)

**Framework**: Foundation  
**Kind**: method

Returns a term of address restricted to a specific language for a group of pronouns.

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
static func localized(language: Locale.Language, pronouns: [Morphology.Pronoun]) -> TermOfAddress
```

#### Return Value

A term of address associating a group of pronouns  to a specific language.

## Parameters

- `language`: The language locale to use for the term of address.
- `pronouns`: The pronouns for representing the terms of address.

## See Also

- [var language: Locale.Language?](termofaddress/language.md)
  The specific language associated with a term of address.
- [var pronouns: [Morphology.Pronoun]](termofaddress/pronouns.md)
  The pronouns associated with a term of address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/termofaddress/localized(language:pronouns:))*