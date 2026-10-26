# setCustomPronoun:forLanguage:error:

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
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 8.0+ - Deprecated in 10.0

## Declaration

```objc
- (BOOL) setCustomPronoun:(NSMorphologyCustomPronoun *) features forLanguage:(NSString *) language error:(NSError **) error;
```

#### Return Value

A Boolean value that indicates whether setting the custom pronoun succeeded.

#### Discussion

This method throws if the system doesn’t support custom pronouns for the given language, or if any of the required pronoun keys aren’t set.

## Parameters

- `features`: A [`NSMorphologyCustomPronoun`](../nsmorphologycustompronoun.md) instance for the morphology to use.
- `language`: The language the morphology applies the custom pronoun to.
- `error`: On return, any error encountered while setting the custom pronoun, or `nil` if no error occurred.

## See Also

### Related Documentation
- [+ isSupportedForLanguage:](../nsmorphologycustompronoun/issupportedforlanguage_.md)
  Returns a Boolean value that indicates whether the given language supports setting custom pronouns.
- [+ requiredKeysForLanguage:](../nsmorphologycustompronoun/requiredkeysforlanguage_.md)
  Returns a collection of the custom pronoun keys required by this language.
### Accessing Per-Language Features
- [- customPronounForLanguage:](./custompronounforlanguage_.md)
  Returns any custom pronoun behavior this morphology applies to the given language.
- [NSMorphologyCustomPronoun](../nsmorphologycustompronoun.md)
  A custom pronoun behavior for use in a specific langauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmorphology/setcustompronoun:forlanguage:error:)*