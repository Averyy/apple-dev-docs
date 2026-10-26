# requiredKeysForLanguage:

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
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 8.0+ - Deprecated in 10.0

## Declaration

```objc
+ (NSArray<NSString *> *) requiredKeysForLanguage:(NSString *) language;
```

#### Return Value

The keys required for the given language.

#### Discussion

If any of the required keys for a given language are unset, calling [`setCustomPronoun:forLanguage:error:`](../nsmorphology/setcustompronoun_forlanguage_error_.md) for that language with an incomplete [`NSMorphologyCustomPronoun`](../nsmorphologycustompronoun.md) results in an error.

## Parameters

- `language`: The language to create a custom pronoun for.

## See Also

### Assessing Custom Pronoun Support
- [+ isSupportedForLanguage:](./issupportedforlanguage_.md)
  Returns a Boolean value that indicates whether the given language supports setting custom pronouns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmorphologycustompronoun/requiredkeysforlanguage:)*