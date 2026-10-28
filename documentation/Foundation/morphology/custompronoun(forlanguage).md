# customPronoun(forLanguage:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns any custom pronoun behavior this morphology applies to the given language.

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
func customPronoun(forLanguage language: String) -> Morphology.CustomPronoun?
```

## Return Value

A [`Morphology.CustomPronoun`](./custompronoun.md) behavior this morphology uses for the given language, or `nil` if the morphology doesn’t have a custom pronoun behavior set.

## Parameters

- `language`: The language to query for any custom pronoun behavior.

## See Also

### Accessing Per-Language Features
- [func setCustomPronoun(Morphology.CustomPronoun?, forLanguage: String) throws](./setcustompronoun%28_,forlanguage%29.md)
  Sets a custom pronoun behavior for this morphology to apply to the given language.
- [Morphology.CustomPronoun](./custompronoun.md)
  A custom pronoun behavior for use in a specific langauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/custompronoun(forlanguage:))*