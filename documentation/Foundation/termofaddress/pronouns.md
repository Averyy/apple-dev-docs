# pronouns

**Framework**: Foundation  
**Kind**: property

The pronouns associated with a term of address.

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
var pronouns: [Morphology.Pronoun] { get }
```

#### Discussion

This property is only set for terms of address created through the [`localized(language:pronouns:)`](termofaddress/localized(language:pronouns:).md) function. Calling this property returns an empty array otherwise.

## See Also

- [static func localized(language: Locale.Language, pronouns: [Morphology.Pronoun]) -> TermOfAddress](termofaddress/localized(language:pronouns:).md)
  Returns a term of address restricted to a specific language for a group of pronouns.
- [var language: Locale.Language?](termofaddress/language.md)
  The specific language associated with a term of address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/termofaddress/pronouns)*