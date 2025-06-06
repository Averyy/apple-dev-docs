# customPronoun(forLanguage:)

**Framework**: Foundation  
**Kind**: method

Returns any custom pronoun behavior this morphology applies to the given language.

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
func customPronoun(forLanguage language: String) -> Morphology.CustomPronoun?
```

#### Return Value

A [`Morphology.CustomPronoun`](morphology/custompronoun.md) behavior this morphology uses for the given language, or `nil` if the morphology doesn’t have a custom pronoun behavior set.

## Parameters

- `language`: The language to query for any custom pronoun behavior.

## See Also

- [func setCustomPronoun(Morphology.CustomPronoun?, forLanguage: String) throws](morphology/setcustompronoun(_:forlanguage:).md)
  Sets a custom pronoun behavior for this morphology to apply to the given language.
- [Morphology.CustomPronoun](morphology/custompronoun.md)
  A custom pronoun behavior for use in a specific langauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/custompronoun(forlanguage:))*