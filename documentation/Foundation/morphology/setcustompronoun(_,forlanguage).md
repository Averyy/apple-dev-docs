# setCustomPronoun(_:forLanguage:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets a custom pronoun behavior for this morphology to apply to the given language.

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
mutating func setCustomPronoun(_ pronoun: Morphology.CustomPronoun?, forLanguage language: String) throws
```

## Discussion

This method throws if the system doesn’t support custom pronouns for the given language, or if any of the required pronoun keys aren’t set.

## Parameters

- `pronoun`: A [`Morphology.CustomPronoun`](./custompronoun.md) instance for the morphology to use.
- `language`: The language the morphology should apply the custom pronoun to.

## See Also

### Related Documentation
- [static func isSupported(forLanguage: String) -> Bool](./custompronoun/issupported%28forlanguage%29.md)
  Returns a Boolean value that indicates whether the given language supports setting custom pronouns.
- [static func requiredKeys(forLanguage: String) -> [PartialKeyPath<Morphology.CustomPronoun>]](./custompronoun/requiredkeys%28forlanguage%29.md)
  Returns a collection of the custom pronoun keys required by this language.
### Accessing Per-Language Features
- [func customPronoun(forLanguage: String) -> Morphology.CustomPronoun?](./custompronoun%28forlanguage%29.md)
  Returns any custom pronoun behavior this morphology applies to the given language.
- [Morphology.CustomPronoun](./custompronoun.md)
  A custom pronoun behavior for use in a specific langauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/setcustompronoun(_:forlanguage:))*