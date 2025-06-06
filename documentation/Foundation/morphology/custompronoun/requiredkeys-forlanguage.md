# requiredKeys(forLanguage:)

**Framework**: Foundation  
**Kind**: method

Returns a collection of the custom pronoun keys required by this language.

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
static func requiredKeys(forLanguage language: String) -> [PartialKeyPath<Morphology.CustomPronoun>]
```

#### Return Value

The keys required for the given language.

#### Discussion

If any of the required keys for a given language are unset, calling [`setCustomPronoun(_:forLanguage:)`](morphology/setcustompronoun(_:forlanguage:).md) for that language with an incomplete [`Morphology.CustomPronoun`](morphology/custompronoun.md) instance throws an error.

## Parameters

- `language`: The language to create a custom pronoun for.

## See Also

- [static func isSupported(forLanguage: String) -> Bool](morphology/custompronoun/issupported(forlanguage:).md)
  Returns a Boolean value that indicates whether the given language supports setting custom pronouns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/morphology/custompronoun/requiredkeys(forlanguage:))*