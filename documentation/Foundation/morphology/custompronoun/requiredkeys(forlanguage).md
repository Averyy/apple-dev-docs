# requiredKeys(forLanguage:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a collection of the custom pronoun keys required by this language.

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
static func requiredKeys(forLanguage language: String) -> [PartialKeyPath<Morphology.CustomPronoun>]
```

#### Return Value

The keys required for the given language.

#### Discussion

If any of the required keys for a given language are unset, calling [`setCustomPronoun(_:forLanguage:)`](../setcustompronoun%28_,forlanguage%29.md) for that language with an incomplete [`Morphology.CustomPronoun`](../custompronoun.md) instance throws an error.

## Parameters

- `language`: The language to create a custom pronoun for.

## See Also

### Assessing Custom Pronoun Support
- [static func isSupported(forLanguage: String) -> Bool](./issupported%28forlanguage%29.md)
  Returns a Boolean value that indicates whether the given language supports setting custom pronouns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/custompronoun/requiredkeys(forlanguage:))*