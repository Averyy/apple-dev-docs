# language

**Framework**: Foundation  
**Kind**: property

The specific language associated with a term of address.

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
var language: Locale.Language? { get }
```

#### Discussion

This property is only set for terms of address created through the [`localized(language:pronouns:)`](termofaddress/localized(language:pronouns:).md) function. This property is `nil` otherwise.

## See Also

- [static func localized(language: Locale.Language, pronouns: [Morphology.Pronoun]) -> TermOfAddress](termofaddress/localized(language:pronouns:).md)
  Returns a term of address restricted to a specific language for a group of pronouns.
- [var pronouns: [Morphology.Pronoun]](termofaddress/pronouns.md)
  The pronouns associated with a term of address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/termofaddress/language)*