# isSupported(forLanguage:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the given language supports setting custom pronouns.

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
static func isSupported(forLanguage language: String) -> Bool
```

#### Return Value

`true` if the language supports custom pronouns; otherwise, `false`.

#### Discussion

If this value is `false` for a given language, calling [`setCustomPronoun(_:forLanguage:)`](../setcustompronoun%28_,forlanguage%29.md) for that language throws an error.

## Parameters

- `language`: The language to query.

## See Also

### Assessing Custom Pronoun Support
- [static func requiredKeys(forLanguage: String) -> [PartialKeyPath<Morphology.CustomPronoun>]](./requiredkeys%28forlanguage%29.md)
  Returns a collection of the custom pronoun keys required by this language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/custompronoun/issupported(forlanguage:))*