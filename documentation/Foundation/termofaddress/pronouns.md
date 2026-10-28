# pronouns

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

This property is only set for terms of address created through the [`localized(language:pronouns:)`](./localized%28language,pronouns%29.md) function. Calling this property returns an empty array otherwise.

## See Also

### Defining your own terms of address
- [static func localized(language: Locale.Language, pronouns: [Morphology.Pronoun]) -> TermOfAddress](./localized%28language,pronouns%29.md)
  Returns a term of address restricted to a specific language for a group of pronouns.
- [var language: Locale.Language?](./language.md)
  The specific language associated with a term of address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/termofaddress/pronouns)*